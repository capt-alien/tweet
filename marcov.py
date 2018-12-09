from sys import argv
import cleanup
import sample
import sentance
import dictogram


#build a map for marcov chain
def marcov(text_list):
    #define marcov Dictionary
    m_dictionary = dict()
    #create for value in variable:
    # pass loop for each word, the word is the key and value is a histogram
    for index in range(len(text_list) - 1):
        word = text_list[index]
        # check if key is stored already
        if word in m_dictionary:
            m_dictionary[word].add_count([text_list[index + 1]])
        else:
            m_dictionary[word] = dictogram.Dictogram([text_list[index + 1]])
            #if it is it should be added in our histogram
        return m_dictionary


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
    print(words)
    m_chain = marcov(words)
    print(m_chain)
    key = m_chain[0]
    sentace1 = M_sentance(m_chain, looper, )
