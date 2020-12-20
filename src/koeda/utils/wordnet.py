import os
import json

WORDNET_JSON_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir, "corpora/wordnet.json"
)

with open(WORDNET_JSON_PATH, "r", encoding="utf-8") as f:
    WORDNET = json.load(f)
