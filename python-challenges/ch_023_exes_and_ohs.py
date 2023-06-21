'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO('ooxx') => true
XO('xooxx') => false
XO('ooxXm') => true
XO('zpzpzpp') => true // when no 'x' and 'o' is present should return true
XO('zzoo') => false
'''


def xo(s):
    x_amount = len(''.join(letter for letter in s if letter.lower() == 'x'))
    o_amount = len(''.join([letter for letter in s if letter.lower() == 'o']))
    return x_amount == o_amount


print((xo('ooxx') == True) == True)
print((xo('xooxx') == False) == True)
print((xo('ooxXm') == True) == True)
print((xo('zpzpzpp') == True) == True)
print((xo('zzoo') == False) == True)
print((xo('oxOx') == True) == True)
print((xo('') == True) == True)
