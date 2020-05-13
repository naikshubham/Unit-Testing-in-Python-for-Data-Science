# Practice the context manager:In pytest, we can test whether a function raises an exception by using a context manager. 
from preprocessing_helpers import split_into_training_and_testing_sets
import pytest
import numpy as np 

# Fill in with a context manager that will silence the ValueError
with pytest.raises(ValueError):
    raise ValueError

try:
    # Fill in with a context manager that raises Failed if no OSError is raised
    with pytest.raises(OSError):
        raise ValueError
except:
    print("pytest raised an exception because no OSError was raised in the context.")


# Store the raised ValueError in the variable exc_info
with pytest.raises(ValueError) as exc_info:
    raise ValueError("Silence me!")

with pytest.raises(ValueError) as exc_info:
    raise ValueError("Silence me!")
# Check if the raised ValueError contains the correct message
assert exc_info.match("Silence me!")

#Unit test a ValueError : Sometimes, we want a function to raise an exception when called on bad arguments. This prevents the function from returning nonsense results or hard-to-interpret exceptions.
#This is an important behavior which should be unit tested.

'''
Remember the function split_into_training_and_testing_sets()? It takes a NumPy array containing housing area and prices as argument. 
The function randomly splits the array row wise into training and testing arrays in the ratio 3:1, and returns the resulting arrays in a tuple.
If the argument array has only 1 row, the testing array will be empty. To avoid this situation, we want the function to not return anything, 
but raise a ValueError with the message "Argument data_array must have at least 2 rows, it actually has just 1"
'''

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Store information about raised ValueError in exc_info
    with pytest.raises(ValueError) as exc_info:
      split_into_training_and_testing_sets(test_argument)
    expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
    # Check if the raised ValueError contains the correct message
    assert exc_info.match(expected_error_msg)




















