__title__ = "KoEDA"
__version__ = "0.0.4"

__author__ = "Dongju Park"
__email__ = "toriving@gmail.com"
__url__ = "http://toriving.github.io"

__summary__ = "Easy Data Augmentation for Korean"
__license__ = "MIT License"
__copyright__ = "Copyright 2020 {}".format(__author__)


from .eda import EasyDataAugmentation
from .aeda import AEasierDataAugmentation
from .augmenters import RandomDeletion, RandomInsertion, \
    SynonymReplacement, RandomSwap

from .aeda import AEasierDataAugmentation as AEDA
from .eda import EasyDataAugmentation as EDA
from .augmenters import RandomDeletion as RD
from .augmenters import RandomInsertion as RI
from .augmenters import SynonymReplacement as SR
from .augmenters import RandomSwap as RS
