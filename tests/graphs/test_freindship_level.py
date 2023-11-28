import pytest

from problems.graphs.frendship_level import get_friendship_level


def test1():
    friends = [[0,1,0],[1,0,1],[0,1,0]]
    assert get_friendship_level(friends, 0, 1) == 1
def test2():
    friends = [[0,1,0],[1,0,1],[0,1,0]]
    assert get_friendship_level(friends, 1, 2) == 1
def test3():
    friends = [[0,1,0],[1,0,1],[0,1,0]]
    assert get_friendship_level(friends, 0, 2) == 2

def test4():
    friends = [[0,1,0],[1,0,1],[0,1,0]]
    assert get_friendship_level(friends, 0, 0) == 0

def test5():
    friends = [[0,1,1,0], [1,0,1,0],[1,1,0,1],[0,0,1,0]]
    assert get_friendship_level(friends, 0,3) == 2

def test6():
    friends = [[0,1,1,0], [1,0,1,0],[1,1,0,1],[0,0,1,0]]
    assert get_friendship_level(friends, 0,6) == -1

def test7():
    friends = [[0,1,1,0], [1,0,1,0],[1,1,0,1],[0,0,1,0]]
    assert get_friendship_level(friends, -1,6) == -1