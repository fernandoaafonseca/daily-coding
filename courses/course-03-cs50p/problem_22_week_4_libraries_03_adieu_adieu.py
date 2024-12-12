'''
Adieu, Adieu

Source: https://www.youtube.com/watch?v=Qy9_lfjQopU

In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
 names with 
 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

Hints
Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:
pip install inflect
'''


import inflect


def main():
    names = get_names()
    output_text = generate_output_text(names)
    print(output_text)


def get_names() -> list[str]:
    names = []

    while True:
        try:
            new_name = input('Name: ')
            names.append(new_name)
        except EOFError:
            break

    return names


def generate_output_text(names: list[str]) -> str:
    p = inflect.engine()
    output_names_text = p.join(names)
    return f'Adieu, adieu, to {output_names_text}'


if __name__ == '__main__':
    main()
