##Code based on Dylan Flyn's code. I made some improvments

from sys import argv
import random


##open text file and turn it into a usable words_list
def text_list(file_name):
    split_words_list = open(file_name, 'r').read().lower().split()
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
    unique_words = unique_list(words)
    for word in unique_words:
        #adds unique value to words list
            words_list.append([word, words.count(word)])
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

if __name__ == '__main__':
    file1 = argv[1]
    print_list = text_list(file1)
    #promts user for method
    print("1 for a Dictionary")
    print("2 for a List of Lists")
    print("3 for a Tuple")
    input1 = input("Which method would you like returned? ")
    #dictionary
    if input1 == "1":
        dict_list = dict_words(print_list)
        print(dict_list)
    #list of list
    elif input1 == "2":
        wlist = list_words(print_list)
        print(wlist)
    #Tuple
    elif input1 == "3":
        tlist = tuple(print_list)
        print(tlist)
    else:
        print("Incorect input, Please try again!")
