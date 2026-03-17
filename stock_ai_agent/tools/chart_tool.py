import matplotlib.pyplot as plt
import os


class ChartTool:

    def __init__(self, data):
        self.data = data

    def plot(self, ticker="stock", fields=["Close"], period="3mo"):

        plt.figure(figsize=(10, 5))

        for field in fields:
            if field in self.data.columns:
                plt.plot(self.data.index, self.data[field], label=field)

        plt.title(f"{ticker} Stock Chart ({period})")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.tight_layout()

        # Create charts directory if it doesn't exist
        os.makedirs("charts", exist_ok=True)

        file_path = f"charts/{ticker}_{period}_chart.png"

        # Save the chart
        plt.savefig(file_path)

        # Show chart to user
        plt.show()

        plt.close()

        return file_path
