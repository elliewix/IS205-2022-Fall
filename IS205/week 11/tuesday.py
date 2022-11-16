empty_d = {} # dict()

# add it in by hand....
stuff = {'IS205A': "Wickes", "IS205B": "Wickes", "IS206A": "Evans"}

# add a value
stuff['IS305A'] = "Wickes"
print(stuff)

# change a value
stuff['IS205B'] = "TBD"
print(stuff)

# get a value out, lookup by key
print(stuff['IS206A'])

# looping over dictionaries
# there are many ways but this one is one the best for a starter

for pair in stuff.items():
    # print(pair)
    # key = pair[0]
    # value = pair[1]
    courseid = pair[0]
    prof = pair[1]
    print(courseid, prof)

# you may also see it like this

# for key, value in stuff.items():
#     print(key, value)


# a list of stuff that happen to be keys.....
# loop over em and get the values
classes = ['IS205A', 'IS206A']

# we know we can do this....
print(stuff['IS205A'])
# so then this must work....
c = classes[0] # class_list
# vs stuff_dict or classes_dict
print(stuff[c])
# so then this must also work...
print(stuff[classes[0]])

# and putting it all together.....
## loop over a list....that contains my keys I want....
for c in classes:
    print("class", c, "taught by", stuff[c])

## lets loop over our stuff dict

stuff['IS204'] = "Besser"
stuff['IS203'] = "Batzloff"
stuff['IS202'] = "Sanfillipo"

# let's find all the classes that Wickes teaches
# dict accumulator pattern
non_wickes = {}
for pair in stuff.items():
    courseid = pair[0]
    prof = pair[1]
    if prof == 'Wickes':
        print(pair)
    else:
        non_wickes[courseid] = prof

print(non_wickes)


# count the letters in a string
name = "five nights at freddies"

letter_counts = {}

for letter in name: # loop over the content to count
    # check if the letter is already counted
    if letter in letter_counts: # in checks for memebership of keys
        letter_counts[letter] = letter_counts[letter] + 1
        # you can alt do
        # letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1 # becasue I'm loooking at one, it's 1

print(letter_counts)

# count how many courses each prof teaches?

class_counts = {}
for pair in stuff.items():
    course = pair[0]
    prof = pair[1]
    if prof in class_counts:
        class_counts[prof] = class_counts[prof] + 1
    else:
        class_counts[prof] = 1

print(class_counts)


