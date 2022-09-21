# write a function that converts a string
# into an integer, but silly

# str_to_int
# takes a string
# converts it to a integer....somehow....
# returns the resulting integer, just the int

def str_to_int(original_string):
    ord_total = 0
    for character in original_string:
        ord_total = ord_total + ord(character)
    return ord_total

text = "cats"
# result = str_to_int(text)
# print(result)

import random

def add_word(original_string):
    words = ["unicorn", "zoom", "sleep"]
    selection = random.choice(words)
    return original_string + " " + selection

print(add_word("cats"))
