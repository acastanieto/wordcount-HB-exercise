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
    """Creates a Counter collection of the words occuring in a text file."""

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


def sort_and_print(word_counts):
    sorted_tuples_by_count = word_counts.most_common() # one way
    # another way:
    # sorted_tuples_by_count = sorted(word_counts.items(), key=lambda pair: pair[1], reverse=True)
    for word, count in sorted_tuples_by_count:
        print word, count

    # sorted_wordcounts = sorted(word_counts.items(), key=lambda pair:pair[1], reverse=True)
    # for word, count in sorted_wordcounts:
    #     print word, count
    # for word, count in word_counts.iteritems():
    #     print word, count


sort_and_print(count_words(filename))

# http://stackoverflow.com/questions/20950650/how-to-sort-counter-by-value-python