
def count_words(phrase):
    # count words
    words = phrase.split()
    results = len(words)
    return results

sen1 = "cats are critters"
sen2 = "so are dogs"
sen3 = "maybe crickets are, but who knows"

# print(count_words(sen1))
# print(count_words(sen2))
# print(count_words(sen3))

# index extraction
print(sen1[10])
print(sen2[10])
words_list = sen1.split()
print(words_list[2])

# slicing

print(words_list[0:2])
print(words_list[1:])

# (-inf,10), (10, inf]

# handy index shortcuts

# when you want the "first" of something
# use 0 in indexing!
print(words_list[0])
print("cats"[0])

# when you want the "last" of something!
print(words_list[-1])
print("cats"[-1])

# when you want the "last two" or someting...

print("banana crackers all over my car"[-2:])
print("banana crackers all over my car".split()[-2:])

