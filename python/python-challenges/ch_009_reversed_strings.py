'''
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
'''


def solution(string):
    rev_string = ''.join(reversed(string))
    return rev_string


print(solution('world'))
