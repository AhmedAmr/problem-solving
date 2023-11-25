import pytest
from problems.sorting.number_finder import find_first

def test_find_first_case_1():
    _input = [200,200,200,500,500]
    output = 3
    assert find_first(_input, 500) == output

def test_find_first_case_2():
    _input = [200,200,500,500,500]
    output = 2
    assert find_first(_input, 500) == output

def test_find_first_case_3():
    _input = [200,500,500,500,500]
    output = 1
    assert find_first(_input, 500) == output

def test_find_first_case_4():
    _input = [500,500,500,500,500]
    output = 0
    assert find_first(_input, 500) == output

def test_find_first_case_5():
    _input = [200,200,200,200,200]
    output = -1
    assert find_first(_input, 500) == output

def test_find_first_case_6():
    _input = [200,200,200,200,500]
    output = 4
    assert find_first(_input, 500) == output

def test_find_first_case_7():
    _input = [100,200,200,200,500]
    output = 0
    assert find_first(_input, 100) == output



