from bank import value


def main() -> None:
    test_value()


def test_value() -> None:
    assert value('Hello, Newman') == 0
    assert value('Hey') == 20
    assert value('How you doing?') == 20
    assert value('What\'s happening?') == 100
    assert value('What\'s up?') == 100
    assert value('How\'s it going?') == 20


if __name__ == '__main__':
    main()