'''
Frank, Ian and Glen’s Letters

FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

Hints
You can install pyfiglet with:
pip install pyfiglet
The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
from pyfiglet import Figlet

figlet = Figlet()
You can then get a list of available fonts with code like this:

figlet.getFonts()
You can set the font with code like this, wherein f is the font’s name as a str:

figlet.setFont(font=f)
And you can output text in that font with code like this, wherein s is that text as a str:

print(figlet.renderText(s))
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
'''


import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    is_font_random = check_font_arg()
    set_font_name(figlet, is_font_random)
    user_text = get_user_text()
    ascii_text = generate_ascii_text(figlet, user_text)
    print(ascii_text)


def check_font_arg() -> bool:
    if len(sys.argv) == 1:
        is_font_random = True
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        is_font_random = False
    else:
        sys.exit(1)

    return is_font_random


def set_font_name(figlet, is_font_random: bool) -> None:
    # Get a list of available fonts
    available_fonts = figlet.getFonts()
    input_font = sys.argv[2]
    if not is_font_random:
        if input_font in available_fonts:
            figlet.setFont(font=input_font)
        else:
            sys.exit(1)
    else:
        font_name = random.choice(available_fonts)
        figlet.setFont(font=font_name)


def get_user_text() -> str:
    return input()


def generate_ascii_text(figlet, user_text: str) -> str:
    return figlet.renderText(user_text)


if __name__ == '__main__':
    main()
