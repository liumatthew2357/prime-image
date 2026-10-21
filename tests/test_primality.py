import pytest

from src.primality import decompose, miller_rabin_round, is_probable_prime


def test_decompose():
    assert decompose(41) == (3, 5)
    assert decompose(101) == (2, 25)
    assert decompose(17) == (4, 1)


def test_miller_rabin_round():
    assert miller_rabin_round(17, 2) is True
    assert miller_rabin_round(21, 2) is False


def test_strong_pseudoprime():
    assert miller_rabin_round(2047, 2) is True
    assert miller_rabin_round(2047, 3) is False


def test_known_primes():
    for n in [2, 3, 5, 7, 11, 101, 1009, 7919]:
        assert is_probable_prime(n) is True


def test_known_composites():
    for n in [4, 6, 9, 15, 21, 561, 1105, 1729]:
        assert is_probable_prime(n) is False


def test_invalid_rounds():
    with pytest.raises(ValueError):
        is_probable_prime(101, rounds=0)

    with pytest.raises(ValueError):
        is_probable_prime(101, rounds=-5)