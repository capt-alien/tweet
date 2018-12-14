from flask import Flask
import random
import cleanup
import tokenize
import wordcount
import sample
import sentance
import markov


# connect to the web
app = Flask(__name__)


@app.route('/')
def result():
    #process and import file
    words = cleanup.text_list('text/dickens.txt')
    m_chain = markov.order_mchain(2, words)
    c_start = markov.start_token(m_chain)
    walk_the_dog = markov.walk(c_start, m_chain)
    home = markov.finalize(walk_the_dog)
    # # #create resulting object
    return home



if __name__ == "__main__":
    #this makes it so that we only call the servier
    #when run directly
    app.run(debug =True)




    # @app.route('/')
    # def result():
    #     #process and import file
    #     hgram = wordcount.dict_words(cleanup.text_list('text/dikens.txt'))
    #     result = sentance.sentance(hgram, total, loop)
    #     #create resulting object
    #     return result
