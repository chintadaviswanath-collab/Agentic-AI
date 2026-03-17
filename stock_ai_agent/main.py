from agents.stock_agent import StockAgent


def main():

    print("=" * 60)
    print("📈 AI Stock Analyst Agent")
    print("=" * 60)
    print("Examples:")
    print("- What is the current price of TCS?")
    print("- Compare TCS and Infosys price")
    print("- Show RSI of Reliance")
    print("- Plot chart of HDFC for 6 months")
    print("- Show fundamentals of Wipro")
    print("=" * 60)

    agent = StockAgent()

    while True:
        try:
            query = input("\nAsk something about stocks (or type 'exit' to quit): ").strip()

            if not query:
                print("Please enter a question.")
                continue

            if query.lower() in ["exit", "quit"]:
                print("\n👋 Exiting AI Stock Analyst Agent.")
                break

            print("\n🔎 Analyzing...\n")

            # Run agent
            answer = agent.analyze(query)

            print("📊 AI Answer:\n")
            print(answer)

        except KeyboardInterrupt:
            print("\n\nInterrupted. Exiting safely.")
            break

        except Exception as e:
            print("\n⚠️ Error occurred:")
            print(str(e))


if __name__ == "__main__":
    main()
