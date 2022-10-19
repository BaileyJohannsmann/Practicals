"""
CP1404 - Practical 5
wimbledon
a program to count the occurrences of words in a string
"""

words = input("String: ").split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

word_max_length = max([len(word) for word in word_count])
for word, count in sorted(word_count.items()):
    print(f"{word:{word_max_length}} : {count}")
