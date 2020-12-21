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

## Prerequisites
- python >= 3.6

## Installation
This repository is tested on Python 3.6 - 3.9.  
KoEDA can be installed using pip as follows:
```shell script
$ pip install koeda
```

## Quick Start

```python
from koeda import EasyDataAugmentation


EDA = EasyDataAugmentation(
    morpheme_analyzer=None, alpha_sr=0.3, alpha_ri=0.3, alpha_rs=0.3, prob_rd=0.3
)

text = "아버지가 방에 들어가신다"

result = EDA(text)
print(result)
# 아버지가 정실에 들어가신다
```

## Augmenters
- EasyDataAugmentation (EDA)
- RandomDeletion (RD)
- RandomInsertion (RI)
- SynonymReplacement (SR)
- RandomSwap (RS)


## Usage
- EDA class
```python
EDA = EasyDataAugmentation(
    morpheme_analyzer: str = None,
    alpha_sr: float = 0.1,
    alpha_ri: float = 0.1,
    alpha_rs: float = 0.1,
    prob_rd: float = 0.1,
):

text = "아버지가방에들어가신다"

# EDA(data: Union[List[str], str], p: List[float] = None, repetition: int = 1)
result = EDA(data=text, p=None, repetition=1)
```

- The others (RD, RI, SR, RS)
```python
augmenter = Augmenter(morpheme_analyzer: str = None, stopword: bool = False)

text = "아버지가방에들어가신다"

# augmenter(data: Union[List[str], str], p: float = 0.1, repetition: int = 1)
result = augmenter(data=text, p=0.5, repetiion=1)
```

## Reference
[Easy Data Augmentation Paper](https://www.aclweb.org/anthology/D19-1670.pdf)  
[Easy Data Augmentation Repository](https://github.com/jasonwei20/eda_nlp)  
[Korean WordNet](http://wordnet.kaist.ac.kr/)
