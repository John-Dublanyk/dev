import pytest
from projects.hw12.hw12 import compute_complexity
'''
1st- no special characters, 2nd- two special characters, 
3rd- only special characters, 4th- empty string
'''
@pytest.mark.parametrize('key', [
    ('johndub123', 0.0),
    ('j0hn@ub1!', 14.285714285714286),
    ('!^^&', 100.0),
    ('', 0.0),
])
def test_key(key):
    this_key = key
    assert compute_complexity(this_key)
