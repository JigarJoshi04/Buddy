import os
import openai


class OpenAI:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def chat_completion_api(self, messages):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
        )
        return response
