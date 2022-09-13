# Complete the function horizontal_bar_chart below that takes in a string and creates a horizontal bar chart made out of the instances of the letters in that string based on the number of each letter.

# The return value is a list of the strings of the letters in alphabetical order.

# For example, given the sentence "abba has a banana", it would return this list of strings because there are seven "a", three "b", one "h", two "n", and one "s" letters in it:

# [
#   "aaaaaaa",
#   "bbb",
#   "h",
#   "nn",
#   "s",
#
# All letters in the input will be lowercase letters.

# You may want to look at the methods for dictionaries and the built-in functions. Remember, you can also compare strings with >= and <=.

def horizontal_bar_chart(sentence):

    # chart = []
    # dict = {}

    # for i in sentence:

    #     i = i.lower()

    #     if i not in dict and i.isalpha():
    #         dict[i] = 1
    #     elif i.isalpha():
    #         dict[i] += 1

    # for i in dict:
    #     chart.append(i * dict[i])

    # return sorted(chart)

    # return sorted(list(set([i * sentence.count(i) for i in sentence if i.isalpha()])))

    return sorted(list({i.lower() * sentence.count(i) for i in sentence if i.isalpha()}))

    # letter_bucket = {}

    # for char in sentence:
    #     char = char.lower()
    #     if char >= "a" and char <= "z":
    #         if letter_bucket.get(char):
    #             letter_bucket[char] += char
    #         else:
    #             letter_bucket[char] = char

    # bar_chart = letter_bucket.values()

    # return sorted(bar_chart)


print(horizontal_bar_chart("ABBA has a banANA"))
