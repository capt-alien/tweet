from sys import argv
import re
import random


##open text file and turn it into a usable words_list
def text_list(file_name):
    #Opens file
    raw_words = open(file_name, 'r').read()
    # take all titles outer (Getting errors need help)
    no_titles = re.sub(r"(X?|X{0,3})(CM|CD|D?C{0,3})(IX|IV|V?I{0,3})\.(\s\w+){1,7}", " ", raw_words).lower()
    #turn all periods into start/stop tokens
    w_ss_tokens = re.sub(r"\." , " STOP START ", no_titles)
    #take out punctuation
    wo_punctuation = re.sub(r"\W", " " , w_ss_tokens)
    # splilts the string into a list
    word_pasta = wo_punctuation.split()
    return word_pasta
    # return pasta

# to spead up this process, we could get the resulting word list to write to a file. 

#streatch go through a list and puncuate the first letter of the next
# word after the start token and end with a period after the stop token

if __name__ == '__main__':
    file1 = argv[1]
    print(text_list(file1))
