text = "here are the cats"

# print(text[6])
# text[6] = "x" # nope can't do this

numbers = [1, 0, 8, 6, 9, 10, 23, -3, 5]

# sorted is a returner, so we need assignment
# numbers = sorted(numbers)
# print(numbers)

numbers = [1, 0, 8, 6, 9, 10, 23, -3, 5]
# sort method is a mutator!
# numbers.sort()
# print(numbers)

import random

# numbers = [1, 0, 8, 6, 9, 10, 23, -3, 5]
numbers = list(range(10))
# print(numbers)
sorted_numbers = numbers.copy()
random.shuffle(sorted_numbers)
# print(numbers)
# print(sorted_numbers)
# my_list = ['a', 'b', 'c', 'd']
# my_list.append('e')
# my_list.append('e')
# my_list.append('e')
# my_list.append('e')
# my_list.count('e')
# 4
# my_list.count('a')
# 1
# sorted(my_list)
# ['a', 'b', 'c', 'd', 'e', 'e', 'e', 'e']
# my_list.reverse()
# my_list
# ['e', 'e', 'e', 'e', 'd', 'c', 'b', 'a']
# sorted(my_list)
# ['a', 'b', 'c', 'd', 'e', 'e', 'e', 'e']

## list accumulator pattern

numbers = list(range(20))

evens = [] # list()
odds = []

for num in numbers:
    # print(num, num % 2)
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print(num, evens, odds)
