import numpy as np
from sklearn.model_selection import train_test_split

def row_to_list(row):
    # "2,081\t314,942\n"
    try:
        f = row.split('\t')[0]
        s = row.split('\t')[1].split(',')[0]
        t = row.split('\t')[1].split(',')[1].split('\n')[0]
        result = [f, s, t]
    except IndexError:
        result = None
    return result

def convert_to_int(value):
    value = value.replace(',', '')
    return int(value)

def get_data_as_numpy_array(path, num_columns=2):
    with open(path, 'r') as f:
        l = f.readlines()
    row_1 = []
    row_2 = []
    for ele in l:
        # print(ele.split('\t'))
        row_1.append(ele.split('\t')[0])
        row_2.append(ele.split('\t')[1].strip('\n'))
    print(row_1, row_2)
    n = np.empty(shape=(3,num_columns))
    seq = 0
    for i, val in enumerate(row_1):
        n[i, seq] = val
    seq = 1
    for i, val in enumerate(row_2):
        n[i, seq] = val
    return n


# get_data_as_numpy_array('example_clean_data.txt', 2)
def split_into_training_and_testing_sets(array):
    if array.shape[0] <= 1:
        raise ValueError("Argument data_array must have at least 2 rows, it actually has just 1")
    train, test = train_test_split(array)
    print(train.shape, test.shape)
    # print(train)
    # print(test)
    return (train, test)
# split_into_training_and_testing_sets(np.array([[  2081., 314942.],
#        [  1059., 186606.],
#        [  1148., 206186.],
#        [  1506., 248419.],
#        [  1210., 214114.],
#        [  1697., 277794.]])
# )

def convert_to_int_new(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
        # Write the if statement for incorrectly placed commas
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    # Fill in with the correct exception for float valued argument strings
    except ValueError:
        return None