def count_words(phrase):
    # do stuff
    words_list = phrase.split()
    length = len(words_list)
    # return the count
    # return len(phrase.split())
    return length

sen1 = "cats are critters"
sen2 = "so are dogs"
sen3 = "but crickets are questionable"

# print(count_words(sen1))
# print(count_words(sen2))
# print(count_words(sen3))

###

# string indexing

print("cats"[0])

# list indexing
words = sen1.split()
print(words[0])

# string slicing

print("cats"[0:2])

# list slicing
print(words[0:2])

print(words[0])
print(words[0:2])

# negative index

print(words[0])
print(words[-1])
print(words[:2])
print("here's something longer"[:5])
print("here's something longer"[-3:])
