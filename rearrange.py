#This rearanges random words on a listself.
import random

words = ["this", "is", "a", "random", "string" ]
new_words = []



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



# def rearange():
#     rand_index = random.randint(0, len(words) - 1)
#     return quotes[rand_index]
#
U_input()
print(words,)
rearragne(words, new_words)
print(new_words,)
