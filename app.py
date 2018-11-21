from flask import Flask
import random
import cleanup
import tokenize
import wordcount
import sample
import sentance


# connect to the web
app = Flask(__name__)


@app.route('/')
def result():
    #process and import file
    hgram = wordcount.dict_words(cleanup.text_list('text/heart_of_darkness.txt'))
    total = wordcount.sum_value(hgram)
    loop = 30
    result = sentance.sentance(hgram, total, loop)
    #create resulting object
    return result

@app.route('/tuna')
def tuna():
    return 'Tuna Fuck YeaH!'
    # If you want to make a variable inside the URL you need to use angle
    # brackets <>   for example to insert username into URL  do <username>


if __name__ == "__main__":
    #this makes it so that we only call the servier
    #when run directly
    app.run(debug =True)
