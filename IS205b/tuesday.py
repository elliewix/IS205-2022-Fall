# for character in "cats":
#     print(character)

# words = ['cats', 'dogs', 'mice']
# for w in words:
#     print(w)


phrase = "cats dogs spit"
print(phrase + "!")

base = "" # step 1, make your base
for w in ["cats", "dogs", "spit"]: # step 2, loop
    new_word = w + "! " # step 3, do your stuff
    # step 4, which variable?
    base = base + new_word # step 5, update base

print(base)


