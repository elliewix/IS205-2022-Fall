def acronym(line_of_text):
    words = line_of_text.split()
    acr = ""
    for w in words:
        first_letter = w[0]
        acr = acr + first_letter
    return acr.upper()

# result = acronym("here are the cats")
# print(result)

infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')
lines = infile.readlines()
infile.close()

# print(acronym(lines)) # NOPE

# we need to loop

# loop and print
# for l in lines:
#     result = acronym(l)
#     print(result)


# now collect and write pattern

all_lines = ""
for l in lines:
    result = acronym(l)
    # print(result) # gives you free newlines
    all_lines = all_lines + result + "\n"

# print(all_lines)

# now that it's all together, we can write it out

outfile = open('3years_acronyms.txt', 'w', encoding= 'utf-8')
outfile.write(all_lines)
outfile.close()

# write out line by line pattern

outfile = open('3years_acronyms_linebyline.txt','w', encoding='utf-8')
for l in lines:
    result = acronym(l)
    # print(result)
    outfile.write(result + "\n")
outfile.close()


outfile = open('cats.txt', 'w', encoding='utf-8')
outfile.write("the cats are here")
outfile.close()


