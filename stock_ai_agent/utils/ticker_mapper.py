class TickerMapper:

    def __init__(self):

        # company name → NSE ticker
        self.company_map = {
            "tcs": "TCS.NS",
            "infosys": "INFY.NS",
            "reliance": "RELIANCE.NS",
            "hdfc": "HDFCBANK.NS",
            "hdfc bank": "HDFCBANK.NS",
            "icici": "ICICIBANK.NS",
            "icici bank": "ICICIBANK.NS",
            "wipro": "WIPRO.NS"
        }

    def get_tickers(self, query: str):

        query = query.lower()
        tickers = []

        for company, ticker in self.company_map.items():

            if company in query and ticker not in tickers:
                tickers.append(ticker)

        return tickers
