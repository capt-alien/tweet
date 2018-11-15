from flask import Flask
import random
import weight_prob

# Create loop for sentance
def sentance(histogram, total, loop):
    looper = int(loop)
    sentance1= []
    # loop
    for i in range(0,looper):
        weight_word = weight_prob.weighted_random(histogram, total)
        sentance1.append(weight_word)
    return sentance1


# connect to the web
app = Flask(__name__)


@app.route('/')
def result():
    #process and import file
    hgram = weight_prob.dict_words(weight_prob.text_list('test.txt'))
    total = weight_prob.sum_value(hgram)
    loop = 15
    result = sentance(hgram, total, loop)
    #create resulting object
    return str(result)

@app.route('/tuna')
def tuna():
    return 'Tuna Fuck YeaH!'
    # If you want to make a variable inside the URL you need to use angle
    # brackets <>   for example to insert username into URL  do <username>


if __name__ == "__main__":
    #this makes it so that we only call the servier
    #when run directly
    app.run(debug =True)
