import pytest

from fuel import convert, gauge


def test_convert() -> None:
    assert convert('1/3') == 33
    assert convert('2/3') == 67
    assert convert('3/4') == 75
    assert convert('0/100') == 0
    assert convert('1/100') == 1
    assert convert('99/100') == 99
    assert convert('100/100') == 100


def test_convert_zero_division_error() -> None:
    with pytest.raises(ZeroDivisionError):
        convert('100/0')


def test_convert_value_error() -> None:
    with pytest.raises(ValueError):
        convert('10/3')
    with pytest.raises(ValueError):
        convert('-1/3')
    with pytest.raises(ValueError):
        convert('1/-3')
    with pytest.raises(ValueError):
        convert('three/four')
    with pytest.raises(ValueError):
        convert('5-4')
    with pytest.raises(ValueError):
        convert('1.5/4')
    with pytest.raises(ValueError):
        convert('3/5.5')


def test_gauge() -> None:
    assert gauge(round(1 / 3 * 100)) == '33%'
    assert gauge(round(2 / 3 * 100)) == '67%'
    assert gauge(round(3 / 4 * 100)) == '75%'
    assert gauge(round(0 / 100 * 100)) == 'E'
    assert gauge(round(1 / 100 * 100)) == 'E'
    assert gauge(round(99 / 100 * 100)) == 'F'
    assert gauge(round(100 / 100 * 100)) == 'F'