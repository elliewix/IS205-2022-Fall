# write a function that converts a string
# to an integer

# str_to_int
# input is a string
# do the thing?...... however that is....?
# output is an integer, the result

def print_cats(some_word):
    return some_word + " are maybe a cat"

results = print_cats("cats")
# print(results)

def str_to_int(original_string):
    ord_total = 0
    for character in original_string:
        ord_total = ord_total + ord(character)
    return ord_total
text = "cats"
result = str_to_int(text)
# print(result)
# print(str_to_int("cats"))

print(chr(str_to_int("hell")))
