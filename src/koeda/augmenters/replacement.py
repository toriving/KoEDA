import random
from typing import Union, List
from itertools import repeat, chain

from konlpy.tag import *

from ..utils import replace_space, revert_space, get_synonyms, STOPWORD


class SynonymReplacement:
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
        return self.synonym_replacement(*args, **kwargs)

    def synonym_replacement(
        self, data: Union[List[str], str], p: float = 0.1, repetition: int = 1
    ) -> Union[List[str], str]:
        if isinstance(data, str):
            if repetition <= 1:
                return self._replacement(data, p)
            else:
                return list(
                    map(
                        self._replacement,
                        repeat(data, repetition),
                        repeat(p, repetition),
                    )
                )
        elif isinstance(data, list):
            if repetition <= 1:
                return list(map(self._replacement, data, repeat(p, len(data))))
            else:
                return list(
                    map(
                        self._replacement,
                        chain.from_iterable(repeat(x, repetition) for x in data),
                        repeat(p, len(data) * repetition),
                    )
                )
        else:
            raise TypeError(f"Does not support the data type : {type(data)}")

    def _replacement(self, data: str, p: float = 0.1) -> str:
        split_words = self.morpheme_analyzer.morphs(replace_space(data))
        words = self.morpheme_analyzer.morphs(data)

        n = max(1, int(len(words) * p))

        new_words = split_words.copy()
        if self.stopword:
            random_word_list = list(
                set([word for word in words if word not in STOPWORD])
            )
        else:
            random_word_list = list(set(words))

        random.shuffle(random_word_list)
        num_replaced = 0
        for random_word in random_word_list:
            synonyms = get_synonyms(random_word)
            if len(synonyms) >= 1:
                synonym = random.choice(list(synonyms))
                new_words = [
                    synonym if word == random_word else word for word in split_words
                ]
                num_replaced += 1
            if num_replaced >= n:  # only replace up to n words
                break

        return revert_space(new_words)
