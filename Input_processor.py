import nltk
import requests
#nltk.download('all')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import spacy


class InputProcessor:

    def __init__(self):
        self.ps = PorterStemmer()  # initializes the stemmer
        self.stop_words = set(stopwords.words('english'))  # gets the english stop words ex:(in, a, the, etc.)
        self.nlp = spacy.load('en_core_web_sm') #loads the spacy english model
        self.sentiment_api_url = "http://127.0.0.1:8000/analyze_sentiment"

    def get_input(self):
        return input()

    def process_input(self, user_input):
        tokens = word_tokenize(user_input)  #tokenize the input (split into individual words)

        #removes all stop words by creating a new list by iterating over each 'word' in 'tokens'
        #and only adding words that satisfy the if condition; reason for this, this will be the filtered string that the AI model will process and respond to

        filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]

        stemmed_tokens = [self.ps.stem(word) for word in filtered_tokens]  #stem the words

        return stemmed_tokens  #return the final product of the string after all the processing

    #designed to extract specific types of named entities from a piece of text using spaCy:
    def extract_entities(self, user_input):
        doc = self.nlp(user_input) #passing the user_input into the nlp model allows spacy to process it through its pipeline and return a doc object (doc object: contains the string as well as
        #annotations on that text for various linguistic features such as part-of-speech tags, syntactic dependencies, and named entities.)

        entities = {"PERSON": [], "GPE": [], "DATE": [], "MONEY": []} #dictionary that holds the name of the lists as keys and defaulted empty lists for their pairs

        #'.ents' is a predefined function from the spacy package where the model recognizes entities in the user_input and stores into the list
        for ent in doc.ents:
            if ent.label_ == "PERSON": #ent.label_: the label of the entity, which corresponds to the category (e.g., "PERSON", "GPE", or "DATE").
                entities["PERSON"].append(ent.text) #ent.text: the text of the entity (e.g., "Albert Einstein", "New York").
            elif ent.label_ == "GPE":  #Geopolitical Entity (Country, City, etc.)
                entities["GPE"].append(ent.text)
            elif ent.label_ == "DATE":
                entities["DATE"].append(ent.text)
            elif ent.label_ == "MONEY":
                entities["MONEY"].append(ent.text)

        return entities
    def get_sentiment(self, text: str):
        response = requests.post(self.sentiment_api_url, json={"text": text}) #sends the POST request to the api for analysis
        if response.status_code == 200: #check if the api call was successful
            sentiment_data = response.json() #if so, convert the response to a json object
            return sentiment_data["label"], sentiment_data["score"] #return the json formatted sentiment
        else:
            print("Error analyzing sentiment.")
            return "NEUTRAL", 0.0



