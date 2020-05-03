# Unit testing in Python for Data Science
- Every data science project needs unit testing. It comes with huge benefits - saving a lot of development and maintenance time, improving documentation, increasing end-user trust and reducing downtime of productive systems. As a result, unit testing has become a must-have skill in the industry, used by almost every company. 
- Unit tests for data preprocessors, models and visualizations, interpret test results and fix any buggy code. We will also learn advanced concepts like TDD, test organization, fixtures and mocking so that you can test your own data science projects properly.

### Unit testing basics

#### Why Unit test?
- How can we test an implementation of pythton function is correct? The easiest way is to open the interpreter and pass few arguments and check whether the return value is correct. Testing on interpreter is easy but its very inefficient.

#### Life cycle of a function

<p align="center">
  <img src="./images/lifecycle.JPG" width="350" title="Lifecycle of a function">
</p>

- Notice how many times we need to test the function, either to fix bugs or to implement new features, we have to test it everytime we have to test it. If a project continues for few years we might be testing the function about a 100 times, maybe more.

#### Manual test vs. Unit tests
- Unit tests automates this repetitve and tedious testing process.


### Write a simple unit test using pytest
- There are many python libraries to write unit tests such as pytest, unittest, nosetests and doctest. Pytest has all essential features and most popular testing library in Python.
- *Step 1*: Create a file called `test_row_to_list.py`
- When pytest sees a filename starting with **"test_"** , it understands that this is not an usual Python file, but a special one containing unit tests.We must make sure to follow this naming convention. Files holding unit tests are also called test modules.

```python
# test module
import pytest
import row_to_list   # import function under test
```

- A unit test is written as a Python function, whose name starts with a "test_", just like the test module. This way, pytest can tell that it is a unit test and not an ordinary function.
- The unit test usually corresponds to exactly one entry in the argument and return value table for `row_to_list()`. The unit test checks whether `row_to_list()` has the expected return value when called on this particular argument.

```python
def test_for_clean_row():
    assert row_to_list("2,081\t314, 942\n") == ["2,081", "314,942"]
    
def test_for_missing_area():
    assert row_to_list("\t293,410\n") is None
 
def test_for_missing_tab():
    assert row_to_list("1,463238, 765\n") is None
```

- This particular argument is a clean row, so we call the unit test test_for_clean_row(). The actual check is done via an assert statement, and every test must contain one.

#### Theoretical structure of an assertion

`assert boolean_expression`

- The assert statement has a required first argument, which can be any boolean expression. **If the expression is True, the assert statement passes, giving us a blank output. If the expression is False it raises an AssertionError.**
- **1)** In this case, we want to check if row_to_list() returns the correct list when called on the clean row.
- **2)** Second we create a test called `test_for_missing_area()` because the argument has missing area data. Then we assert that the return value for this argument is None.
- **3)** Third we create `test_for_missing_tab` because the argument is missing the tab separating area and price.

#### Running unit tests
- To test whether `row_to_list()` is working in its life cycle, we simply run the test module. The standard way to run tests is to open a command line and type pytest followed by the test module name.
- **`!pytest test_module.py`**

```python
 D:\Projects\Datacamp\Unit Testing in Python for Data Science\test_modules>pytest test_preprocessing_helpers.py
====================================================================================== test session starts ====================================================================================== 
platform win32 -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: D:\Projects\Datacamp\Unit Testing in Python for Data Science\test_modules, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 1 item                                                                                                                                                                                  

test_preprocessing_helpers.py .                                                                                                                                                            [100%] 

=================================================================================== 1 passed in 0.03 seconds ==================================================================================== 
```

### Understanding test result report

- test result of **test_row_to_list.py**

```python
(base) D:\Projects\Datacamp\Unit Testing in Python for Data Science\test_modules>pytest test_row_to_list.py
====================================================================================== test session starts ======================================================================================
platform win32 -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: D:\Projects\Datacamp\Unit Testing in Python for Data Science\test_modules, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 3 items

test_row_to_list.py FF.                                                                                                                                                                    [100%]

=========================================================================================== FAILURES ============================================================================================ 
______________________________________________________________________________________ test_for_clean_row _______________________________________________________________________________________ 

    def test_for_clean_row():
>       assert row_to_list("2,081\t314, 942\n") == ["2,081", "314,942"]
E       AssertionError: assert ['2,081', '314', ' 942'] == ['2,081', '314,942']
E         At index 1 diff: '314' != '314,942'
E         Left contains more items, first extra item: ' 942'
E         Use -v to get the full diff

test_row_to_list.py:6: AssertionError
_____________________________________________________________________________________ test_for_missing_area _____________________________________________________________________________________ 

    def test_for_missing_area():
>       assert row_to_list("\t293,410\n") is None
E       AssertionError: assert ['', '293', '410'] is None
E        +  where ['', '293', '410'] = row_to_list('\t293,410\n')

test_row_to_list.py:9: AssertionError
============================================================================== 2 failed, 1 passed in 0.14 seconds =============================================================================== 
```

