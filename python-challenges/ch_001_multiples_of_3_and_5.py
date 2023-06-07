'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.
'''


def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum


test_cases = [
    (4, 3), (6, 8), (16, 60), (3, 0), (5, 3), (15, 45), (0, 0), (-1, 0),
    (10, 23), (20, 78), (200, 9168)
]

for input, result in test_cases:
    func_result = solution(input)
    if result == func_result:
        print('Correct answer!')
    else:
        print('Incorrect answer!')
