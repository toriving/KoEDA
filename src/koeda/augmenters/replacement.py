import random
from typing import Union

from src.koeda.utils import STOPWORDS, get_synonyms, list_to_string


def synonym_replacement(data: Union[list, str], p: float = 0.1) -> Union[list, str]:
    if isinstance(data, str):
        return _replacement(data, p)
    elif isinstance(data, list):
        return list(map(_replacement, data))
    else:
        raise Exception(f"Does not support the data type : {type(data)}")


def _replacement(data: str, p: float = 0.1) -> str:
    words = data.split()

    n = max(1, int(len(words) * p))

    new_words = words.copy()
    random_word_list = list(set([word for word in words if word not in STOPWORDS]))
    random.shuffle(random_word_list)
    num_replaced = 0
    for random_word in random_word_list:
        synonyms = get_synonyms(random_word)
        if len(synonyms) >= 1:
            synonym = random.choice(list(synonyms))
            new_words = [synonym if word == random_word else word for word in new_words]
            num_replaced += 1
        if num_replaced >= n:  # only replace up to n words
            break

    return list_to_string(new_words)
