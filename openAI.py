import openai


class OpenAI:
    def __init__(self):
        self.model = "gpt-3.5-turbo"

    def chat_completion_api(self, messages):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
        )
        return response
