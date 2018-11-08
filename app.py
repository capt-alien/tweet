from flask import Flask
import random
from stoch import weighted_probablity
from dictionary_words import load_words
from dictionary_words import random_word

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is a test!'



#Insert code for app here
# def run():
#     histogram = ["there", "once", "was", "a", "man", "from", "nantucket"]
#     weighted_histogram = [["there", 0.1], ["once", 0.2], ["was", 0.1], ["a", 0.1], ["man", 0.1], ["from", 0.1], ["nantucket", 0.3]]
#     loops = int(input("Enter number of words in new sentance: "))
#     for _ in range(loops):
#         return(weighted_probablity(weighted_histogram))



if __name__ == "__main__":
    app.run()
