'''
Find the sum of all numbers that are divisible by 5 or 7 less than 100.

Present the solution in the form of a function called "calculate()". In response, call "calculate()" function and print the result to the console.
'''


def calculate():
    numbers = []
    for i in range(100):
        if i % 5 == 0 or i % 7 == 0:
            numbers.append(i)

    total = sum(numbers)
    print(total)


calculate()
