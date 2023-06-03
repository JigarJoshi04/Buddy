import random


class Prompt:
    def conversation_divider():
        story_percentage = 20
        quote_percentage = 30
        conversation_percentage = 50
        
        r = random.randint(1,100)
        if r <= conversation_percentage:
            return "CHAT"

        elif conversation_percentage < r <= conversation_percentage + quote_percentage:
            return "QUOTE"
        
        elif conversation_percentage + quote_percentage < r <= 100:
            return "STORY"

        
    
    