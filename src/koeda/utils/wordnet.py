import json

WORDNET_JSON_PATH = '../data/wordnet.json'


with open(WORDNET_JSON_PATH, 'r', encoding='utf-8') as f:
    WORDNET = json.load(f)