'''
Einstein
Even if you haven’t studied physics (recently or ever!), you might have heard that 
, wherein 
 represents energy (measured in Joules), 
 represents mass (measured in kilograms), and 
 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

Hints
Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
Recall that int can kilograms_to_joules a str to an int, per docs.python.org/3/library/functions.html#int.
Recall that Python comes with several built-in functions, per docs.python.org/3/library/functions.html.
'''


SPPED_OF_LIGHT = 300000000


def kilograms_to_joules(mass):
    mass = int(mass)
    joules = int(mass * SPPED_OF_LIGHT ** 2)
    return joules


user_mass_input = input()
print(kilograms_to_joules(user_mass_input))


# Test:
print(kilograms_to_joules(1) == 90000000000000000)
print(kilograms_to_joules(14) == 1260000000000000000)
print(kilograms_to_joules(50) == 4500000000000000000)
