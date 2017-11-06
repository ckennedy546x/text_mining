#import wikipedia
import random
import string

#turtle = wikipedia.page("Turtle") #was used to acquire the original file which was then copy and pasted into the new "wikiwords.txt" file
# print(turtle.title)
# print(turtle.url)
# print(turtle.content)

def process_file(filename, skip_header):

    """Makes a histogram that contains the words from a file.



    filename: string

    skip_header: boolean, whether to skip the Gutenberg header



    returns: map from each word to the number of times it appears.

    """

    hist = {} #Creates a new, empty list

    fp = open(filename, encoding='utf8') #opens the specified file



    if skip_header: #calls upon skip_turtle_header function

        skip_turtle_header(fp)



    for line in fp: #for each line in the text

        if line.startswith('See also'): #won't read anything after this string

            break

        line = line.replace('-', ' ') #replace any -'s with a space

        strippables = string.punctuation + string.whitespace



        for word in line.split():

            # remove punctuation and convert to lowercase

            word = word.strip(strippables)

            word = word.lower()



            # update the histogram and adds the new word to the list hist

            hist[word] = hist.get(word, 0) + 1



    return hist #prints the new histogram





def skip_turtle_header(fp):

    """Reads from fp until it finds the line that ends the header.



    fp: open file object

    """

    for line in fp: #for each line in the opened document, it will continue until it sees this string

        if line.startswith('Turtles are reptiles of the order Testudines'):

            break

def total_words(hist):

    """Returns the total of the frequencies in a histogram."""

    return sum(hist.values()) #returns the sum of the amount of values that were created in hist list





def different_words(hist):

    """Returns the number of different words in a histogram."""

    return len(hist) #returns length of the hist list

def most_common(hist):

    """Makes a list of word-freq pairs(tuples) in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """

    t = [] # creates a new dictionary

    for key, value in hist.items():#for each word in the list hist

        t.append((value, key)) #will add the the word and how many times it appears to the dictionary 



    t.sort() #will put in descending order

    t.reverse() #reverses the way the dictionary shows words and frequncy

    return t # returns dictionary

def print_most_common(hist, num=30):

    """Prints the most commons words in a histgram and their frequencies.



    hist: histogram (map from word to frequency)

    num: number of words to print

    """

    t = most_common(hist)

    print('The most common words are:')

    for freq, word in t[:num]:#uses the last funtion but it puts it prints them instead of adding them to a dictionary

        print(word, '\t', freq)

def main():#prints all the results and calls upon the functions

    hist = process_file('C:\\wikiwords.txt', skip_header=True) #defines what the hist is

    print('Total number of words:', total_words(hist))

    print('Number of different words:', different_words(hist))

    print('Frequency of each word in descending order:', most_common(hist))

    print(print_most_common(hist))

if __name__ == '__main__':

    main()