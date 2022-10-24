import json

with open('test.json', 'r', encoding='utf-8') as jin:
    data = json.load(jin)

with open('prettytest.json', 'w', encoding='utf-8') as jout:
    json.dump(data, jout, indent = 4)
