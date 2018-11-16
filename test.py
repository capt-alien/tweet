import random
from stoch import weighted_probablity
import weight_prob


# Create loop for sentance
def sentance(histogram, total, loop):
    looper = int(loop)
    sentance1= []
    # loop
    for i in range(0, looper):
        weight_word = weight_prob.weighted_random(hgram, total)
        sentance1.append(weight_word)
    return sentance1

#process and import file
hgram = weight_prob.dict_words(weight_prob.text_list('test.txt'))
total= weight_prob.sum_value(hgram)
loop = 15

#create resulting object
result = sentance(hgram, total, loop)
word_string = " "
word_string = word_string.join(word for word in result)
print(word_string)
