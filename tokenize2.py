# Creates a list of unique values
from sys import argv
import cleanup


def unique_list(words):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    # return unique words lists
    return unique_words

if __name__ == '__main__':
    file1 = argv[1]
    list = unique_list(cleanup.text_list(file1))
    print(list)
