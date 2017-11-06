#import wikipedia
import random
import string

#turtle = wikipedia.page("Turtle")
# print(turtle.title)
# print(turtle.url)
# print(turtle.content)

def process_file(filename, skip_header):

    """Makes a histogram that contains the words from a file.



    filename: string

    skip_header: boolean, whether to skip the Gutenberg header



    returns: map from each word to the number of times it appears.

    """

    hist = {}

    fp = open(filename, encoding='utf8')



    if skip_header:

        skip_gutenberg_header(fp)



    for line in fp:

        if line.startswith('See also'):

            break

        line = line.replace('-', ' ')

        strippables = string.punctuation + string.whitespace



        for word in line.split():

            # remove punctuation and convert to lowercase

            word = word.strip(strippables)

            word = word.lower()



            # update the histogram

            hist[word] = hist.get(word, 0) + 1



    return hist





def skip_gutenberg_header(fp):

    """Reads from fp until it finds the line that ends the header.



    fp: open file object

    """

    for line in fp:

        if line.startswith('Turtles are reptiles of the order Testudines'):

            break

def total_words(hist):

    """Returns the total of the frequencies in a histogram."""

    return sum(hist.values())





def different_words(hist):

    """Returns the number of different words in a histogram."""

    return len(hist)

def most_common(hist):

    """Makes a list of word-freq pairs(tuples) in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """

    t = []

    for key, value in hist.items():

        t.append((value, key))



    t.sort()

    t.reverse()

    return t

def print_most_common(hist, num=30):

    """Prints the most commons words in a histgram and their frequencies.



    hist: histogram (map from word to frequency)

    num: number of words to print

    """

    t = most_common(hist)

    print('The most common words are:')

    for freq, word in t[:num]:

        print(word, '\t', freq)

def main():

    hist = process_file('C:\\wikiwords.txt', skip_header=True)

    print('Total number of words:', total_words(hist))

    print('Number of different words:', different_words(hist))

    print('Frequency of each word in descending order:', most_common(hist))

    print(print_most_common(hist))

if __name__ == '__main__':

    main()