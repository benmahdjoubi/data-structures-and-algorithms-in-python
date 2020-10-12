"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""

    # middle index
    m = len(input_array) // 2

    # find the first, middle and last values
    first_element = input_array[0] 
    middle_element = input_array[m]
    last_element = input_array[-1]
    
    # Array of length 1

    i = 0
    while i < len(input_array) and len(input_array) > 1:
        # Found the element
        if value == input_array[i]:
            return i
            break
        # Eliminate the lower half
        elif value > middle_element:
            first_element = input_array[m+1]
        # Eliminate the upper half
        elif value < middle_element:
            last_element = input_array[m]
        i += 1

    if len(input_array) == 1 and value == input_array[0]:
        return 0
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15

test_list2 = [0]
test_val3 = 0
# return -1
print(binary_search(test_list, test_val1))
# return 4
print(binary_search(test_list, test_val2))

print(binary_search(test_list2, test_val3))