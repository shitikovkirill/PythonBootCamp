from numbers_pairs import contain_10


def test_contain_10_case1():
    result = contain_10(5, 5, 6, 7, 2, 3, 2, 3)
    assert len(result) == 2
    assert (3, 7) in result
    assert (5, 5) in result


def test_contain_10_case2():
    result = contain_10(1, 2, 3, 4, 5, 5, 6)
    assert len(result) == 2
    assert (4, 6) in result
    assert (5, 5) in result


def test_contain_10_case3():
    result = contain_10(3, 4, 6, 0, 3, 7, 8, 8, 2, 2, 3,)
    assert len(result) == 3
    assert (3, 7) in result
    assert (2, 8) in result
    assert (4, 6) in result
