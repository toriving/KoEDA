import pytest

from koeda import EasyDataAugmentation
from koeda import AEasierDataAugmentation
from koeda import RandomDeletion
from koeda import RandomInsertion
from koeda import SynonymReplacement
from koeda import RandomSwap


@pytest.fixture
def EDA():
    EDA = EasyDataAugmentation()
    return EDA


@pytest.fixture
def AEDA():
    AEDA = AEasierDataAugmentation()
    return AEDA


@pytest.fixture
def RD():
    RD = RandomDeletion()
    return RD


@pytest.fixture
def RI():
    RI = RandomInsertion()
    return RI


@pytest.fixture
def SR():
    SR = SynonymReplacement()
    return SR


@pytest.fixture
def RS():
    RS = RandomSwap()
    return RS


@pytest.fixture
def str_data():
    str_data = "아버지가 방에 들어가신다."
    return str_data


@pytest.fixture
def list_data():
    list_data = ["아버지가 방에 들어가신다.",
                 "어머니가 집을 나가신다.",
                 "아버지가방에들어가신다 .",
                 "어머니가집을나가신다 ."]
    return list_data
