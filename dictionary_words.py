import random
from sys import argv
i = 0
uhh = int(argv[1])
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    split_words_list = words_list[0].split(' ')
    secret_word = random.choice(split_words_list)
    return secret_word

while i < uhh:
    print(load_word(),)
    i += 1






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
