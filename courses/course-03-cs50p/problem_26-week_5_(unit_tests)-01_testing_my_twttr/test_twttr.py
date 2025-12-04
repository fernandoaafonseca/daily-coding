from twttr import shorten


def main() -> None:
    test_twttr()


def test_twttr() -> None:
    assert shorten('Twitter') == 'Twttr'
    assert shorten('What\'s your name?') == 'Wht\'s yr nm?'
    assert shorten('CS50') == 'CS50'
    assert shorten('PYTHON') == 'PYTHN'
    assert shorten('42') == '42'


if __name__ == '__main__':
    main()