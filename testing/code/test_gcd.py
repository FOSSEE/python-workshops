from gcd import gcd, atoi

def test_gcd():
    assert gcd(48, 64) == 16
    assert gcd(44, 19) == 1

def test_atoi_works():
    x = '1'
    assert atoi(x) == 1

import pytest

def test_atoi_raises_error():
    x = 'hello'
    with pytest.raises(ValueError):
        atoi(x)


if __name__ == '__main__':
    test_gcd()

