# Drew on code from the following artical borrowed code from Faith C.:
# https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
from sys import argv
import cleanup
import sample
import sentance
import dictogram
import random


def order_mchain(order, text_list):
    markov_dict = {}
    # for each word in list, key is word and value is dictogram
    for index in range(len(text_list) - order):
        # text_list[index] should be our word from list
        window = tuple(text_list[index: index + order])
        # check if window is stored in the dictionary already
        if window in markov_dict:
            # if it is, then append it to the existing histogram
            markov_dict[window].add_count([text_list[index + order]])
        else:
            # if not, create new entry with window as key and dictogram as value
            markov_dict[window] = dictogram.Dictogram([text_list[index + order]])
    # return dictionary
    return markov_dict

##Need help
def start_token(markov_model):
    # generate a random word followin START in a corpus
    start_tokens= []
    for key in markov_model:
        if key[0] == "START":
            start_tokens.append(key)
    print(start_tokens)
    token = random.choice(start_tokens)
    return token

def stop_tokens(dictionary):
    # create list of words that ened sentances
    stop_tokens = []
    for key, value in dictionary.items():
        if key[1] == "STOP":
            stop_tokens.append(key)
    return stop_tokens

def walk(start_token, dictionary):
    # walks the markov
    sentance = ['START', start_token[1]]
    #while the last entry in the list sentance is not "STOP"
    while sentance[len(sentance)-1] != 'STOP':
        window = (sentance[len(sentance) - 2], sentance[len(sentance)-1])
        hist = dictionary[tuple(window)]
        next_word = sample.weighted_random(hist, sample.sum_value(hist))
        sentance.append(next_word)
    print(sentance)

    return(sentance)

    # current_token = start_token
    # while current_token not in stop_tokens:
    #     # use current value to referace the m
    #     # sample from histogram of values
    #     rand_token = sample.weighted_random(current_token, sum_value(key))
    #     print(rand_token)
    #     # add new sample to sentence_list
    #     sentence.append(sample_word)
    #     break
    # return sentence



if __name__ == '__main__':
    file1 = argv[1]  #file to analyze
    words = cleanup.text_list(file1)
    m_chain = order_mchain(2, words)
    c_start = start_token(m_chain)
    c_stop = stop_tokens(m_chain)
    walk_the_dog = walk(c_start, m_chain)
    # key = m_chain[0]
    # sentace1 = M_sentance(m_chain, looper, )









# def generate_sentance(length, markov_model):
#     #creates first word
#     current_word = generate_random_start(markov_model)
#     sentance = [current_word]
#     for i in range(0, length):
#         current_dictogram = marcov_model[current_word]
#         random_weighted_word = sample.weighted_random(marcov_model[current_word], sample.sum_value(marcov_model[current_word]))
#         current_word = random_weighted_word
#         sentance.append(current_word)
#     #handles puncuation:
#     return ' '.join(sentence) + '.'
#     return sentence
