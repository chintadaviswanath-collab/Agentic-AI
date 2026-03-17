import json
import re
from llm.groq_client import GroqClient
from tools.tool_executor import ToolExecutor
from utils.ticker_mapper import TickerMapper

VALID_PERIODS = ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]

def normalize_period(period: str) -> str:
    if not period:
        return "3mo"

    period = str(period).lower().replace("p","").replace(" ","").strip()

    mapping = {
        "1d": "1d",
        "5d": "5d",
        "1mo": "1mo",
        "3mo": "3mo",
        "6mo": "6mo",
        "6m": "6mo",
        "1month": "1mo",
        "3months": "3mo",
        "6months": "6mo",
        "1y": "1y",
        "1year": "1y",
        "2y": "2y",
        "2years": "2y",
        "5y": "5y",
        "5years": "5y",
        "10y": "10y",
        "10years": "10y",
        "ytd": "ytd",
        "max": "max"
    }

    return mapping.get(period, "3mo")


class StockAgent:

    def __init__(self):
        self.llm = GroqClient()
        self.executor = ToolExecutor()
        self.mapper = TickerMapper()

        self.allowed_tools = [
            "current_price",
            "average_price",
            "max_price",
            "min_price",
            "calculate_rsi",
            "calculate_moving_average",
            "calculate_ema",
            "calculate_sma",
            "fundamentals",
            "plot_chart",
        ]


    def detect_tools_from_query(self, query: str):

        q = query.lower()
        tools = []

        # Detect period from query
        period = None

        if "3 month" in q or "3 months" in q:
            period = "3mo"

        elif "6 month" in q or "6 months" in q:
            period = "6mo"

        elif "1 year" in q or "12 month" in q:
            period = "1y"

        # ---------------- PRICE TOOLS ----------------

        if "average price" in q or "average" in q:
            tools.append({
                "tool": "average_price",
                "args": {"period": period or "3mo"}
            })

        elif "price" in q:
            tools.append({
                "tool": "current_price",
                "args": {}
            })

        if "max" in q or "highest" in q:
            tools.append({
                "tool": "max_price",
                "args": {"period": period or "3mo"}
            })

        if "min" in q or "lowest" in q:
            tools.append({
                "tool": "min_price",
                "args": {"period": period or "3mo"}
            })


        # ---------------- INDICATORS ----------------

        indicator_period = period or "3mo"

        # Detect window size like "20 day", "50 day"
        window = 20
        match = re.search(r'(\d+)\s*day', q)
        if match:
            window = int(match.group(1))

        if "rsi" in q:
            tools.append({
                "tool": "calculate_rsi",
                "args": {
                    "window": window,
                    "period": indicator_period
                }
            })

        if "moving average" in q:
            tools.append({
                "tool": "calculate_moving_average",
                "args": {
                    "window": window,
                    "period": indicator_period
                }
            })

        if "ema" in q:
            tools.append({
                "tool": "calculate_ema",
                "args": {
                    "window": window,
                    "period": indicator_period
                }
            })

        if "sma" in q:
            tools.append({
                "tool": "calculate_sma",
                "args": {
                    "window": window,
                    "period": indicator_period
                }
            })


        # ---------------- CHART ----------------

        if "chart" in q or "plot" in q or "graph" in q:
            tools.append({
                "tool": "plot_chart",
                "args": {"period": period or "6mo"}
            })

        # ---------------- FUNDAMENTALS ----------------

        if "fundamental" in q or "pe ratio" in q or "valuation" in q:
            tools.append({
                "tool": "fundamentals",
                "args": {}
            })

        return tools


    def analyze(self, query: str) -> str:

        # Extract tickers
        tickers = self.mapper.get_tickers(query)

        if not tickers:
            return "Could not identify the company tickers."

        # STEP 1: rule-based tool detection
        steps = self.detect_tools_from_query(query)

        # STEP 2: fallback to LLM if rules fail
        if not steps:

            tool_prompt = f"""
You are a financial AI assistant.

User Question:
{query}

Stock Tickers:
{tickers}

Allowed tools:
{', '.join(self.allowed_tools)}

Return ONLY a JSON array of tool steps.

Example:
[
  {{
    "tool": "current_price",
    "args": {{}}
  }}
]
"""

            llm_response = self.llm.generate(tool_prompt)

            try:
                start = llm_response.find("[")
                end = llm_response.rfind("]") + 1
                steps = json.loads(llm_response[start:end])
            except Exception:
                return "Could not understand tool plan."

        # STEP 3: execute tools
        results = {}

        for ticker in tickers:

            results[ticker] = {}

            for step in steps:

                tool_name = step.get("tool")
                args = step.get("args", {}).copy()

                if tool_name not in self.allowed_tools:
                    continue

                args["ticker"] = ticker

                if "period" in args:
                    args["period"] = normalize_period(args["period"])

                try:
                    result = self.executor.execute(tool_name, args)
                    results[ticker][tool_name] = result

                except Exception as e:
                    results[ticker][tool_name] = f"Error: {str(e)}"

        if not results:
            return "No tools executed successfully."

        # Validate data
        valid_data = False

        for ticker in results:
            for tool in results[ticker]:

                value = results[ticker][tool]

                if value is None:
                    continue

                if isinstance(value, dict) and len(value) == 0:
                    continue

                if isinstance(value, list) and len(value) == 0:
                    continue

                valid_data = True

        if not valid_data:
            return "Unable to retrieve sufficient stock data to answer the query."

        # STEP 4: reasoning
        summary_prompt = f"""
You are a financial analysis assistant.

User Question:
{query}

Stock Data (from tools):
{json.dumps(results, indent=2)}

STRICT RULES:
- ONLY use the numerical data provided in "Stock Data".
- NEVER invent or assume stock prices.
- NEVER simulate examples.
- If data is missing, say the calculation cannot be performed.

Instructions:
- Answer the user's question directly.
- If multiple stocks exist, compare them.
- Keep the answer within 2–3 sentences.
- Format numbers to 2 decimal places.
"""

        final_answer = self.llm.generate(summary_prompt)

        return final_answer
