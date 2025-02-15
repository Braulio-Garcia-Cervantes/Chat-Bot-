from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

class IntentClassifier:
    def __init__(self):
        #initialize objects
        self.vectorizer = CountVectorizer()
        self.classifier = LogisticRegression()
    def train(self, training_data): #training_data is a list of tuples
        texts, labels = zip(*training_data) #'zip': splits the list of tuples into two seperate lists
        x = self.vectorizer.fit_transform(texts) #converts the texts into a matrix representation of the data
        y = labels #the intents are stored to be used later as the target for training the classifier
        self.classifier.fit(x, y) #this trains the classifier: learns the relationship between the text features (represented as word counts) and their associated intents (labels)
        #essentially means: that even though the user input was not the exact text we had in our training data, the program will recognize the similarities between texts
    def predict(self, user_input):
        x = self.vectorizer.transform([user_input]) #converts user_input into the same matrix as above and analyzes it
        return self.classifier.predict(x)[0] #uses the classifier to predict the intent for the given input 'x' based on what it learned from the train method; since there is only one input: user_input, we return [0]


        #downsides of this approach: limited to our predefined training data that we would have to keep expanding


