import pytest
import numpy as np

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int, get_data_as_numpy_array, split_into_training_and_testing_sets

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
    assert convert_to_int("2,018") == 2018

def test_on_string_with_one_comma_new():
    return_value = convert_to_int("2,018")
    assert isinstance(return_value, int)
    assert return_value == 2018

# Write an informative test failure message : The test result reports become a lot easier to read when we make good use of the optional message argument of the assert statement.
# the convert_to_int() function. The function takes an integer valued string with commas as thousand separators e.g. "2,081" as argument and should return the integer 2081
# we will rewrite the test called test_on_string_with_one_comma() so that it prints an informative message if the test fails.

def test_on_string_with_one_comma_new2():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    # Format the string with the actual return value
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)

    # Write the assert statement which prints message on failure
    assert actual is expected, message
    # message = "convert_to_int('2,081') should return the int {0}, but it actually returned {1}".format(expected, actual)

# Testing float return values
# The get_data_as_numpy_array() function takes two arguments: the path to a clean data file and the number of data columns in the file .
# The function converts the data into a 3x2 NumPy array with dtype=float64. The expected return value has been stored in a variable called expected
# The housing areas are in the first column and the housing prices are in the second column. This array will be the features that will be fed to the linear regression model for learning.
# The return value contains floats. Therefore we have to be especially careful when writing unit tests for this function.

def test_on_clean_file():
    expected = np.array([[2081.0, 314942.0],
                        [1059.0, 186606.0],
                        [1148.0, 206186.0]
                        ]
                        )
    actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
    message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
    # Complete the assert statement
    assert actual == pytest.approx(expected), message
    # The pytest.approx() function not only works for NumPy arrays containing floats, but also for lists and dictionaries containing floats.

# Testing with multiple assert statements : test the function split_into_training_and_testing_sets() 
def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = 2
    actual = split_into_training_and_testing_sets(example_argument)
    # Write the assert statement checking training array's number of rows
    assert actual[0].shape[0] == expected_training_array_num_rows, "The actual number of rows in the training array is not {}".format(expected_training_array_num_rows)
    # Write the assert statement checking testing array's number of rows
    assert actual[1].shape[1] == expected_testing_array_num_rows, "The actual number of rows in the testing array is not {}".format(expected_testing_array_num_rows)


