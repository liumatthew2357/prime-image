import secrets


SMALL_PRIMES = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97
)

def decompose(n: int) -> tuple[int, int]:
    # Express n - 1 as 2^s * d, where d is odd.
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    return s, d


def miller_rabin_round(n: int, a: int) -> bool:
    s, d = decompose(n)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = (x * x) % n

        if x == n - 1:
            return True
    return False


def is_probable_prime(n: int, rounds: int = 40) -> bool:
    # Perform multiple Miller-Rabin rounds. (default is 40)
    # Miller-Rabin is a probabilistic test, so more rounds increase the confidence that n is prime.
    
    if rounds <= 0:
        raise ValueError("Number of rounds must be positive.")
    if n < 2:
        return False
    for p in SMALL_PRIMES:
        if n == p:
            return True
        if n % p == 0:
            return False
    for _ in range(rounds):
        a = secrets.randbelow(n - 3) + 2  # Random integer in [2, n-2]
        if not miller_rabin_round(n, a):
            return False
    return True