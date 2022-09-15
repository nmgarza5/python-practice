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
    # init left right, and mid pointers. mid will be reassigned during every iter.
    #   either left or right will be reassigned after during every iter. unless we find the value
    left = 0
    right = len(input_array)-1
    mid = 0

    # keep iterating we find mid or until we have searched through every index
    while right >= left:
        # assign mid. // gives an integer
        mid = (right + left) // 2
        if input_array[mid] < value:
            left = mid + 1
        elif input_array[mid] > value:
            right = mid - 1
        # if input_array[mid] is neither greater or less than, it must be the value. return mid
        else:
            return mid
    # if we exit the while loop, we did not find the value, return -1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
