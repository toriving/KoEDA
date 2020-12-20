__title__ = 'KoEDA'
__version__ = '0.0.3'

__author__ = 'Dongju Park'
__email__ = 'toriving@gmail.com'
__url__ = 'http://toriving.github.io'

__summary__ = 'Easy Data Augmentation for Korean'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2020 {}'.format(__author__)


from .eda import EasyDataAugmentation

from .augmenters import (
    RandomDeletion,
    RandomInsertion,
    SynonymReplacement,
    RandomSwap
)

from .utils import (
    STOPWORD,
    WORDNET,
    get_synonyms
)
