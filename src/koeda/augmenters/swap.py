import random
from typing import Union
from itertools import repeat

from src.koeda.utils import replace_space, revert_space
from konlpy.tag import *


class RandomSwap:

    def __init__(self, morpheme_analyzer=None):
        if morpheme_analyzer is None:
            self.morpheme_analyzer = Okt()
        elif morpheme_analyzer in ["Okt", "Kkma", "Komoran", "Mecab", "Hannanum"]:
            self.morpheme_analyzer = eval(morpheme_analyzer)()
        elif hasattr(morpheme_analyzer, "morphs"):
            self.morpheme_analyzer = morpheme_analyzer
        else:
            raise Exception("Does not support morpheme analyzer.")

    def __call__(self, *args, **kwargs):
        return self.random_swap(*args, **kwargs)

    def random_swap(self, data: Union[list, str], p: float = 0.1) -> Union[list, str]:
        if isinstance(data, str):
            return self._swap(data, p)
        elif isinstance(data, list):
            return list(map(self._swap, data, repeat(p, len(data))))
        else:
            raise Exception(f"Does not support the data type : {type(data)}")

    def _swap(self, data: str, p: float = 0.1) -> str:
        split_words = self.morpheme_analyzer.morphs(replace_space(data))
        words = self.morpheme_analyzer.morphs(data)

        n = max(1, int(len(words) * p))

        new_words = split_words.copy()
        for _ in range(n):
            new_words = self._swap_word(new_words)

        return revert_space(new_words)

    def _swap_word(self, new_words):
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
