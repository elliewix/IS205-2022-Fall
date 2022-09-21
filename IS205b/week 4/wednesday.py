letters_a = ['a', '', 'b', 'c', 'd','']
letters_b = ['w', '', 'x', 'y', '', 'z']
# assert the lengths match
assert len(letters_b) == len(letters_a), "diff lengths"

# print(list(zip(letters_a, letters_b)))
# for pair in zip(letters_a, letters_b):
#     print(pair)
#
# for i in range(len(letters_a)):
#     print(letters_a[i], letters_b[i])

letters_a = ['a', '', 'b', 'c', 'd','']
letters_b = ['w', '', 'x', 'y', '', 'z']

for pair in zip(letters_a, letters_b):
    letter_a, letter_b = pair
    print("A:", letter_a, "B:", letter_b)

for i in range(len(letters_a)):
    letter_a = letters_a[i]
    letter_b = letters_b[i]
    print(letter_a, letter_b)

new_headers = []

for pair in zip(letters_a, letters_b):
    letter_a, letter_b = pair
    a_blank = letter_a == ''
    b_blank = letter_b == ''
    print(letter_a, a_blank, letter_b, b_blank)
    if not b_blank:
        new_headers.append(letter_b)
