import sys
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

lexicon = {}

def loadLexicon(file):
    for line in file:
        count, word  = line.split()
        lexicon[word] = int(count)


if __name__ == "__main__":
    print("foo")
    loadLexicon(open(sys.argv[1]))
    freqs = plt.bar(range(len(lexicon.keys())), sorted(lexicon.values(), reverse=True))
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Word frequency plot')
    plt.savefig(sys.stdout.buffer)
#    plt.show()
