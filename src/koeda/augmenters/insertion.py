import random
from typing import Union, List
from itertools import repeat, chain

from konlpy.tag import *

from ..utils import replace_space, revert_space, get_synonyms, STOPWORD, SPACE_TOKEN


class RandomInsertion:
    def __init__(self, morpheme_analyzer: str = None, stopword: bool = False):
        self.stopword = stopword

        if morpheme_analyzer is None:
            self.morpheme_analyzer = Okt()
        elif morpheme_analyzer in ["Okt", "Kkma", "Komoran", "Mecab", "Hannanum"]:
            self.morpheme_analyzer = eval(morpheme_analyzer)()
        elif hasattr(morpheme_analyzer, "morphs"):
            self.morpheme_analyzer = morpheme_analyzer
        else:
            raise ValueError(f'Does not support {morpheme_analyzer} morpheme analyzer. '
                             f'Choose one of ["Okt", "Kkma", "Komoran", "Mecab", "Hannanum"]')

    def __call__(self, *args, **kwargs):
        return self.random_insertion(*args, **kwargs)

    def random_insertion(
        self, data: Union[List[str], str], p: float = 0.1, repetition: int = 1
    ) -> Union[List[str], str]:
        if isinstance(data, str):
            if repetition <= 1:
                return self._insertion(data, p)
            else:
                return list(
                    map(
                        self._insertion, repeat(data, repetition), repeat(p, repetition)
                    )
                )
        elif isinstance(data, list):
            if repetition <= 1:
                return list(map(self._insertion, data, repeat(p, len(data))))
            else:
                return list(
                    map(
                        self._insertion,
                        chain.from_iterable(repeat(x, repetition) for x in data),
                        repeat(p, len(data) * repetition),
                    )
                )
        else:
            raise TypeError(f"Does not support the data type : {type(data)}")

    def _insertion(self, data: str, p: float = 0.1) -> str:
        split_words = self.morpheme_analyzer.morphs(replace_space(data))
        words = self.morpheme_analyzer.morphs(data)

        n = max(1, int(len(words) * p))

        new_words = split_words.copy()
        for _ in range(n):
            self.add_word(words, new_words)
        return revert_space(new_words)

    def add_word(self, words: list, new_words: list) -> None:
        synonyms = []
        counter = 0
        while len(synonyms) < 1:
            random_word = words[random.randint(0, len(words) - 1)]
            if self.stopword and random_word in STOPWORD:
                continue
            synonyms = get_synonyms(random_word)
            counter += 1
            if counter >= 10:
                return
        random_synonym = random.choice(synonyms)
        random_idx = random.randint(0, len(new_words) - 1)
        new_words.insert(random_idx, SPACE_TOKEN)
        new_words.insert(random_idx + 1, random_synonym)
        new_words.insert(random_idx + 2, SPACE_TOKEN)
