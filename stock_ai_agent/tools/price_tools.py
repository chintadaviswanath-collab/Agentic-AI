class PriceTools:

    def __init__(self, data):
        """
        data = dataframe returned from MarketDataFetcher
        """
        self.data = data

    def get_close_prices(self):
        """
        Safely return closing price series
        """
        if self.data is None or self.data.empty:
            return None

        if "Close" not in self.data.columns:
            return None

        return self.data["Close"]

    def current_price(self):

        prices = self.get_close_prices()

        if prices is None or len(prices) == 0:
            return None

        return round(float(prices.iloc[-1]), 2)

    def average_price(self):

        prices = self.get_close_prices()

        if prices is None or len(prices) == 0:
            return None

        return round(float(prices.mean()), 2)

    def max_price(self):

        prices = self.get_close_prices()

        if prices is None or len(prices) == 0:
            return None

        return round(float(prices.max()), 2)

    def min_price(self):

        prices = self.get_close_prices()

        if prices is None or len(prices) == 0:
            return None

        return round(float(prices.min()), 2)
