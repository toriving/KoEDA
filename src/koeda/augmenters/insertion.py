import random
from typing import Union

from src.koeda.utils import get_synonyms, list_to_string


def random_insertion(data: Union[list, str], p: float = 0.1) -> Union[list, str]:
    if isinstance(data, str):
        return _insertion(data, p)
    elif isinstance(data, list):
        return list(map(_insertion, data))
    else:
        raise Exception(f"Does not support the data type : {type(data)}")


def _insertion(data: str, p: float = 0.1) -> str:
    words = data.split()

    n = max(1, int(len(words) * p))

    new_words = words.copy()
    for _ in range(n):
        add_word(new_words)
    return list_to_string(new_words)


def add_word(new_words):
    synonyms = []
    counter = 0
    while len(synonyms) < 1:
        random_word = new_words[random.randint(0, len(new_words) - 1)]
        synonyms = get_synonyms(random_word)
        counter += 1
        if counter >= 10:
            return
    random_synonym = synonyms[0]
    random_idx = random.randint(0, len(new_words) - 1)
    new_words.insert(random_idx, random_synonym)





