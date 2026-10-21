from src.prime_search import next_prime


def test_small_inputs():
    assert next_prime(-10) == 2
    assert next_prime(0) == 2
    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5


def test_even_composites():
    assert next_prime(4) == 5
    assert next_prime(8) == 11
    assert next_prime(10) == 11
    assert next_prime(20) == 23


def test_odd_composites():
    assert next_prime(9) == 11
    assert next_prime(15) == 17
    assert next_prime(21) == 23
    assert next_prime(25) == 29


def test_prime_inputs():
    assert next_prime(5) == 7
    assert next_prime(11) == 13
    assert next_prime(17) == 19
    assert next_prime(97) == 101


def test_larger_inputs():
    assert next_prime(100) == 101
    assert next_prime(101) == 103
    assert next_prime(1000) == 1009
    assert next_prime(10000) == 10007


def test_skipping_multiple_composites():
    assert next_prime(24) == 29
    assert next_prime(89) == 97
    assert next_prime(113) == 127


def test_result_is_strictly_greater():
    for n in range(-10, 101):
        assert next_prime(n) > n

from src.image_processing import average_color


