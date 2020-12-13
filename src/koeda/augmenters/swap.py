import random
from typing import Union

from src.koeda.utils import list_to_string


def random_swap(data: Union[list, str], p: float = 0.1) -> Union[list, str]:
    if isinstance(data, str):
        return _swap(data, p)
    elif isinstance(data, list):
        return list(map(_swap, data))
    else:
        raise Exception(f"Does not support the data type : {type(data)}")


def _swap(data: str, p: float = 0.1) -> str:
    words = data.split()

    n = max(1, int(len(words) * p))

    new_words = words.copy()
    for _ in range(n):
        new_words = swap_word(new_words)
    return list_to_string(new_words)


def swap_word(new_words):
    random_idx_1 = random.randint(0, len(new_words) - 1)
    random_idx_2 = random_idx_1
    counter = 0
    while random_idx_2 == random_idx_1:
        random_idx_2 = random.randint(0, len(new_words) - 1)
        counter += 1
        if counter > 3:
            return new_words
    new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1]
    return new_words
