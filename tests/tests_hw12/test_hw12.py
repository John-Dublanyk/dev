import pytest
from projects.hw12.hw12 import compute_complexity

@pytest.mark.parametrize('key', [
    ('johndub123', 0.0),
    ('j0hn@ub1!', 14.285714285714286),
    ('!^^&', 100.0),
    ('', 0.0),
])
def test_key(key):
    this_key = key
    assert compute_complexity(this_key)
