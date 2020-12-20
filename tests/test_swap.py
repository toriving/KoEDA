def test_str(RS, str_data):
    assert RS(str_data, 0.8) != str_data
    assert type(RS(str_data, 0.8)) is str
    assert len(RS(str_data, 0.8, repetition=3)) == 3


def test_list(RS, list_data):
    assert RS(list_data, 0.8) != list_data
    assert type(RS(list_data, 0.8)) is list
    assert len(RS(list_data, 0.8, repetition=3)) == len(list_data) * 3
