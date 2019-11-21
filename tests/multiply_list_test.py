import pytest
from pythonExercises import multiply_list

def testMultiplyListFloat():
    assert multiply_list.product([2.5, 3.5, 6.5]) == 56.875

def testMultiplyListNumbers():
    assert multiply_list.product([2, 3, 6, 4, 2]) == 288
