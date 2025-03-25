from flask import Flask, render_template, jsonify, request
import yfinance as yf
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os
import pandas as pd
from functools import lru_cache
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Cache models
@lru_cache(maxsize=None)
def load_models():
    lstm_model = load_model('backend/lstm_model.h5')
    lstm_model.compile(optimizer='adam', loss='mse')
    
    with open('backend/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    return lstm_model, scaler

def fetch_stock_data(symbol, days=66):
    stock = yf.Ticker(symbol)
    df = stock.history(period=f"{days}d")
    if df.empty or 'Close' not in df.columns:
        raise ValueError(f"No data available for {symbol}")
    return df[['Close']]

def generate_plot(symbol, actual, lstm_pred):
    plt.figure(figsize=(10, 5))
    plt.plot(actual.index, actual.values, label='Actual', color='blue')
    plt.plot(actual.index[-1], lstm_pred, 'ro', label='LSTM Prediction')
    plt.title(f'{symbol} Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    img = BytesIO()
    plt.savefig(img, format='png', dpi=100)
    img.seek(0)
    plt.close()
    return base64.b64encode(img.getvalue()).decode('utf-8')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        symbol = request.form['symbol'].upper()
        lstm_model, scaler = load_models()
        data = fetch_stock_data(symbol)
        
        # LSTM Prediction
        scaled_data = scaler.transform(data.values)
        lstm_input = scaled_data[-60:].reshape(1, 60, 1)
        lstm_value = float(scaler.inverse_transform(lstm_model.predict(lstm_input))[0][0])
        
        plot_url = generate_plot(symbol, data['Close'], lstm_value)
        
        return jsonify({
            'symbol': symbol,
            'lstm': round(lstm_value, 2),
            'plot_url': plot_url,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    os.makedirs("backend", exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)