##Code borrows from Dylan Flyn's code. I made improvments

from sys import argv
import re
import random


##open text file and turn it into a usable words_list
def text_list(file_name):
    #Opens file
    raw_words = open(file_name, 'r').read().lower().split()
#should be able to filter out punctuations and special charictors.
    return raw_words

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

#sums dictionary in histo
def sum_value(histogram):
    total = (sum(histogram.values()))
    return total

def write_file(object, type):
    fname = input("Please enter name for file: ")
    with open(fname, "w") as file:
        file.write(type)
        file.write(str(object))
        file.close()


#opens file_name

if __name__ == '__main__':
    file1 = argv[1]
    print_list = text_list(file1)
    #promts user for method
    print("==================================")
    print("Welcome to Hist-o-grama-rama!!!!!")
    print("=======>INSTRUCTIONS<============")
    print("Press 1 for a Dictionary")
    print("Press 2 for a List of Lists")
    print("Press 3 for a Tuple")
    input1 = input("Which method would you like returned? ")
    #dictionary
    if input1 == "1":
        dict_list = dict_words(print_list)
        tots = sum_value(dict_list)
        print(dict_list)
        print(tots)
        #saves result to text file
        answer1 = input("Would you like to save to a file? y/n").lower()
        if answer1 == "y":
            write_file(dict_list, "Dictionary")


    #list of list
    elif input1 == "2":
        wlist = list_words(print_list)
        print(wlist)
        answer2 = input("Would you like to save to a file? y/n").lower()
        if answer2 == "y":
            write_file(wlist, "List of lists")

    #Tuple
    elif input1 == "3":
        tlist = tuple(print_list)
        print(tlist)
        answer3 = input("Would you like to save to a file? y/n").lower()
        if answer3 == "y":
            write_file(tlist, "Tuple")


    else:
        print("Incorect input, Please try again!")
