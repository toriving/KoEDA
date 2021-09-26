import random
from typing import Union, List
from itertools import repeat, chain

from konlpy.tag import *

from ..utils import replace_space, revert_space, SPACE_TOKEN


class RandomDeletion:
    def __init__(self, morpheme_analyzer: str = None):
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
        return self.random_deletion(*args, **kwargs)

    def random_deletion(
        self, data: Union[List[str], str], p: float = 0.1, repetition: int = 1
    ) -> Union[List[str], str]:
        if isinstance(data, str):
            if repetition <= 1:
                return self._deletion(data, p)
            else:
                return list(
                    map(self._deletion, repeat(data, repetition), repeat(p, repetition))
                )
        elif isinstance(data, list):
            if repetition <= 1:
                return list(map(self._deletion, data, repeat(p, len(data))))
            else:
                return list(
                    map(
                        self._deletion,
                        chain.from_iterable(repeat(x, repetition) for x in data),
                        repeat(p, len(data) * repetition),
                    )
                )
        else:
            raise TypeError(f"Does not support the data type : {type(data)}")

    def _deletion(self, data: str, p: float = 0.1) -> str:
        split_words = self.morpheme_analyzer.morphs(replace_space(data))
        words = self.morpheme_analyzer.morphs(data)

        # obviously, if there's only one word, don't delete it
        if len(words) == 1:
            return words

        # randomly delete words with probability p
        new_words = []
        for word in split_words:
            if word == SPACE_TOKEN:
                new_words.append(word)
                continue
            r = random.uniform(0, 1)
            if r > p:
                new_words.append(word)

        # if you end up deleting all words, just return a random word
        if len(set(filter(SPACE_TOKEN.__ne__, new_words))) == 0:
            rand_int = random.randint(0, len(words) - 1)
            return revert_space([data[rand_int]])

        return revert_space(new_words)
