# """
# This is the Template Repl for Python with Turtle.
#
# Python with Turtle lets you make graphics easily in Python.
#
# Check out the official docs here: https://docs.python.org/3/library/turtle.html
# """
#
# import turtle
#
# t = turtle.Turtle()
# t.speed(1)
# # for i in range(4):
# #   t.forward(50)
# #   t.left(90)
#
# # t.clear()
#
# # for i in range(3):
# #   t.forward(50)
# #   t.left(120)
#
# t.clear()
#
#
# # sides = 20
#
# # for i in range(sides):
# #   t.forward(50)
# #   t.left(360/sides)
#
# for letter in "cats":
#   t.forward(50)
#   t.left(360 / len("cats"))

# loop over a string


# for character in "dogs":
#     print(character)

old_colors = ['purple', 'teal', 'snot']
my_colors = ["red", "blue", "green"] + old_colors
# print(my_colors)
# for word in my_colors:
#     print(word)
    # for character in word:
    #     print(word, character)

phrase = "dogs and cats"
print(phrase + "!")

words = ["dogs", "and", "cats"]

base = "" # step 1, make base
for w in words: # step 2, loop
    new_word = w + "! " # step 3, do your business
    # step 4, identify the thing you want to save
    base = base + new_word # step 5, update your base

print(base)

