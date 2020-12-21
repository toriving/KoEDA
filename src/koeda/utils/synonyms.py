from koeda.utils import WORDNET


def get_synonyms(word):
    synonyms = set()
    synsets = WORDNET["lemmas"].get(word, None)

    if synsets is None:
        return []

    for syn in synsets:
        synonym = WORDNET["synsets"][syn]["lemmas"]
        synonyms.update(synonym)

    if word in synonyms:
        synonyms.remove(word)

    return list(synonyms)
