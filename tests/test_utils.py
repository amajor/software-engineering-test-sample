from utilities.utils import sum
import pytest

@pytest.mark.parametrize('list_of_integers, result', [
    ([1],1)
])
def test_sum(list_of_integers, result):
    assert sum(list_of_integers) == result

###########################
# Test Exception Messages #
###########################

def catch_exception(bad_input, expected_exception_phrase):
    with pytest.raises(Exception, match=r".*" + expected_exception_phrase + ".*"):
        sum(bad_input)

# Test input is only list of integers
@pytest.mark.parametrize('bad_input', [
    ('string of some kind'),
    (1),
    (-1),
    (0),
    (2.34)
])
def test_only_list(bad_input):
    expected_exception_phrase = "Input type 'list' only."
    catch_exception(bad_input, expected_exception_phrase)

# Test input is only list of positive integers
@pytest.mark.parametrize('bad_input', [
    # ([1.2, 3.40]),
    # (['a','b','c']),
    ([-1])
])
def test_only_positive_integers(bad_input):
    expected_exception_phrase = "Positive integers only."
    catch_exception(bad_input, expected_exception_phrase)

def test_empty_list():
    empty_list = []
    expected_exception_phrase = "List cannot be empty."
    catch_exception(empty_list, expected_exception_phrase)
