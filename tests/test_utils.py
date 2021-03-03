from utilities.utils import sum
import pytest

@pytest.mark.parametrize('list_of_integers, result', [
    ([1],1)
])
def test_sum(list_of_integers, result):
    assert sum(list_of_integers) == result
