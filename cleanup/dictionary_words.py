### this func

import random
from sys import argv


def load_words():
    """loads words from dictionary"""
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    split_words_list = words_list[0].split(' ')
    return split_words_list


def random_word(words_list):
    #picks random word
    secret_word = random.choice(words_list)
    return secret_word

if __name__ == '__main__':
    i = 0
    number = int(argv[1])
    loaded_words = load_words()
    # while i < number:
    #     print(random_word(loaded_words))
    #     i += 1
    for i in range(0, number):
        print(random_word(loaded_words))








# import random
# sentance = []
#
# # def load_word():
# # open word file
# f = open('words.txt', 'r')
# words_list = f.readlines()
# f.close() #Closes file
# words_list = words_list[0].split(' ')
# #turns file into a list.
#
# print(words_list)
#
# def build_sentance(words_list):
#     #Prompts user
#     num_words = int(input("How many words would you like this sentance to have? ")
# #build loop for sentance list
#     for i in range(0, num_words):
#         rand_index = (random.randint(0,ln(words_list))-1)
#         sentance.append(words_list[rand_index])
#
#
# build_sentance(words_list)