| Character| Meaning | When                                           | Action                         |
:---------:|:-------:|:----------------------------------------------:|:------------------------------:|
| *F*      | Failure |An exception is raised when running unit test   |Fix the function or unit test   |
| *.*      | Passed  |No exception raised when running unit test      |Everything is fine              |

- If we get an AssertionError, this means the function has a bug and you should fix it. If you get another exception, e.g. NameError, this means that something else is wrong with the unit test code and you should fix it so that the assert statement can actually run.

### More benefits and tests types

#### Unit tests serve as documentation
- This is why - when onboarding new colleagues - it is a good idea to tell them to look at the unit tests if they are not sure about a function's purpose. 

#### More trust
- Unit tests also increase trust in a package, as users can run the unit tests and verify that the functions work.

#### Reduced Downtime

<p align="center">
  <img src="./images/CI.JPG" width="350" title="Reduced Downtime">
</p>

- Suppose we make a mistake and push a bad code to a productive system. This will bring the system down and annoy the users. We can cure this by setting up Continuos Integration or CI. 
- **CI** runs all unit tests when any code is pushed, and if any unit test fails, it rejects the change, preventing downtime. It also informs us that the code needs to be fixed.
- If we run productive systems that many people depend upon, we must write unit tests and setup CI.

<p align="center">
  <img src="./images/unit_test.JPG" width="350" title="Unit Test">
</p>

- We will write unit tests for all functions in the example linear regression project. We already wrote tests for `row_to_list()` and `convert_to_int()`. They are part of the data module, which creates a clean data file from raw data on housing area and price. We will also see functions from the feature module, which compute features from the clean data. Also the models module, which will output a model for predicting housing price from the features.These are called **Unit test**.
- In contrast, **Integration tests** check if multiple units work well together when they are connected, and not just independently. FOr example, we could check if the data and the feature module work well when connected. Here the argument will be the raw data, and the return values to check would be the features.
- **End to End tests** check the whole software at once. They start from one end, which is the unprocessed data file, goes through all the units till the other end, and checks whether we get the correct model.

### Mastering assert statements 
- So far we have used only a boolean expression as an argument of the assert statement. But the assert statement can take an optional second argument, called the **message**. 
- `assert boolean_expression, message`
- The message is only printed when the assert statement raises an AssertionError and it should contain information about why the AssertionError was raised.**If the assert statement passes, nothing is printed** 
- We could enhance `test_for_missing_area` by adding a messsage

```python
import pytest
....

def test_for_missing_area_with_message():
    actual = row_to_list("\t293, 410\n")
    expected = None
    message = ("row_to_list('\t293, 410\n') returned{0} instead of {1}".format(actual, expected))
    assert actual is expected , message
```

- Now we get nice human readable message tet next to the AssertionError

```python
>       assert actual is expected , message
E       AssertionError: row_to_list('   293, 410
E         ') returned['', '293', ' 410'] instead of None
E       assert ['', '293', ' 410'] is None
```

#### Beware of float return values!
- A tricky situation when the function returns a float. In python, comparisons between floats dont always work as expected.
- `0.1 + 0.1 + 0.1 == 0.3` -->> outputs `False`
- Because of the way Python represents floats, the digits on the right might be different from what we expect causing comparisons to fail.
- `0.1 + 0.1 + 0.1` -->> outputs `0.3000000000004`
- The bottom line is : we should not use the usual way to compare floats in the assert statement. Instead we should use the **`pytest.approx()`** to wrap the expected value.
- `assert 0.1 + 0.1 + 0.1 == pytest.approx(0.3)`

#### Numpy arrays containing floats
- pytest.approx() also works for numpy arrays containing floats.
- `assert np.array([0.1 + 0.1, 0.1 + 0.1 + 0.1]) == pytest.approx(np.array([0.2, 0.3])`

#### Multiple assertions in one unit test
- So far, we have only seen one assert statement per unit test, but unit tests can have more than one assert statement.We will modify the unit test `test_convert_to_int.py`
- We first wanted to test if the function returns an integer at all.For this, we use the `isinstance()` function, which takes the return value as a first argument and the expected type of the return value as a second argument, which is int in this case.We follow up with another assert statement which checks if the return value matches the expected value.
- The modified test will pass if both assertions pass. It will fail if any of them raises AssertionError.

```python
import pytest

def test_on_string_with_one_comma():
    return_value = convert_to_int("2,018")
    assert isinstance(return_value, int)
    assert return_value == 2018
```




















































    
    
    
    
    
    
    
    
    
    
    
    




























































































































