terms = ['cat', 'london', 'boat', 'dog']

data = {}

for term in terms:
    data[term] = {'count': 0, 'lines': []}

current = 'boat'
# data[current]['count'] += 1
data[current]['count'] = data[current]['count'] + 1
data[current]['lines'].append('hello there I am a boat')

for pair in data.items():
    print(pair)
