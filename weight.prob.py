# code borrows from Dylan Flinn

import random
from sys import argv
from histogram import text_list
from histogram import dict_words

# create a sum of key values in dict
#sums dictionary in histo
def sum_value(hist):
    dict_total = (sum(hist.values()))
    return dict_total

# created weighted probabliltiy function
def weighted_random(hist, total):
    dict_total = (sum(hist.values()))
    """
    Takes a histogram and returns a weighted random choice from it
    """
    destination = random.randint(0, total)
    for word in hist:
        destination = destination - hist[word]
        if destination < 0:
            return word


if __name__ == '__main__':
    file1 = argv[1]  #file to analyze
    looper = int(argv[2]) # number of times that loop will run
    #processing words and defineing objects
    words = text_list(file1)
    hist1 = dict_words(words)
    total = sum_value(words)
    #run loop for input values
    sentance = []
    for i in range(0,looper):
        rand_word = weighted_random(hist1, total)
        sentance.append(rand_word)

    print(sentance)



        sys.exit()
