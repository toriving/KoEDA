def test_str(EDA, str_data):
    assert EDA(str_data, (0.8, 0.8, 0.8, 0.8)) != str_data
    assert type(EDA(str_data, (0.8, 0.8, 0.8, 0.8))) is str
    assert len(EDA(str_data, (0.8, 0.8, 0.8, 0.8), repetition=3)) == 3


def test_list(EDA, list_data):
    assert EDA(list_data, (0.8, 0.8, 0.8, 0.8)) != list_data
    assert type(EDA(list_data, (0.8, 0.8, 0.8, 0.8))) is list
    assert len(EDA(list_data, (0.8, 0.8, 0.8, 0.8), repetition=3)) == len(list_data) * 3
