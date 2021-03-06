import random
from typing import Union, List
from itertools import repeat, chain

from konlpy.tag import *

from koeda.utils import replace_space, revert_space


class RandomSwap:
    def __init__(self, morpheme_analyzer: str = None):
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

    def random_swap(
        self, data: Union[List[str], str], p: float = 0.1, repetition: int = 1
    ) -> Union[List[str], str]:
        if isinstance(data, str):
            if repetition <= 1:
                return self._swap(data, p)
            else:
                return list(
                    map(self._swap, repeat(data, repetition), repeat(p, repetition))
                )
        elif isinstance(data, list):
            if repetition <= 1:
                return list(map(self._swap, data, repeat(p, len(data))))
            else:
                return list(
                    map(
                        self._swap,
                        chain.from_iterable(repeat(x, repetition) for x in data),
                        repeat(p, len(data) * repetition),
                    )
                )
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

    def _swap_word(self, new_words: list) -> list:
        random_idx_1 = random.randint(0, len(new_words) - 1)
        random_idx_2 = random_idx_1
        counter = 0
        while random_idx_2 == random_idx_1:
            random_idx_2 = random.randint(0, len(new_words) - 1)
            counter += 1
            if counter > 3:
                return new_words
        new_words[random_idx_1], new_words[random_idx_2] = (
            new_words[random_idx_2],
            new_words[random_idx_1],
        )

        return new_words
