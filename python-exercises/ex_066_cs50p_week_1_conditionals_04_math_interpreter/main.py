'''
Math Interpreter
Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split, which separates a str into a sequence of values, all of which can be assigned to variables at once. For instance, if expression is a str like 1 + 1, then

x, y, z = expression.split(" ")
will assign 1 to x, + to y, and 1 to z.
'''


def main():
    user_expression = get_user_expression()
    n1, operator, n2 = format_expression(user_expression)
    result = calculate_operation(n1, operator, n2)
    print(result)


def get_user_expression():
    user_expression = input('Expression: ')

    return user_expression


def format_expression(user_expression):
    raw_n1, operator, raw_n2 = user_expression.split(' ')
    n1 = float(raw_n1)
    n2 = float(raw_n2)

    return n1, operator, n2


def calculate_operation(n1, operator, n2):
    match operator:
        case '+':
            result = n1 + n2
        case '-':
            result = n1 - n2
        case '*':
            result = n1 * n2
        case '/':
            result = n1 / n2

    final_result = round(result, 1)

    return final_result


main()


# Test:
test_n1, test_operator, test_n2 = format_expression('1 + 1')
print(calculate_operation(test_n1, test_operator, test_n2) == 2.0)

test_n1, test_operator, test_n2 = format_expression('2 - 3')
print(calculate_operation(test_n1, test_operator, test_n2) == -1.0)

test_n1, test_operator, test_n2 = format_expression('2 * 2')
print(calculate_operation(test_n1, test_operator, test_n2) == 4.0)

test_n1, test_operator, test_n2 = format_expression('50 / 2')
print(calculate_operation(test_n1, test_operator, test_n2) == 25.0)

test_n1, test_operator, test_n2 = format_expression('4 / 3')
print(calculate_operation(test_n1, test_operator, test_n2) == 1.3)

test_n1, test_operator, test_n2 = format_expression('100 - 1')
print(calculate_operation(test_n1, test_operator, test_n2) == 99.0)

test_n1, test_operator, test_n2 = format_expression('-1 + 100')
print(calculate_operation(test_n1, test_operator, test_n2) == 99.0)
