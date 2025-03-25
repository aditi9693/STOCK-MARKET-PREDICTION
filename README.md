# 📈 Stock Market Prediction

This project predicts stock prices using **Linear Regression** and **LSTM models**. It fetches historical stock data using the **Yahoo Finance API**, processes it, and visualizes future stock price trends.

---

## 🚀 Features
- 📊 **Stock Price Prediction** using **Linear Regression & LSTM**.
- 🔍 **Fetch real-time stock data** using `yfinance`.
- 📈 **Data visualization** with charts & graphs.
- 🖥 **Flask Backend** for running predictions via an API.
- 🌐 **Frontend Interface** to visualize stock trends.

---

## 🛠 Tech Stack
- **Backend:** Flask, Python
- **Machine Learning:** scikit-learn, TensorFlow/Keras
- **Data Handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Stock Data API:** Yahoo Finance API
- **Frontend:** HTML, CSS, JavaScript (if applicable)

---

## 💂 Project Structure
```
Stock-Market-Prediction/
👉 backend/                # Flask backend
👉 templates/              # Frontend HTML files
👉 model.py                # ML models (Linear Regression & LSTM)
👉 app.py                  # Main Flask application
👉 Stock_price.ipynb       # Jupyter Notebook for data analysis
👉 requirements.txt        # Required Python dependencies
👉 README.md               # Project documentation
👉 .gitignore              # Ignored files (venv, __pycache__, etc.)
```

---

## ⚙️ Installation & Setup
### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd Stock-Market-Prediction
```

### 🔹 Step 2: Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 🔹 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project
### 🔹 Run Flask Backend
```bash
python app.py
```
- The API will be available at `http://127.0.0.1:5000/`

### 🔹 Run Jupyter Notebook (For Model Training)
```bash
jupyter notebook
```

---

## 📊 Example Usage
To predict stock prices, send a request to:
```bash
GET /predict?symbol=AAPL
```
This returns future predictions for Apple stock (`AAPL`).

---

## 🏰 Future Improvements
- ✅ Add more ML models (XGBoost, ARIMA).
- ✅ Improve frontend UI with interactive graphs.
- ✅ Deploy on cloud (AWS, GCP, or Heroku).

---

## 🤝 Contributing
Feel free to contribute by submitting pull requests! 🚀

---

## 🐟 License
This project is **MIT Licensed**.

---

### 💎 Contact
For any queries, reach out at aditivatsa2003@gmail.com.

