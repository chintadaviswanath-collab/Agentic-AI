# 📊 AI Stock Analyst Agent

An intelligent stock analysis agent that uses **LLM + financial tools** to analyze stocks, compute indicators, and provide insights like a real analyst.

---

## 🚀 Features

- 📈 Fetch current stock prices  
- 📊 Calculate historical metrics:
  - Average price  
  - Highest / Lowest price  
- 📉 Technical Indicators:
  - RSI (Relative Strength Index)  
  - SMA (Simple Moving Average)  
  - EMA (Exponential Moving Average)  
  - Moving Average  
- 🔍 Multi-stock comparison  
- 🧠 LLM-powered reasoning & interpretation  
- 📊 Chart generation (lightweight, optimized)  

---

## 🧠 How It Works

The agent follows a **Tool + LLM architecture**:

1. User enters a stock query  
2. Agent detects required tools (rule-based + LLM fallback)  
3. Tools fetch real stock data (via `yfinance`)  
4. LLM interprets results and generates insights  

---

## 📁 Project Structure

    stock_ai_agent/
    │
    ├── agents/        # Core agent logic
    ├── tools/         # Data fetching & calculations
    ├── utils/         # Helper utilities (ticker mapping)
    ├── llm/           # LLM client (Groq API)
    ├── config/        # Configurations (optional)
    ├── data/          # Optional storage (charts/cache)
    │
    ├── main.py        # Entry point
    ├── requirements.txt
    ├── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd stock_ai_agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup API Key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the Application

```bash
python main.py
```

---

## 💬 Example Queries

```text
what is the current price of tcs
```

```text
calculate average price of infosys for last 3 months
```

```text
calculate 20 day sma of tcs
```

```text
calculate rsi of reliance
```

```text
compare price of tcs and infosys
```

```text
show chart of wipro
```

---

## ⚠️ Limitations

- Depends on `yfinance` data availability  
- Limited to supported stock tickers  
- No real-time streaming data (uses recent historical data)  
- Chart queries are optimized to avoid large data loads  
- Does not provide financial advice (educational purposes only)  

---

## 🔮 Future Improvements

- 📊 Advanced indicators (MACD, Bollinger Bands)  
- 📉 Buy/Sell signal generation  
- 🌐 Integration with NSE / Screener APIs  
- 🖥️ Web interface (Streamlit)  
- 🤖 Autonomous financial analysis agent  

---

## 🛠️ Tech Stack

- Python  
- yfinance  
- Pandas / NumPy  
- Matplotlib  
- Groq LLM API  

---

## 📌 Disclaimer

This project is for **educational purposes only** and should not be used for real financial decision-making.

---

## 👨‍💻 Author

Developed as an AI-powered stock analysis system combining **data tools + LLM reasoning**.

---
