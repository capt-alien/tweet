
from collections import Counter
import sys

def histogram(string):
    words1 = string.lower()
    words = words1.split()
    count = Counter()
    for word in words:
        count[word] += 1
    return count


if __name__ == '__main__'
    filename = sys.argv[1]
    words = open(sys.argv[1], "r").read()
    hist = histogram(words)
    print(hist)



#check out set fuunction in python
