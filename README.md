![pytests](https://github.com/amajor/software-engineering-test-sample/actions/workflows/main.yml/badge.svg)

# Unit Test Example

> Using any programming language that you know, write a function/method that accepts a list of positive integers as a parameter and returns the sum of the numbers in that list. Using an appropriate test framework, write automated tests to test that function. Make sure that your program returns an error if the list is empty or if some members of the list are not positive integers.

# Tests

You can see the tests outlined in the test file:

[test_utils.py](./tests/test_utils.py)

- [x] Function adds together positive integers within input list
- [x] Input is only a list
- [x] Input list only contains positive integers
- [x] Input list is not empty

## Pipeline

The tests automatically run in the pipeline.

https://github.com/amajor/software-engineering-test-sample/actions/workflows/main.yml

- [x] Test for successful summation of any number of list items
- [x] Test input is only list of integers (throws exception if not)
- [x] Test input is only list of positive integers (throws exception if not)
- [x] Test for empty lists (throws exception if empty)

<img width="924" alt="Passing Tests" src="https://user-images.githubusercontent.com/796753/110190905-adb86580-7df3-11eb-92f1-8334f36feb8a.png">
