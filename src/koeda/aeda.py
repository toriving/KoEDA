import random
from typing import Union, List
from itertools import repeat, chain

from konlpy.tag import *

from .utils import replace_space, revert_space, SPACE_TOKEN


class AEasierDataAugmentation:
    def __init__(
        self,
        morpheme_analyzer: str = None,
        punc_ratio: float = 0.3,
        punctuations: List[str] = None
    ):
        if punctuations is None or not isinstance(punctuations, list):
            self.punctuations = ('.', ',', '!', '?', ';', ':')
        else:
            self.punctuations = punctuations

        if morpheme_analyzer is None:
            self.morpheme_analyzer = Okt()
        elif morpheme_analyzer in ["Okt", "Kkma", "Komoran", "Mecab", "Hannanum"]:
            self.morpheme_analyzer = eval(morpheme_analyzer)()
        elif hasattr(morpheme_analyzer, "morphs"):
            self.morpheme_analyzer = morpheme_analyzer
        else:
            raise ValueError(f'Does not support {morpheme_analyzer} morpheme analyzer. '
                             f'Choose one of ["Okt", "Kkma", "Komoran", "Mecab", "Hannanum"]')

        self.ratio = punc_ratio

    def __call__(self, *args, **kwargs):
        return self.aeda(*args, **kwargs)

    def aeda(
            self, data: Union[List[str], str], p: float = None, repetition: int = 1
    ) -> Union[List[str], str]:
        if isinstance(data, str):
            if repetition <= 1:
                return self._aeda(data, p)
            else:
                return list(
                    map(self._aeda, repeat(data, repetition), repeat(p, repetition))
                )
        elif isinstance(data, list):
            if repetition <= 1:
                return list(map(self._aeda, data, repeat(p, len(data))))
            else:
                return list(
                    map(
                        self._aeda,
                        chain.from_iterable(repeat(x, repetition) for x in data),
                        repeat(p, len(data) * repetition),
                    )
                )
        else:
            raise TypeError(f"Does not support the data type : {type(data)}")

    def _aeda(self, data: str, p: float) -> str:
        if p is None:
            p = self.ratio

        split_words = self.morpheme_analyzer.morphs(replace_space(data))
        words = self.morpheme_analyzer.morphs(data)

        new_words = []
        q = random.randint(1, int(p * len(words) + 1))
        qs = random.sample(range(0, len(split_words)), q)

        while self.check_special_selection(split_words, qs):
            qs = random.sample(range(0, len(split_words)), q)

        for j, word in enumerate(split_words):
            if j in qs:
                new_words.append(SPACE_TOKEN)
                new_words.append(
                    self.punctuations[random.randint(0, len(self.punctuations) - 1)])
                new_words.append(SPACE_TOKEN)
                new_words.append(word)
            else:
                new_words.append(word)

        augmented_sentences = revert_space(new_words)

        return augmented_sentences

    @staticmethod
    def check_special_selection(split_words: list, qs: list) -> bool:
        for i in qs:
            if split_words[i] == SPACE_TOKEN:
                return True
        return False
