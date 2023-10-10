import pytest
from projects.hw11.hw11 import get_formal_name

@pytest.mark.parametrize('key', [
    ('apple', 'Malus domestica'),
    ('pear', 'Pyrus'),
    ('banana', 'Musa acuminata'),
    ('grape', 'Vitis vinifera'),
    
])

def test_get_formal_name(key):
    this_key = key
    assert get_formal_name(this_key)
