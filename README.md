<h1 align="center">
KoEDA
</h1>
<p align="center">
    <a href="https://github.com/toriving/KoEDA/actions">
        <img alt="Deploy" src="https://github.com/toriving/KoEDA/workflows/deploy/badge.svg">
    </a>
    <a href="https://github.com/toriving/KoEDA/actions">
        <img alt="Test" src="https://github.com/toriving/KoEDA/workflows/test/badge.svg">
    </a>
    <a href="https://github.com/toriving/KoEDA/releases">
        <img alt="Release" src="https://img.shields.io/github/release/toriving/KoEDA.svg">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
</p>

<h3 align="center">
<p>Easy Data Augmentation for Korean
</h3>

This is a project that re-implemented Easy data augmentation and A Easier Data Augmentation, which were implemented for English, to fit Korean.

## Prerequisites
- python >= 3.7

## Installation
This repository is tested on Python 3.7 - 3.9.  

KoEDA can be installed using pip as follows:
```shell script
$ pip install koeda
```

## Quick Start
- EDA
```python
from koeda import EDA


eda = EDA(
    morpheme_analyzer="Okt", alpha_sr=0.3, alpha_ri=0.3, alpha_rs=0.3, prob_rd=0.3
)

text = "아버지가 방에 들어가신다"

result = eda(text)
print(result)
# 아버지가 정실에 들어가신다

result = eda(text, p=(0.9, 0.9, 0.9, 0.9), repetition=2)
print(result)
# ['아버지가 객실 아빠 안방 방에 정실 들어가신다', '아버지가 탈의실 방 휴게실 에 안방 탈의실 들어가신다']
```

- AEDA
```python
from koeda import AEDA


aeda = AEDA(
    morpheme_analyzer="Okt", punc_ratio=0.3, punctuations=[".", ",", "!", "?", ";", ":"]
)

text = "어머니가 집을 나가신다"

result = aeda(text)
print(result)
# 어머니가 ! 집을 , 나가신다

result = aeda(text, p=0.9, repetition=2)
print(result)
# ['! 어머니가 ! 집 ; 을 ? 나가신다', '. 어머니 ? 가 . 집 , 을 , 나가신다']
```
## Augmenters
- EasyDataAugmentation (EDA)
- AEasierDataAugmentation (AEDA)
- RandomDeletion (RD)
- RandomInsertion (RI)
- SynonymReplacement (SR)
- RandomSwap (RS)

There are two ways to load Augmenter.
  
The first is to use the full name.
```python
from koeda import EasyDataAugmentation
```
The second is to use abbreviations.
```python
from koeda import EDA
```

## Usage
- EDA
```python
augmenter = EDA(
              morpheme_analyzer: str = None,  # Default = "Okt"
              alpha_sr: float = 0.1,
              alpha_ri: float = 0.1,
              alpha_rs: float = 0.1,
              prob_rd: float = 0.1
            )

result = augmenter(
            data: Union[List[str], str], 
            p: List[float] = None,  # Default = (0.1, 0.1, 0.1, 0.1)
            repetition: int = 1
          )
```

- AEDA
```python
augmenter = AEDA(
              morpheme_analyzer: str = None,  # Default = "Okt"
              punc_ratio: float = 0.3,
              punctuations: List[str] = None  # default = ('.', ',', '!', '?', ';', ':')
            )

result = augmenter(
            data: Union[List[str], str], 
            p: float = None,  # Default = 0.3 
            repetition: int = 1
          )
```

- The others (RD, RI, SR, RS)
```python
augmenter = RD(
              morpheme_analyzer: str = None, 
            )

augmenter = RI(
              morpheme_analyzer: str = None, 
              stopword: bool = False
            )

augmenter = SR(
              morpheme_analyzer: str = None, 
              stopword: bool = False
            )

augmenter = RS(
              morpheme_analyzer: str = None, 
            )

result = augmenter(
            data: Union[List[str], str], 
            p: float = 0.1,
            repetition: int = 1
          )
```

## Reference
[Easy Data Augmentation Paper](https://www.aclweb.org/anthology/D19-1670.pdf)  
[Easy Data Augmentation Repository](https://github.com/jasonwei20/eda_nlp)  
[A Easier Data Augmentation Paper](https://arxiv.org/pdf/2108.13230.pdf)  
[A Easier Data Augmentation Repository](https://github.com/akkarimi/aeda_nlp)  
[Korean WordNet](http://wordnet.kaist.ac.kr/)
