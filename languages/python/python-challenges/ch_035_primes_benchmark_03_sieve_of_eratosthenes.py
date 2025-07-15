import time
import math


def sieve_of_eratosthenes(limit):
    '''Return a list of primes up to the limit (inclusive).'''
    sieve = [True] * (limit + 1)
    sieve[0] = False
    sieve[1] = False

    for number in range(2, int(limit ** 0.5) + 1):
        if sieve[number]:
            for multiple in range(number * number, limit + 1, number):
                sieve[multiple] = False

    primes = [i for i, prime in enumerate(sieve) if prime]
    return primes


def estimate_upper_bound(n):
    '''
    Estimates an upper bound for the nth prime number using
    the approximation: p_n < n * (log n + log log n), for n >= 6.
    For small n, returns a fixed small number.
    '''
    if n < 6:
        return 15
    return int(n * (math.log(n) + math.log(math.log(n)))) + 1


def first_n_primes_with_sieve(n):
    '''
    Generate the first n primes using sieve of Eratosthenes.
    '''
    limit = estimate_upper_bound(n)
    primes = sieve_of_eratosthenes(limit)
    # Sometimes the estimate can be a bit low, so keep increasing limit if needed
    while len(primes) < n:
        limit *= 2
        primes = sieve_of_eratosthenes(limit)
    return primes[:n]


# Benchmark

test_sizes = [10, 100, 1000, 2000, 5000, 10000, 100000, 1000000, 10000000]
execution_times = {}

print('Benchmark: Sieve of Eratosthenes for first n primes\n')

for n in test_sizes:
    print(f'Testing n = {n}...')
    start_time = time.time()
    primes = first_n_primes_with_sieve(n)
    end_time = time.time()
    elapsed = end_time - start_time
    execution_times[n] = elapsed
    print(f'  Execution time: {elapsed:.4f} seconds\n')

print('Summary of execution times:\n')
for n in test_sizes:
    print(f'  n = {n:<5} --> {execution_times[n]:.4f} seconds')
