import pandas as pd


class FundamentalAnalyzer:

    def __init__(self, stock):
        self.stock = stock

    def get_income_statement(self):
        return self.stock.financials

    def get_balance_sheet(self):
        return self.stock.balance_sheet

    def get_cash_flow(self):
        return self.stock.cashflow

    def get_key_metrics(self):

        try:
            info = self.stock.info
        except Exception as e:
            print("Failed to fetch fundamental data:", e)
            return {}

        metrics = {
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "roe": info.get("returnOnEquity"),
            "debt_to_equity": info.get("debtToEquity"),
            "eps": info.get("trailingEps"),
            "revenue_growth": info.get("revenueGrowth"),
        }

        return metrics

