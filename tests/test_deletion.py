def test_str(RD, str_data):
    assert RD(str_data, 0.8) != str_data
    assert type(RD(str_data, 0.8)) is str
    assert len(RD(str_data, 0.8, repetition=3)) == 3


def test_list(RD, list_data):
    assert RD(list_data, 0.8) != list_data
    assert type(RD(list_data, 0.8)) is list
    assert len(RD(list_data, 0.8, repetition=3)) == len(list_data) * 3
