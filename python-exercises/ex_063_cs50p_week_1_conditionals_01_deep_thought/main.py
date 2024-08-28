'''
Deep Thought
“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You’re really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

— The Hitchhiker’s Guide to the Galaxy, Douglas Adams

In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

Hints
No need to convert the user’s input to an int if you check for equality with "42", a str, rather than 42, an int!
It’s okay if your output or the user’s wraps onto multiple lines.
'''


def main():
    print('What is the Answer to the Great Question of Life, the Universe, and Everything?')
    user_answer = input()
    print(check_user_answer(user_answer))


def check_user_answer(user_answer):
    right_answers = ('42', 'forty-two', 'forty two')
    user_answer = ' '.join(user_answer.lower().split())
    if user_answer in right_answers:
        return 'Yes'
    else:
        return 'No'


main()


# Test:
print(check_user_answer('42') == 'Yes')
print(check_user_answer('  42  ') == 'Yes')
print(check_user_answer('Forty Two') == 'Yes')
print(check_user_answer('forty-two') == 'Yes')
print(check_user_answer('50') == 'No')
