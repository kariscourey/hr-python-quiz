# Complete the function make_description below, which takes a person's name and a dictionary of their attributes and constructs a single string from them.

# For example, say the person's name is "Lulu" and their attribute dictionary contained the following entries:

# {
#     "hair": "red",
#     "eyes": "blue",
# }
# Then, the return value of the function should be the string:

# Lulu, red hair, blue eyes
# If the dictionary has no entries, then the return value should just be the person's name.

def make_description(name, attributes):

    statement = name

    for key, value in attributes.items():
        # statement += ", " + value + " " + key
        statement += f", {value} {key}"


    return statement

name = "Lulu"
attributes = {
    "hair": "red",
    "eyes": "blue",
}


print(make_description(name,attributes))
