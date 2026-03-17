from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME


class GroqClient:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, prompt):

        completion = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content
