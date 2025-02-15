import nltk
class ConvoHistory():
    def __init__(self):
        self.history = []
    def save_convo(self, user_input, response):
        self.history.append((user_input, response))


    @property
    def get_history(self):
        if not self.history:
            return "No chat history found."

        formatted = ""
        #enumerate will give us access to index and element
        for i, (user_input, input_text) in enumerate(self.history): #similar thought process to a leet code problem, every even index is the bot's response
            if i % 2 == 0:
                formatted += f"AI MODEL: {input_text}\n"
            else:
                formatted += f"YOU: {user_input}\n"

        return formatted
    def clear_history(self):
        self.history = []
        return "History cleared."