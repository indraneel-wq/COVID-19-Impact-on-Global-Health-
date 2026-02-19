# 🦠 COVID-19 Forecast Dashboard

A robust machine learning web application that visualizes and predicts the future trajectory of COVID-19 cases (Active, Confirmed, Recovered, Deaths) using state-of-the-art time-series forecasting.

## 🌟 Overview

This project provides an intuitive dashboard for monitoring pandemic trends. By leveraging **Facebook Prophet**, an advanced additive regression model, it analyzes historical data from the `Covid-19.csv` dataset to generate accurate forecasts for the upcoming days. This tool is designed for researchers, data enthusiasts, and anyone interested in understanding public health data trends.

## 🚀 Key Features

*   **Interactive Dashboard**: A clean, responsive interface built with Bootstrap and Chart.js.
*   **Multi-Metric Forecasting**: Simultaneously predicts Active, Confirmed, Recovered, and Deceased cases.
*   **Dynamic Timeframe**: User-controlled forecast horizon (predict 7 days, 30 days, or more into the future).
*   **Visual Data Representation**: Interactive line charts with confidence intervals for easy trend analysis.
*   **Robust Backend**: Powered by Flask for efficient data processing and API management.

## 🛠️ Tech Stack

*   **Backend**: Python, Flask
*   **Machine Learning**: Prophet (Time-series forecasting)
*   **Data Processing**: Pandas
*   **Frontend**: HTML5, CSS3, Bootstrap 5, Chart.js

## 📸 Usage

1.  **Dashboard View**: The home page displays the latest forecasted numbers for all four metrics.
2.  **Custom Forecast**: Enter the number of days you want to predict (e.g., 30) in the "Forecast Horizon" box and click "Update Forecast".
3.  **Analyze Charts**:
    *   **Active Cases Chart**: Tracks the specific trend of active infections.
    *   **Cumulative Metrics Chart**: Compares the growth of Confirmed, Recovered, and Death cases over time.

## ⚙️ Setup & Installation

Follow these steps to run the project locally on your machine.

### Prerequisites
*   Python 3.8 or higher installed.
*   Git installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/covid-19-forecast-dashboard.git
cd covid-19-forecast-dashboard
```

### Step 2: Create a Virtual Environment (Recommended)
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```
The application will start on `http://localhost:5000`.

## 📁 Project Structure

```
├── app.py              # Main Flask application logic
├── templates/
│   └── index.html      # Frontend HTML dashboard
├── Covid-19.csv        # Dataset used for training
├── requirements.txt    # List of Python dependencies
├── Procfile            # Configuration for deployment (e.g., Render/Heroku)
└── README.md           # Project documentation
```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

---
*Developed by [Your Name]*
