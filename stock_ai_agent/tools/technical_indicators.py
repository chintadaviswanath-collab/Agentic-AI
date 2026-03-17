import pandas as pd


class TechnicalIndicators:

    def __init__(self, data):

        self.data = data

    def calculate_sma(self, window):

        return self.data["Close"].rolling(window=window).mean()
    
    def calculate_ema(self, window=14):
        """
        Exponential Moving Average
        """
        return self.data["Close"].ewm(span=window, adjust=False).mean()

    def calculate_rsi(self, period=14):

        """
        Relative strength index
        """

        delta = self.data["Close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return rsi

    
