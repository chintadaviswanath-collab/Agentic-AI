📊 AI Stock Analyst Agent

An intelligent stock analysis agent that uses LLM + financial tools to analyze stocks, compute indicators, and provide insights like a real analyst.

🚀 Features: 

📈 Fetch current stock prices
📊 Calculate historical metrics:
Average price
Highest / Lowest price

📉 Technical Indicators:

RSI (Relative Strength Index)
SMA (Simple Moving Average)
EMA (Exponential Moving Average)
Moving Average
🔍 Multi-stock comparison
🧠 LLM-powered reasoning & interpretation
📊 Chart generation (lightweight, optimized)

🧠 How It Works:

The agent follows a Tool + LLM architecture:

User enters a stock query
Agent detects required tools (rule-based + LLM fallback)
Tools fetch real stock data (via yfinance)
LLM interprets results and generates insights


⚙️ Installation & Setup:

1️⃣ Clone the Repository
git clone <your-repo-link>
cd stock_ai_agent

2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate


Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup API Key

Create a .env file in the root directory:
GROQ_API_KEY=your_api_key_here

5️⃣ Run the Application
python main.py

💬 Example Queries:

Try asking:

1.what is the current price of tcs
2.calculate average price of infosys for last 3 months
3.calculate 20 day sma of tcs
4.calculate rsi of reliance
5.compare price of tcs and infosys
6.show chart of wipro

⚠️ Limitations:
Depends on yfinance data availability
Limited to supported stock tickers
No real-time streaming data (uses recent historical data)
Chart queries are optimized to avoid large data loads
Does not provide financial advice (educational purposes only)

🔮 Future Improvements:

📊 Advanced indicators (MACD, Bollinger Bands)
📉 Buy/Sell signal generation
🌐 Integration with NSE / Screener APIs
🖥️ Web interface (Streamlit)
🤖 Autonomous financial analysis agent

🛠️ Tech Stack:

Python
yfinance
Pandas / NumPy
Matplotlib
Groq LLM API
