import pytest
from problems.sorting.find_the_duplicates import find_duplicates


def test_find_duplicates_1():
    arr1 = [1,2,3,4,5]
    arr2 = [6,7,8,9,10]
    output = []

    assert find_duplicates(arr1, arr2) == output


def test_find_duplicates_2():
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,3,4,5]
    output = [1,2,3,4,5]

    assert find_duplicates(arr1, arr2) == output

def test_find_duplicates_3():
    arr1 = [1,2,3,4,5]
    arr2 = [1,3]
    output = [1,3]

    assert find_duplicates(arr1, arr2) == output

def test_find_duplicates_4():
    arr1 = [2,10]
    arr2 = [1,10,100,200,400]
    output = [10]

    assert find_duplicates(arr1, arr2) == output

def test_find_duplicates_5():
    arr1 = []
    arr2 = [1,10,100,200,400]
    output = []

    assert find_duplicates(arr1, arr2) == output

def test_find_duplicates_6():
    arr1 = [1,10,100,200,400]
    arr2 = []
    output = []

    assert find_duplicates(arr1, arr2) == output