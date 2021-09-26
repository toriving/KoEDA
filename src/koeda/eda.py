import random
from typing import Union, List
from itertools import repeat, chain

from konlpy.tag import *

from .augmenters import *


class EasyDataAugmentation:
    def __init__(
        self,
        morpheme_analyzer: str = None,
        alpha_sr: float = 0.1,
        alpha_ri: float = 0.1,
        alpha_rs: float = 0.1,
        prob_rd: float = 0.1,
    ):
        if morpheme_analyzer is None:
            self.morpheme_analyzer = Okt()
        elif morpheme_analyzer in ["Okt", "Kkma", "Komoran", "Mecab", "Hannanum"]:
            self.morpheme_analyzer = eval(morpheme_analyzer)()
        elif hasattr(morpheme_analyzer, "morphs"):
            self.morpheme_analyzer = morpheme_analyzer
        else:
            raise ValueError(f'Does not support {morpheme_analyzer} morpheme analyzer. '
                             f'Choose one of ["Okt", "Kkma", "Komoran", "Mecab", "Hannanum"]')

        self.alphas = (alpha_sr, alpha_ri, alpha_rs, prob_rd)

        self.augmentations = (
            SynonymReplacement(self.morpheme_analyzer, False),
            RandomInsertion(self.morpheme_analyzer, False),
            RandomSwap(self.morpheme_analyzer),
            RandomDeletion(self.morpheme_analyzer),
        )

    def __call__(self, *args, **kwargs):
        return self.eda(*args, **kwargs)

    def eda(
        self, data: Union[List[str], str], p: List[float] = None, repetition: int = 1
    ) -> Union[List[str], str]:
        if isinstance(data, str):
            if repetition <= 1:
                return self._eda(data, p)
            else:
                return list(
                    map(self._eda, repeat(data, repetition), repeat(p, repetition))
                )
        elif isinstance(data, list):
            if repetition <= 1:
                return list(map(self._eda, data, repeat(p, len(data))))
            else:
                return list(
                    map(
                        self._eda,
                        chain.from_iterable(repeat(x, repetition) for x in data),
                        repeat(p, len(data) * repetition),
                    )
                )
        else:
            raise TypeError(f"Does not support the data type : {type(data)}")

    def _eda(self, data: str, p: List[float]) -> str:
        random_idx = random.randint(0, 3)
        if p is None or len(p) != 4:
            p = self.alphas

        augmented_sentences = self.augmentations[random_idx](data, p[random_idx])

        return augmented_sentences
