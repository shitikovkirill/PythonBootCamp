from pbc_app.numbers_pairs import contain_10
import pytest

CONTAINS = [
    ([5, 5, 6, 7, 2, 3, 2, 3],          2,  [(3, 7), (5, 5)]),
    ([1, 2, 3, 4, 5, 5, 6],             2,  [(4, 6), (5, 5)]),
    ([3, 4, 6, 0, 3, 7, 8, 8, 2, 2, 3], 3,  [(3, 7), (2, 8), (4, 6)])
]


@pytest.mark.parametrize("number_list,count,pairs", CONTAINS)
def test_contain_10(number_list, count, pairs):
    result = contain_10(*number_list)
    assert len(result) == count
    for pair in pairs:
        assert pair in result
