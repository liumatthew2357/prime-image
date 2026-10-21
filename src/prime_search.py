from src.primality import is_probable_prime

def next_prime(n: int) -> int:
    # Find the next prime number greater than n.
    if n < 2:
        return 2
    candidate = n + 1 if n % 2 == 0 else n + 2
    while True:
        if is_probable_prime(candidate):
            return candidate
        candidate += 2
