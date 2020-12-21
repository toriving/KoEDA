def test_str(RI, str_data):
    assert RI(str_data, 0.8) != str_data
    assert type(RI(str_data, 0.8)) is str
    assert len(RI(str_data, 0.8, repetition=3)) == 3


def test_list(RI, list_data):
    assert RI(list_data, 0.8) != list_data
    assert type(RI(list_data, 0.8)) is list
    assert len(RI(list_data, 0.8, repetition=3)) == len(list_data) * 3
