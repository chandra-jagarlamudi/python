#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

"""
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.
"""


def print_words(filename):
    words_dict = get_words_from_file(filename)

    for k, v in words_dict.items():
        print(k, ' : ', v)

    # for key in words_dict:
    # print(key + " : " + str(words_dict[key]))


"""
2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.
"""


def print_top(filename):
    words_dict = get_words_from_file(filename)

    for k, v in sorted(words_dict.items(), reverse=True, key=lambda item: item[1]):
        print(k, " : ", v)


def get_words_from_file(filename):
    words_list = []
    words_dict = {}

    # Read each line from the file and close the file
    f = open(filename, 'r')
    lines_in_file = f.read().splitlines()
    f.close()

    # split each line and add words to list
    for line in lines_in_file:
        words_list.extend(line.split(" "))

    # convert words to lowercase and sort
    sorted_word_list = sorted([word.lower() for word in words_list if len(word) >= 2], key=str)
    # print(sorted_word_list)

    # add to dict and get count
    for w in sorted_word_list:
        if w in words_dict:
            words_dict[w] = words_dict.get(w) + 1
        else:
            words_dict[w] = 1

    return words_dict


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
