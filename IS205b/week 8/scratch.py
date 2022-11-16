with open('posters.txt', 'r') as fin:
    votes = fin.readlines()

from collections import Counter

for title, count in Counter(votes).most_common(10):
    print(title, count)

