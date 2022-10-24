import requests
import time
import json
import pathlib

html = "https://api.elsevier.com/content/search/scopus?query=all(%22big%20bang%22)&apiKey=7f59af901d2d86f78a1fd60c1bf9426a"


r = requests.get(html)

# print(json.dumps(r.text))

p = pathlib.Path('out.json')

with open(p, 'w', encoding='utf-8') as jout:
    json.dump( json.loads(r.text), jout, indent=4)

