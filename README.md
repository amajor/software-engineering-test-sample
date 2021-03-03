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