import random
from typing import Union

from src.koeda.utils import list_to_string


def random_deletion(data: Union[list, str], p: float = 0.1) -> Union[list, str]:
    if isinstance(data, str):
        return _deletion(data, p)
    elif isinstance(data, list):
        return list(map(_deletion, data))
    else:
        raise Exception(f"Does not support the data type : {type(data)}")


def _deletion(data: str, p: float = 0.1) -> str:
    words = data.split()
    # obviously, if there's only one word, don't delete it
    if len(words) == 1:
        return list_to_string(words)

    # randomly delete words with probability p
    new_words = []
    for word in words:
        r = random.uniform(0, 1)
        if r > p:
            new_words.append(word)

    # if you end up deleting all words, just return a random word
    if len(new_words) == 0:
        rand_int = random.randint(0, len(words) - 1)
        return list_to_string([data[rand_int]])

    return list_to_string(new_words)
