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

# takes a histogram and returns a weighted probabibility
def weighted_random(hist, total):
    destination = random.randint(0, total)
    for word in hist:
        destination = destination - hist[word]
        if destination <= 0:
            return word

#takes a histogram and retuns % of each word for comparitive testing
def hist_p(hist):
    total = 0
    for i in hist:
        total = total + hist[i]
    for j in hist:
        hist[j] = round(float((hist[j])/total), 3)
        hist2 = hist
    return hist2


if __name__ == '__main__':
    file1 = argv[1]  #file to analyze
    looper = int(argv[2]) # number of times that loop will run

    #processing words and defineing objects
    words = text_list(file1)
    hist1 = dict_words(words)
    total = sum_value(hist1)
    # print(analysis1)
    #run loop for input values
    sentance = []
    for i in range(0,looper):
        rand_word = weighted_random(hist1, total)
        sentance.append(rand_word)
    #print Results and convert to new histogram for testing
    sentance_hist = dict_words(sentance)
    print(sentance_hist)
    #fist hist anaylsis
    test1 = hist_p(hist1)
    print(test1)
    #sentance hist analysis
    test2 = hist_p(sentance_hist)
    print(test2)
