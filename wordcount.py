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

    words_by_count_key = {}

    for word, count in sorted_tuples_by_count:
        if count not in words_by_count_key:
            words_by_count_key[count] = [word]
        else:
            words_by_count_key[count].append(word)

    sorted_by_count = words_by_count_key.items()
    sorted_by_count.sort(reverse=True)

    for count, list_of_words in sorted_by_count:
        list_of_words.sort()
        for i in range(len(list_of_words)):
            print count, list_of_words[i]

    # another way without unpacking (if didn't need to change list):    
    #for pair in sorted_tuples_by_count:
    #   print "%s %d" % (pair)

sort_and_print(count_words(filename))

# http://stackoverflow.com/questions/20950650/how-to-sort-counter-by-value-python