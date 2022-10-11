# infile = open('Three-years-in-europe.txt', 'r', encoding = 'utf-8')
# text = infile.read()
# print(infile.read())
# infile.close()

# print(text.split().count("the"))

infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')
lines = infile.readlines()
infile.close()
print(lines)
