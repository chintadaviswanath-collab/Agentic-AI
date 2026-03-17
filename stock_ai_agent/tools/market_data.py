import yfinance as yf
import pandas as pd


class MarketDataFetcher:

    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def get_price_history(self, period="1y"):
        """
        Fetch historical stock price data safely.
        Ensures dataframe is valid and not empty.
        """

        try:
            data = self.stock.history(period=period)

            # Handle empty dataframe
            if data is None or data.empty:
                return pd.DataFrame()

            # Round numeric values
            data = data.round(2)

            # Ensure Close column exists
            if "Close" not in data.columns:
                return pd.DataFrame()

            return data

        except Exception as e:
            print(f"MarketDataFetcher error: {e}")
            return pd.DataFrame()

    def get_company_info(self):
        """
        Fetch company information safely
        """
        try:
            return self.stock.info
        except Exception:
            return {}

    def get_financials(self):
        """
        Fetch financial statements
        """
        try:
            return self.stock.financials
        except Exception:
            return {}

    def get_balance_sheet(self):
        """
        Fetch balance sheet
        """
        try:
            return self.stock.balance_sheet
        except Exception:
            return {}

    def get_cashflow(self):
        """
        Fetch cash flow statement
        """
        try:
            return self.stock.cashflow
        except Exception:
            return {}
