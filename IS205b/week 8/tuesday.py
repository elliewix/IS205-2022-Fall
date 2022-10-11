infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')
text = infile.read()
infile.close()
# print(text.split().count("the"))

# for something in text:
#     print(something)
# infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')
# lines = infile.readlines()
# infile.close()
# print(lines)
#
# for something in lines:
#     print(something)

infile = open('Three-years-in-europe.txt','r', encoding='utf-8')
lines = infile.readlines()
infile.close()

for l in lines:
    # print(len(l.split()))
    # print(l)
    words = l.split()
    # print(words)
    if len(words) >0:
        print(words[0])
    # print(l.split()[0])
