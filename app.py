from flask import Flask, render_template, request, jsonify
import pandas as pd
from prophet import Prophet
import os

app = Flask(__name__)

# Global variable to store models
models = {}

def get_models():
    if models:
        return models
    
    try:
        if os.path.exists('Covid-19.csv'):
            df = pd.read_csv('Covid-19.csv')
        else:
            # Try looking in Downloads if not found (for local dev convenience)
            # This is a fallback
            df = pd.read_csv(r'C:\Users\HP\Downloads\Covid-19.csv')
            
        df['Date'] = pd.to_datetime(df['Date'])
        
        for col in ['Confirmed', 'Active', 'Recovered', 'Deaths']:
            df_tmp = df.groupby(['Date'])[col].sum().reset_index()
            df_tmp.columns = ['ds', 'y']
            m = Prophet()
            m.fit(df_tmp)
            models[col] = m
    except Exception as e:
        print(f"Error loading/training models: {e}")
        return None
    return models

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    try:
        days = int(request.args.get('days', 7))
    except ValueError:
        days = 7
        
    trained_models = get_models()
    if not trained_models:
        return jsonify({'error': 'Models not trained. Check if Covid-19.csv is present.'}), 500

    results = {}
    for col, m in trained_models.items():
        future = m.make_future_dataframe(periods=days)
        forecast = m.predict(future)
        
        # Serialize dates and values
        # We return the whole history + forecast for plotting
        data = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
        data['ds'] = data['ds'].dt.strftime('%Y-%m-%d')
        results[col] = data.to_dict('records')

    return jsonify(results)

if __name__ == '__main__':
    # Build models on startup
    print("Training models...")
    get_models()
    print("Models trained.")
    app.run(debug=True, port=5000)
