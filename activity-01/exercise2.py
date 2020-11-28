# Solution 1
# import os

# file_dir = os.path.dirname(__file__)
# file_reader = open(os.path.join(file_dir, "text.txt"))

# text = file_reader.read().lower()

# current_word = 0
# longest_word = []

# words = text.split()

# for word in words:
#     if len(word) > current_word:
#         current_word = len(word)
#         longest_word = [word, len(word)]

# print(longest_word)


# Solution 2
import os

file_dir = os.path.dirname(__file__)
file_reader = open(os.path.join(file_dir, "text.txt"))

text = file_reader.read().lower()

longest_word = ["", 0]
words = text.split()

for word in words:
    len_current_word = len(word)

    if len_current_word > longest_word[1]:
        longest_word = [word, len_current_word]

print(longest_word)