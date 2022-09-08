# Your friends and you have gone out to dinner and all ordered the same foods. Now, it's time to split the bill.

# Complete the function below to take the total of the bill, figure out the tip, and divide that combined total by the number of diners. Return the final calculation.

# For example, if the bill is $20 and the tip is 20% (0.2), then the bill plus the tip is $20 + $4 for $24. If there were two of you, the return value of the function is 12 (24/2).

def divide_bill(bill, num_diners, tip=0.2):
    return bill * (1 + tip) / num_diners


# Complete the following function to find the longest string in the list of strings passed to it.

# If the list of strings passed to it is empty, return None.

# There will always be a longest string. No two strings in the list will have the same length.

def find_longest(strings):

    # if strings:

    #     longest = ""

    #     for i in strings:
    #         if len(i) > len(longest):
    #             longest = i

    #     return longest

    if strings:
        return max(strings, key=len)
        # used built-in len function

    # longest = None
    # for s in strings:
    #     if longest is None:
    #         longest = s
    #     elif len(s) > len(longest):
    #         longest = s
    #     return longest

# Write a function called "check_age".

# Given a person's name and age, "check_age" returns one of two messages:

# Go home, <insert_name_here>!, if they're younger than 21.
# Welcome, <insert_name_here>!, if they're 21 or older.
# Naturally, replace <insert_name_here> with the given name.

# output = check_age('Adrian', 22)
# print(output) # --> 'Welcome, Adrian!'

def check_age(name, age):

        if age < 21:
            return "Go home, " + name + "!"
            # return f"Welcome, {name}!"
        return "Welcome, " + name + "!"

# Write a function called is_key_in() .

# Given an object and a key, is_key_in() returns True if the key is in the dictionary. Otherwise, it returns False.

# dictionary = {'name':'Sam', 'age': 20}
# answer = is_key_in(dictionary, 'name')

# print(answer)  # Prints true

def is_key_in(dictionary, key):

   return key in dictionary


print(check_age("Adrian", 22))
print(check_age("Nairda", 12))
print(find_longest(["blue", "red", "orange"]))
