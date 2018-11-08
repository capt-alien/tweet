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
    #takes a list argument and returns a word count
    dict = {}
    for word in words:
        if word not in (dict):
            dict[word] = 0
        dict[word] += 1
    return dict

## create a list of lists with counts
def list_words(words):
    #takes a list argument and returns a word count

    words_list = []
    for word in words:
        if word not in words_list:
            words_list.append([word, 0])
        for item in words_list:
            if item[0] == word:
                item[1] += 1
    print(words_list)
    return words_list

##Create a list of tuples
def tuple(words):
    #takes a list argument and returns a word count
    tuple_list = []
    for word in words:
        if (word, words.count(word)) not in tuple_list:
            tuple_list.append((word, words.count(word)))
    return tuple_list


#opens file_name
file1 = argv[1]
print_list = text_list(file1)
type = unique_list(print_list)
hist = dict_words(print_list)
wlist = list_words(print_list)
tlist = tuple(print_list)
print(print_list)
print(type)
print(hist)
print(wlist)
print(tlist)
