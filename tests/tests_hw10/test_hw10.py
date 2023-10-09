import pytest
from projects.hw10.fruit_query import is_it_a_fruit


def test_1():
    assert is_it_a_fruit('apple') == True

def test_2():
    assert is_it_a_fruit('pear') == True

def test_3():
    assert is_it_a_fruit('BAnanna') == False

def test_4():
    assert is_it_a_fruit('') == False

def test_4():
    assert is_it_a_fruit('cherry') == False