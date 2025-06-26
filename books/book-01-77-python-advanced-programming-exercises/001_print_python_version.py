'''
Print the Python version to the console.
'''


import sys


'''
Example:

The "split()" function separates the string into a list, which the default separator is a blank space. So the first element on the list will be the version number:

system.split() => [
    '3.13.5',
    '(tags/v3.13.5:6cb20a2,',
    'Jun',
    '11',
    '2025,',
    16:15:46)',
    '[
        MSC',
        'v.1943',
        '64',
        'bit',
        '(AMD64)
    ]'
        ]
'''
python_version = sys.version.split()[0]

print(f'Your current Python version is: {python_version}')
