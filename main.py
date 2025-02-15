import nltk
#print(nltk.__version__)
#nltk.download('all')


from Bot import Bot
import spacy

spacy.load('en_core_web_sm')



class Main:
    if __name__ == "__main__":
        chatbot = Bot()
        chatbot.start_chat()

