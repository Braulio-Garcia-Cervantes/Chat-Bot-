
from Input_processor import InputProcessor
from convo_history import ConvoHistory
from response_handler import KeywordHandler
from user import User
import nltk


class Bot:
    def __init__(self):
        self.user = User() #creates user object
        self.input_processor = InputProcessor() #creates processor object
        self.response_handler = KeywordHandler(self.input_processor) #creates handler object, we could change the type of handler later
        self.history = ConvoHistory() #creates the convo history chain

    def handle_commands(self, user_input):
        if user_input == "exit":
            print("AI MODEL: GOODBYE!")
            return False
        elif user_input == "username":
            print("AI MODEL: WHAT WOULD YOU LIKE ME TO CALL YOU INSTEAD?")
            new_user_name = self.input_processor.get_input()
            self.user.set_name(new_user_name)
            print("AI MODEL: SOUNDS GOOD, " + self.user.get_name().upper() + "!")
        elif user_input == "clear":
            self.history.clear_history()
            print("AI MODEL: History cleared!")
        elif user_input == "history":
            convo_history = self.history.get_history
            print(convo_history)
        else:
            return True  # Continue the chat loop
        return True  # Continue the chat loop

    def start_chat(self): #introductory messages, lets user pick their name, contains the main chat loop
        print("HI MY NAME IS AI MODEL, WHAT'S YOURS?")
        user_name = self.input_processor.get_input().strip() #solves edge case where user puts white spaces
        if user_name == "":
            user_name = "GUEST"
        self.user.set_name(user_name)
        print(f"NICE TO MEET YOU, " + self.user.get_name().upper() + "! HOW CAN I ASSIST YOU?")

        while True:
            print("\nYou: ")
            user_input = self.input_processor.get_input()
            if not self.handle_commands(user_input):
                break  # Exit the loop if needed
            response = self.get_response(user_input)
            self.history.save_convo(user_input, response)
            print("AI MODEL: " + str(response))

    def get_response(self, user_input): #depending what handler mode we are in, it will process user input and generate responses
        return self.response_handler.generate_response(user_input)


