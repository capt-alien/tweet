import random
import sys
# the following code has been borrowed from Faith

def random_word(histogram):
    # iterate over the histogram
    for word in histogram:
        # using random module to get a random items
        # used random.choice initially, but then changed to random.randint
        random_index = random.randrange(len(histogram))
    random_word = histogram[random_index]
    return random_word

def weighted_probablity(weighted_histogram):
    not_chosen = True
    while not_chosen:
        random_choice = random.choice(weighted_histogram)
        word = random_choice[0]
        probability = random_choice[1]
        random_number = random.uniform(0,1)
        if probability > random_number:
            return word
            not_chosen = False
        else:
            continue




if __name__ == '__main__':
    histogram = ["there", "once", "was", "a", "man", "from", "nantucket"]
    weighted_histogram = [["there", 0.1], ["once", 0.2], ["was", 0.1], ["a", 0.1], ["man", 0.1], ["from", 0.1], ["nantucket", 0.3]]
    # print("Your random histogram word is:\n{}".format(random_word(histogram)))
    loops = int(input("Enter number of words in new sentance: "))
    for _ in range(loops):
        print(weighted_probablity(weighted_histogram))
