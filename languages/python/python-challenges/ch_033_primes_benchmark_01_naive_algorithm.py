import time


def first_primes(n):
    '''Return the first n prime numbers (very basic implementation).'''
    primes = []
    candidate = 2

    while len(primes) < n:
        is_prime = True
        for i in range(2, candidate):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1

    return primes

# List of values for n to test (expanded)
test_sizes = [10, 100, 1000, 2000, 5000, 10000]
execution_times = {}

print('Benchmark: Naive prime number generator\n')

for n in test_sizes:
    print(f'Testing n = {n}...')
    start_time = time.time()
    primes = first_primes(n)
    end_time = time.time()
    elapsed = end_time - start_time
    execution_times[n] = elapsed
    print(f'  Execution time: {elapsed:.4f} seconds\n')

print('Summary of execution times:\n')
for n in test_sizes:
    print(f'  n = {n:<5} --> {execution_times[n]:.4f} seconds')
