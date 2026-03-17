import matplotlib.pyplot as plt


class StockVisualizer:

    def __init__(self, data):
        self.data = data

    def plot_price(self):
        """
        Plot stock closing price
        """

        plt.figure()

        plt.plot(self.data["Close"])

        plt.title("Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price")

        plt.show()

    def plot_moving_averages(self):
        """
        Plot price with SMA and EMA
        """

        plt.figure()

        plt.plot(self.data["Close"], label="Close")
        plt.plot(self.data["SMA_14"], label="SMA 14")
        plt.plot(self.data["EMA_14"], label="EMA 14")

        plt.title("Price with Moving Averages")

        plt.legend()

        plt.show()

    def plot_rsi(self):
        """
        Plot RSI indicator
        """

        plt.figure()

        plt.plot(self.data["RSI_14"], label="RSI")

        plt.axhline(70)
        plt.axhline(30)

        plt.title("RSI Indicator")

        plt.legend()

        plt.show()
