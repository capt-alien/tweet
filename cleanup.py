# proceses textfile into a list

from sys import argv
import re
import random


##open text file and turn it into a usable words_list
def text_list(file_name):
    #Opens file
    raw_words = open(file_name, 'r').read().lower().split()
#should be able to filter out punctuations and special charictors.
    return raw_words


if __name__ == '__main__':
    file1 = argv[1]
    print(text_list(file1))
