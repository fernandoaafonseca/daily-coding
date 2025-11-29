'''
The code below prints the numbers from 1 to 50. Rewrite the code using a while loop to accomplish the same thing.

    for i in range(1, 51):
        print(i)
'''


LOWER_BOUND = 1
HIGHER_BOUND = 50


def main() -> None:
    current_num = LOWER_BOUND
    while current_num <= HIGHER_BOUND:
        print(current_num)
        current_num += 1


if __name__ == '__main__':
    main()