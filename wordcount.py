# # put your code here.
# 1. open file "test.txt", assign contents to a string using file.read()
# 2. split at " ", get a list of all words
# 3. loop through list, create a key for each word and a value of 1
# 4. each time a word appears update its value by 1
# 5. end up with dictionary of format word: count, print results

def count_words(filename):
    text_file = open(filename)
    text = text_file.read()
    text = text.rstrip().replace("\n", " ")
    word_list = text.split(" ")

    word_counts = {}
    for word in word_list:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    return word_counts


def print_wordcount(word_counts):
    for word, count in word_counts.iteritems():
        print word, count

print_wordcount(count_words("test.txt"))