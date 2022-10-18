# text = "here's a cat"
#
# print(text[7])
# text[7] = "x"

import random

numbers = random.choices(range(10), k = 20)
# print(list(numbers))
numbers = sorted(numbers) # assignment required
# print(numbers)

numbers = list(range(20))
# print(numbers)
# numbers = random.shuffle(numbers) # nope! it's a mutator
random.shuffle( numbers) # correct! b/c it's a a mutator
# print("shuffle",numbers)
numbers.sort()
# print(".sort", numbers)


## list accumulator pattern

evens = [] # list() is the same
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
    print(num, evens, odds)

