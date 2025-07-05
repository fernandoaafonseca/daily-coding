'''
This summation represents the Basel problem:

  ∞
  ∑  1/n²
 n=1

The sum converges to π²/6.

It is an infinite series, but for practical purposes, it can be approximated by summing the first "x" terms:
1/1² + 1/2² + ... + 1/x² ≈ π²/6

As "x" increases, the sum approaches the exact solution for the infinite series, which is π²/6.

You can approximate the value of π by:
(6 * (1/1² + 1/2² + ... + 1/x²)) ** 0.5 ≈ π
'''
summation = 0


def calc_pi(num_terms):
    '''
    You could use the "math" module to calculate the power and to sum the series.
    You can simply use "sum(1 / n**2 for n in range(1, num_terms))" to achieve this.
    However, I chose to do it the hard way to demonstrate the underlying process.
    While we could rely on "sum()" for convenience, consider how the "sum()" function works behind the scenes: it effectively does what we are doing here!
    '''
    # Declare summation as global to modify it
    global summation

    for n in range(1, num_terms):
        # Accumulate the sum
        summation = summation + 1 / n**2

    '''
    Calculate pi without using the math module.
    You could also use: "approximated_pi = pow(6 * summation, 0.5)".
    But again, what does "pow()" really do? It's effectively the same as "x ** 0.5", which means "x to the power of 0.5".
    '''
    approximated_pi = (6 * summation) ** 0.5

    return approximated_pi


# Variable to define the number of terms to sum
num_terms = 1000000
approximated_pi = calc_pi(num_terms)
print(f"Approximated value of π using {num_terms} terms is: {approximated_pi}")
