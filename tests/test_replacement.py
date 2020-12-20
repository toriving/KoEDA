def test_str(SR, str_data):
    assert SR(str_data, 0.8) != str_data
    assert type(SR(str_data, 0.8)) is str
    assert len(SR(str_data, 0.8, repetition=3)) == 3


def test_list(SR, list_data):
    assert SR(list_data, 0.8) != list_data
    assert type(SR(list_data, 0.8)) is list
    assert len(SR(list_data, 0.8, repetition=3)) == len(list_data) * 3
