from simple_calculator import add, subtract, multiply, divide, square


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.5, 0.25) == 0.75


def test_subtract() -> None:
    assert subtract(5, 2) == 3
    assert subtract(0, 5) == -5
    assert subtract(1.5, 0.5) == 1.0


def test_multiply() -> None:
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6


def test_divide() -> None:
    assert divide(10, 2) == 5
    assert divide(3, 2) == 1.5

    try:
        divide(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False


def test_square() -> None:
    assert square(4) == 16
    assert square(-3) == 9
    assert square(1.5) == 2.25