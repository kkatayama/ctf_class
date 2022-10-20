# coding: utf-8
import yaml
import requests


url = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
with open('languages.yml', 'wb') as f:
    r = requests.get(url)
    f.write(r.content)

with open('languages.yml') as f:
    languages = yaml.full_load(f)
print(languages.keys())
