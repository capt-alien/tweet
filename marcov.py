from sys import argv
import cleanup
import sample
import sentance
import Dictogram


#build a map for marcov chain
def marcov(text_list):
    #define marcov Dictionary
    m_dictionary = dict()
    #create for value in variable:
    pass looop for each word, the word is the key and value is a histogram
    for word in text_list:
        word = text_list[index]
        # check if key is stored already
        if word in m_dictionary:
            m_dictionary[word].add_count([text_list[index + 1]])
        else:
            m_dictionary[word] = Dictogram([text_list[index = 1]])
            #if it is it should be added in our histogram
        return marcov_dict


#loop through a sentance:
# def M_sentance(text_list):


if
