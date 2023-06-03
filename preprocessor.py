import random


class PreProcessor:
    def __init__(self, input_text):
        self.input_text = input_text
 
    def conversation_divider(self):
        story_percentage = 40
        quote_percentage = 10
        conversation_percentage = 50
        
        r = random.randint(1,100)
        if r <= conversation_percentage:
            return "CHAT"

        elif conversation_percentage < r <= conversation_percentage + quote_percentage:
            return "QUOTE"
        
        elif conversation_percentage + quote_percentage < r <= 100:
            return "STORY"