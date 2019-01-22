from flask import Flask, render_template
import random
import cleanup
import markov

# connect to the webwith unique name
app = Flask(__name__)


@app.route('/')
def main():
    #process and import file
    words = cleanup.text_list('text/dickens.txt')
    m_chain = markov.order_mchain(2, words)
    c_start = markov.start_token(m_chain)
    walk_the_dog = markov.walk(c_start, m_chain)
    almost = markov.finalize(walk_the_dog)
    home = str(almost)
    print(home)
    # # #create resulting object
    # return home
    return render_template('main.html', sentance = home)



if __name__ == "__main__":
    #this makes it so that we only call the server
    #when run directly
    app.run()

# app.run(debug =True)



    # @app.route('/')
    # def result():
    #     #process and import file
    #     hgram = wordcount.dict_words(cleanup.text_list('text/dikens.txt'))
    #     result = sentance.sentance(hgram, total, loop)
    #     #create resulting object
    #     return result
