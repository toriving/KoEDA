import random
from typing import Union
from itertools import repeat

from src.koeda.utils import list_to_string, replace_space, revert_space, SPACE_TOKEN
from konlpy.tag import *


class RandomDeletion:

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
        return self.random_deletion(*args, **kwargs)

    def random_deletion(self, data: Union[list, str], p: float = 0.1) -> Union[list, str]:
        if isinstance(data, str):
            return self._deletion(data, p)
        elif isinstance(data, list):
            return list(map(self._deletion, data, repeat(p, len(data))))
        else:
            raise Exception(f"Does not support the data type : {type(data)}")

    def _deletion(self, data: str, p: float = 0.1) -> str:
        split_words = self.morpheme_analyzer.morphs(replace_space(data))
        words = self.morpheme_analyzer.morphs(data)

        # obviously, if there's only one word, don't delete it
        if len(words) == 1:
            return list_to_string(words)

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
            return list_to_string([data[rand_int]])

        return revert_space(new_words)
