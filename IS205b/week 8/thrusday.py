def acronym(line_of_text):
    words = line_of_text.split()
    # return words[0]
    acronym = ""
    for w in words:
        first_letter = w[0]
        acronym = acronym + first_letter
    return acronym.upper()

# results = acronym("here are the cats")
# print(results)

infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')
lines = infile.readlines()
infile.close()

# print(acronym(lines)) #NOOOOPE

# you need to loop

all_acronyms = ""
for l in lines:
    result = acronym(l)
    all_acronyms = all_acronyms + result + "\n"
    # print(result)

print(all_acronyms)

# get it ready and write it out at once
outfile = open('3yearsacronyms.txt', 'w', encoding = 'utf-8')
outfile.write(all_acronyms)
outfile.close()


# write out as we go
## goes inside my existing for loop processing the lines
outfile = open('3yearsacronyms-bylines.txt', 'w', encoding = 'utf-8')
for l in lines:
    result = acronym(l)
    outfile.write(result + '\n')

outfile.close()
