def print_giant_A(size):
    '''Prints a giant letter A of the given size.'''
    if size < 3:
        print('Size must be at least 3.')
        return

    mid_line = size // 2

    for row in range(size):
        if row == 0:
            # Top of A
            print(' ' * (size - row - 1) + '*')
        elif row == mid_line:
            # Middle bar of A
            print(' ' * (size - row - 1) + '*' + '*' * (2 * row - 1) + '*')
        else:
            # Other rows
            spaces_between = 2 * row - 1
            print(' ' * (size - row - 1) + '*' + ' ' * spaces_between + '*')

# Example usage:
size = int(input('Enter the size of the letter A (minimum 3): '))
print_giant_A(size)
