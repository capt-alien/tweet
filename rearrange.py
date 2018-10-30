#This rearanges random words on a listself.
import random

words = ["this", "is", "a", "random", "string" ]
new_words = []
list2 = words[::-1]
print(list2)

def U_input():
    next = True
    while next == True:
        input_a = str(input("What word would you like to add? "))
        words.append(input_a)
        input_b = input("Would you like to add another word? (y/n)")
        if input_b == "N" or input_b == "n":
            break


def rearragne(list1, list2):
    while len(list1) > 0:
        rand_index = (random.randint(0, (len(list1))-1))
        list2.append(list1[rand_index])
        list1.pop(rand_index)

def back(list1, list2):
    #easy way to do it:
    list2 = list1[::-1]
    return list2


    #This is the hard way to do it:
    # top_ind = len(list1)
    # while top_ind > 0:
    #     list2.append(list1[(top_ind-1)])
    #     top_ind -= 1


back(words, new_words)
print(words)
print(new_words)

# def rearange():
#     rand_index = random.randint(0, len(words) - 1)
#     return quotes[rand_index]
#
# U_input()
# print(words,)
# rearragne(words, new_words)
# print(new_words,)
