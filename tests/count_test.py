import pytest
from pythonExercises import count

def testCountZeros():
    assert count.count([0, 0, 0, 0], 0) == 4

def testCountMix():
    assert count.count([2, 5, 3, 4, 1, 6, 3, 4, 2, 3, 2], 2) == 3

def testCountA():
    assert count.count("aaaaa", "a") == 5

def testCountString():
    assert count.count("efeeewf", "e") == 4

def testCountStringList():
    assert count.count(["a", "f", "a", "a", "a", "f"], "a") == 4
