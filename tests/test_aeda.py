def test_str(AEDA, str_data):
    assert AEDA(str_data, 0.8) != str_data
    assert type(AEDA(str_data, 0.8)) is str
    assert len(AEDA(str_data, 0.8, repetition=3)) == 3


def test_list(AEDA, list_data):
    assert AEDA(list_data, 0.8) != list_data
    assert type(AEDA(list_data, 0.8)) is list
    assert len(AEDA(list_data, 0.8, repetition=3)) == len(list_data) * 3
