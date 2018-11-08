from sys import argv
import random


##open text file and turn it into a usable words_list
def text_list(file_name):
    split_words_list = open(file_name, 'r').read().split()
    return split_words_list

##Create a list of unique words

def unique_list(words):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    # return unique words lists
    return unique_words


## Create a dictionary with counts
def dict_words(words):
    dict = {}
    for word in words:
        if word not in (dict):
            dict[word] = 0
        dict[word] += 1
    return dict

## create a list of lists with counts

##Create a list of tuples

##create

#tests

#opens file_name
file1 = argv[1]
print_list = text_list(file1)
type = unique_list(print_list)
hist = dict_words(print_list)
print(print_list)
print(type)
print(hist)
