import json

STOPWORDS_JSON_PATH = '../data/stopwords.json'


with open(STOPWORDS_JSON_PATH, 'r', encoding='utf-8') as f:
    STOPWORDS = json.load(f)

