# Drew on code from the following artical:
# https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
from sys import argv
import cleanup
import sample
import sentance
import dictogram


#old code for Markov chain
# def marcov(text_list):
#     #creaete a tuple for word secquence
#     seq_list = list()
#     for key, value in enumerate(text_list):
#         print(key, value)
#         if key+1 < len(text_list):
#             key1 = (value, text_list[key+1])
#             seq_list.append(key1)
#         else:
#             break
#     #define marcov Dictionary
#     m_dict = dict()
#     # for each tuple in seq_list:
#     #     # Creae a dictogram for the second element in the tuple.
#     #     m_dict(tuple) = dictogram.Dictogram(text_list)
#     # #Create a dictogam for each tuple in the list to count the subsiqunt
#     # # Check to see if the tuple is a key in the dictionary
#
#     # for tuple in seq_list:
#     # #check if key is stored already
#     #     if tuple in m_dict:
#     #         m_dict[tuple].add_count([text_list[index + 1]])
#     #     else:
#     #         m_dict[tuple] = dictogram.Dictogram([text_list[index + 1]])
#     #         #if it is it should be added in our histogram
#     return m_dict

# first order Markov
# def markov_model(data):
#     markov_model = dict()
#     for i in range(0, len(data)-1):
#         if data[i] in markov_model:
#             # We have to just append to the existing histogram
#             markov_model[data[i]].update([data[i+1]])
#         else:
#             markov_model[data[i]] = dictogram.Dictogram([data[i+1]])
#     return markov_model

def order_mchain(order, text_list):
    markov_dict = {}
    # for each word in list, key is word and value is dictogram
    for index in range(len(text_list) - order):
        # text_list[index] should be our word from list
        window = tuple(text_list[index: index + order])
        print(window)
        # check if window is stored in the dictionary already
        if window in markov_dict:
            # if it is, then append it to the existing histogram
            markov_dict[window].add_count([text_list[index + order]])
        else:
            # if not, create new entry with window as key and dictogram as value
            markov_dict[window] = dictogram.Dictogram([text_list[index + order]])
    # return dictionary
    print(markov_dict)
    return markov_dict

#loop through a sentance: Key1 is first key in chain
def M_sentance(marcov, looper, first_key):
    looper = int(loop)
    sentance= []
    word_string = " "
    #appends first key to sentance
    sentance.append(first_key)
    # generate a random word using the sampler from marcov m_chain
    for i in range(0,looper):
        #pass referance last entry of sentance list into marcov chain
        key = marcov[(ln(sentace)-1)]
        #generate weighted sample based on marcov chain key and appends to sentance
        next_word = sample.weighted_random((marcov[key]),sample.sum_value(marcov[key]))
        sentance.append(next_word)
    # once list is geneated, turn it into a word_string
    word_string = word_string.join(word for word in sentance1)
    return word_string


if __name__ == '__main__':
    file1 = argv[1]  #file to analyze
    words = cleanup.text_list(file1)
    m_chain = order_mchain(2, words)
    print(m_chain)
    # key = m_chain[0]
    # sentace1 = M_sentance(m_chain, looper, )
