import os
import json

STOPWORDS_JSON_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir, "corpora/stopwords.json"
)

with open(STOPWORDS_JSON_PATH, "r", encoding="utf-8") as f:
    STOPWORD = json.load(f)["stopwords"]
