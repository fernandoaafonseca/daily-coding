'''
Inspired by the video...
Source:
https://www.youtube.com/watch?v=SUcm8xcRyuE


- Explanation:
"The number 6174 is known as Kaprekar's constant after the Indian mathematician D. R. Kaprekar. This number is renowned for the following rule:

    1. Take any four-digit number, using at least two different digits (leading zeros are allowed).

    2. Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.

    3. Subtract the smaller number from the bigger number.

    4. Go back to step 2 and repeat.

The above process, known as Kaprekar's routine, will always reach its fixed point, 6174, in at most 7 iterations.[4] Once 6174 is reached, the process will continue yielding 7641 – 1467 = 6174. For example, choose 1459:

9541 – 1459 = 8082
8820 – 0288 = 8532
8532 – 2358 = 6174
7641 – 1467 = 6174

The only four-digit numbers for which Kaprekar's routine does not reach 6174 are repdigits* such as 1111, which give the result 0000 after a single iteration. All other four-digit numbers eventually reach 6174 if leading zeros are used to keep the number of digits at 4. For numbers with three identical digits and a fourth digit that is one higher or lower (such as 2111), it is essential to treat 3-digit numbers with a leading zero; for example: 2111 – 1112 = 0999; 9990 – 999 = 8991; 9981 – 1899 = 8082; 8820 – 288 = 8532; 8532 – 2358 = 6174.

* repdigits: is a natural number composed of repeated instances of the same digit in a positional number system (often implicitly decimal)."


Explanation took from the Wikipedia article "6174".
Source:
https://en.wikipedia.org/wiki/6174
'''

'''
ascending = "".join(sorted(str(number)))

descending = "".join(sorted(str(number), reverse=True))
'''


# Please enter a positive 4-digit integer, provided that the 4 digits are not the same.


# steps_to_reach_6174 = 0


def main():
    pass


def get_number():
    while True:
        try:
            # Try to convert the user input to an integer
            num = int(input(
                'Please enter a positive 4-digit integer, provided that the 4 digits are not the same: '))
        except ValueError:
            # If the input is not an integer
            print('Erro!')
        else:
            # If it passes the "try" clausule
            if check_number(num):
                break

    return num


def separate_digits(num):
    # Separate the digits into a list
    digits = [int(digit) for digit in str(num)]

    return digits


def test_repdigit(digits):
    '''
    In recreational mathematics, a repdigit or sometimes monodigit is a natural number composed of repeated instances of the same digit in a positional number system. The word is a portmanteau of repeated and digit. Examples are 11, 666, 4444, and 999999.
    '''
    if digits < 0:
        return False
    if digits == 0:
        return True
    return len(set(str(digits))) == 1


x = int(input('Oi! Digite: '))

print(test_repdigit(x))

'''
n = check_number(x)
print(check_number(n))
'''


def gen_ascending_num(num):
    pass


def gen_descending_num(num):
    pass


def final_test(num):
    steps = 0
    subtraction = 0

    while subtraction != 6174:
        digits = separate_digits(num)

        while len(digits) < 4:
            # append() : append the element to the end of the list.
            # insert() : inserts the element before the given index.
            # Insert a leading 0 until the list has 4 digits
            digits.insert(0, 0)

        # Order the digits of the number from the smallest to the largest
        digits_in_ascending_order = gen_ascending_num(num)

        # Order the digits of the number from the largest to the smallest
        digits_in_descending_order = gen_descending_num(num)

        subtraction = digits_in_descending_order - digits_in_ascending_order

        steps += 1
    print(f'{digits_in_descending_order:04d} - {digits_in_ascending_order:04d} = {subtraction:04d}')

    # test_repdigit(digits)
    # if digit


# Transformar os numeros em sequencia de digitos.

# Ordernar os digitos de forma crescente.
# num_in_increasing_order_of_digits = int(''.join(map(str, sorted(digits))))
    pass

# Ordenar os digitos de forma decrescente.
# input_in_decreasing_order

# Subtrair os numeros decrescente.

# Checar se é igual a 6174


'''
if __name__ == '__main__':
    main()
'''


# Test
# 5235
# 6532 - 2356 = 4176

# No máximo 7 etapas (steps)!

# 7641 - 1467 = 6174
