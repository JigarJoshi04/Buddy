import random


class PreProcessor:
    def __init__(self):
        pass

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
    
    def prepare_messages(self, message_obj_list):
        messages = []
        for msg_obj in message_obj_list:
            messages.append({"role": msg_obj.role, "content": msg_obj.content})
        return messages
    
    def system_content_addition_with_age(self, age_category):
        content = "Have a never ending conversation with no monologues. Make your replies short and sweet, but have a neverending conversation. "
        if age_category == "YOUNG":
            content += "You are an assistant speaking with a three year old. " 
        
        elif age_category == "OLDER":
            content += "You are an assistant speaking with an older person. "
        
        return content
    
    def system_content_addition_with_emotion(self, emotion):
        content = "The person you are having conversation with is in "
        if emotion.lower() == "good":
            content += "good mood, try to maintain his mood in the same state."
        
        elif emotion.lower() == "bad":
            content += "bad mood, try to cheer him up passively"
        
        elif emotion.lower() == "depressed":
            content += "depressed mood. Try to console him and improve his mood actively."
            
        return content
    
    def system_content_addition(self, age_category, emotion):
        return self.system_content_addition_with_age(age_category) + self.system_content_addition_with_emotion(emotion)
        