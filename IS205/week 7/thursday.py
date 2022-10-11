# loop over a string, you get characters

for character in "banana crackers":
    print(character)

def dostuff(word, repeat):
    return word * repeat

print(dostuff("cat", 3))
print(dostuff("dog", 2))

print([3])
print("bananas"[3])
print(['cat', 'dog', 'snake', 'kid'][3])

print("bananas"[:2])
print(['cat', 'dog', 'snake', 'kid'][:2])

# print("bananas"[-6:5])
print("bananas"[::-1])
