import time

from src.prime_search import next_prime


def benchmark_next_prime(digits: int) -> None:
    # Benchmark next_prime for a number with the specified digit count.
    n = 10 ** (digits - 1)

    start_time = time.perf_counter()
    result = next_prime(n)
    elapsed_time = time.perf_counter() - start_time

    gap = result - n

    print(
        f"Digits: {digits} | "
        f"Time: {elapsed_time:.6f} seconds | "
        f"Gap: {gap}"
    )

if __name__ == "__main__":
    for digits in [10, 100, 500, 1000]:
        benchmark_next_prime(digits)