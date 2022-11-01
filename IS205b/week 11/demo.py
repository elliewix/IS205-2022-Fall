empty_d = {} # dict()

# populate by hand....

courses = {'IS205A': 'Wickes', 'IS205B': 'Wickes',
           'IS206A': 'Evans'}

# add (something new) by assignment

courses['IS305A'] = "Wickes"
print(courses)

# change a value for something already in there....
courses['IS205B'] = 'TBD'
print(courses)

# looping over dictionaries

for pair in courses.items():
    key_courseid = pair[0] #key = pair[0]
    value_prof = pair[1] #value = pair[1]
    print(key_courseid, value_prof)

# for the googlers...you may see this...
# for key, value in my_dict.items().....

# let's add some more data

courses['IS202A'] = 'Sanfillippo'
courses['IS202B'] = "Kendall"
courses['IS202C'] = "Darch"
courses['IS204'] = "Besser"

print(courses)
non_wickes = {}
for pair in courses.items():
    c = pair[0]
    p = pair[1]
    if p == "Wickes":
        print(c, p)
    else:
        non_wickes[c] = p

print(non_wickes)

# we know that....
print(courses['IS205A'])
course = 'IS205A'
print(courses[course])

# say we have a list of keys....

ids = ["IS205A", "IS202B"]

my_course = ids[1]
print(courses[my_course])
print(courses[ids[1]])

# we know all this syntax works, so we can put it together
# loop over keys printing them out...
# ids = ["IS205A", "IS202B"]
for courseid in ids:
    print(courseid, courses[courseid])

# think less of it like a database, and more likje a collection of counters

## count letters in a phase

phrase = "five nights at freddies"

letter_counts = {}

for letter in phrase:
    if letter in letter_counts: # use in to check if content is a key
        letter_counts[letter] = letter_counts[letter] + 1
        # you may also see this: letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)

# count the number of times each value appears in another dict

prof_counts = {}
for pair in courses.items():
    key_courseid = pair[0]
    value_prof = pair[1]
    if value_prof in prof_counts:
        prof_counts[value_prof] = prof_counts[value_prof] + 1
    else:
        prof_counts[value_prof] = 1
print(prof_counts)
