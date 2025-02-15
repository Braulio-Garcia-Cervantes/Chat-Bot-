import abc
import nltk
import requests
#nltk.download('all')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import intent_classifier
from intent_classifier import IntentClassifier



class ResponseHandler():
    @abc.abstractmethod
    def generate_response(self, user_input):
        pass


class KeywordHandler(ResponseHandler):
    def __init__(self, input_processor):
        self.commands = ["exit", "username", "clear", "history"]
        self.input_processor = input_processor
        self.intent_classifier = intent_classifier.IntentClassifier()
        self.training_data = [
            ("What is the weather like?", "weather"),
            ("Tell me the news", "news"),
            ("Clear the chat history", "clear"),
            ("Show me the conversation history", "history"),
            ("Exit", "exit"),
        ]
        self.sentiment_api_url =  "http://127.0.0.1:8000/analyze_sentiment"


    def generate_response(self, user_input: str):
        self.intent_classifier.train(self.training_data)
        processed_input = self.input_processor.process_input(user_input)  # filter user_input
        entities = self.input_processor.extract_entities(user_input)  # then extract entities and store them
        intent = self.intent_classifier.predict(user_input)
        sentiment_label, sentiment_score = self.input_processor.get_sentiment(user_input)

        if sentiment_label == "POSITIVE":
            return "AI MODEL: Love to hear it!"
        elif sentiment_label == "NEGATIVE":
            return "AI MODEL: Oh no, that's awful!"


        if intent == "weather":
            location = entities[
                "GPE"]  # we look in the gpe list which already stored all possible location entities from the users input and get the location
            date = entities[
                "DATE"]  # we look in the dates list which already stored all possible date entities from the users input and get the date
            if location:  # if a location exists: we will take the first index in those lists, also checking if a date exists, if not it will default to 'today'
                return f"The weather in {location[0]} for {date[0] if date else 'today'} is sunny and 90 degrees."
            return "Please provide a location to get the weather from."
        elif intent == "news":
            return "Broc is the new up and coming Software Engineer in 2025!"  # Implement a news API that gathers the top 5 stories by most recent date

        elif any(command in processed_input for command in self.commands):
            return "COMMAND SUCCESSFULLY EXECUTED."

        return "Sorry, I am still undergoing development, I don't currently have information on this."

