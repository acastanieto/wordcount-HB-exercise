# # put your code here.
# 1. open file "test.txt", assign contents to a string using file.read()
# 2. split at " ", get a list of all words
# 3. loop through list, create a key for each word and a value of 1
# 4. each time a word appears update its value by 1
# 5. end up with dictionary of format word: count, print results

from sys import argv
from collections import Counter

script, filename = argv

def count_words(filename):
    text_file = open(filename)
    text = text_file.read()
    text = text.rstrip().lower().replace("\n", " ")
    no_punct = ""
    for char in text:
        if char.isalpha() or char == " ":
            no_punct += char
    word_list = no_punct.split(" ")

    word_counts = Counter(word_list)

    return word_counts


def print_wordcount(word_counts):
    for word, count in word_counts.iteritems():
        print word, count

print_wordcount(count_words(filename))