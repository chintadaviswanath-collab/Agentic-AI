from tools.market_data import MarketDataFetcher
from tools.price_tools import PriceTools
from tools.technical_indicators import TechnicalIndicators
from tools.fundamental_analysis import FundamentalAnalyzer
from tools.sql_tool import SQLTool
from tools.chart_tool import ChartTool

VALID_PERIODS = ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]

def normalize_period(period):
    """
    Convert period strings from queries to valid yfinance periods
    """
    period = str(period).lower().replace("p", "").strip()
    if period in VALID_PERIODS:
        return period
    if "3 month" in period:
        return "3mo"
    if "1 month" in period:
        return "1mo"
    if "6 month" in period:
        return "6mo"
    if "1 year" in period:
        return "1y"
    return "3mo"  # default

class ToolExecutor:
    """
    Executes all tools deterministically.
    """
    def __init__(self):
        self.sql = SQLTool()

    def execute(self, tool_name, args):
        ticker = args.get("ticker")
        period = normalize_period(args.get("period", "3mo"))
        window = args.get("window", 14)

        if not ticker:
            raise ValueError("Ticker is required for tool execution.")

        # 1️⃣ Load from SQL cache
        table_name = ticker.replace(".", "_") + "_prices"
        data = self.sql.load_dataframe(table_name)

        # 2️⃣ Fetch from yfinance if cache missing
        if data is None:
            fetcher = MarketDataFetcher(ticker)
            data = fetcher.get_price_history(period)
            self.sql.save_dataframe(data, table_name)

        # 3️⃣ Instantiate tools
        price_tool = PriceTools(data)
        indicators = TechnicalIndicators(data)
        fundamental_tool = FundamentalAnalyzer(ticker)  # assumes init handles fetch

        # 4️⃣ Execute price tools
        if tool_name == "current_price":
            return price_tool.current_price()
        elif tool_name == "average_price":
            return price_tool.average_price()
        elif tool_name == "max_price":
            return price_tool.max_price()
        elif tool_name == "min_price":
            return price_tool.min_price()

        # 5️⃣ Execute technical indicators
        elif tool_name == "calculate_rsi":
            return round(indicators.calculate_rsi(period=window).iloc[-1], 2)
        elif tool_name == "calculate_sma":
            return round(indicators.calculate_sma(window=window).iloc[-1], 2)
        elif tool_name == "calculate_ema":
            return round(indicators.calculate_ema(window=window).iloc[-1], 2)
        elif tool_name == "calculate_moving_average":
            # alias to SMA for simplicity
            return round(indicators.calculate_sma(window=window).iloc[-1], 2)

        # 6️⃣ Execute fundamental analysis
        elif tool_name == "fundamentals":
            return fundamental_tool.get_key_metrics()

        elif tool_name == "plot_chart":
            chart_tool = ChartTool(data)
            return chart_tool.plot(ticker=ticker, period=period)


        else:
            raise ValueError(f"Unknown tool: {tool_name}")


