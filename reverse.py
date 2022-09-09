# Complete the function reverse_entries below that takes a dictionary and returns a new dictionary whose key-value pairs are the values and keys from the input.

# For example, if the input is this dictionary:

# {
#     "hair": "red",
#     "eyes": "blue",
# }
# then the output should be this dictionary:

# {
#     "red": "hair",
#     "blue": "eyes",
# }
# First, try solving this with a for loop.

# Then, once you have that figured out, read about list comprehensions and then try it with a dictionary comprehension. You have to look at the third example in the "Dictionaries" section to see an example of a dictionary comprehension.


def reverse_entries(dictionary):

    # reverse = {}

    # for key, value in dictionary.items():
    #     reverse[value] = key

    # return reverse

    return {value: key for key, value in dictionary.items()}


attributes = {
    "hair": "red",
    "eyes": "blue",
}

print(reverse_entries(attributes))
