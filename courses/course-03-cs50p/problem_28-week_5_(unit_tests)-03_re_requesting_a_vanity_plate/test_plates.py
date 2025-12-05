from plates import is_valid


def test_length() -> None:
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False


def test_non_alphanumeric() -> None:
    assert is_valid('PI3.14') == False


def test_first_two_letters() -> None:
    assert is_valid('A5') == False
    assert is_valid('A5BC') == False
    assert is_valid('A0BC') == False
    assert is_valid('AB50') == True


def test_has_any_number_in_first_two_chars() -> None:
    assert is_valid('50CS') == False
    assert is_valid('5CS') == False


def test_begins_with_letter() -> None:
    assert is_valid('7ABC') == False
    assert is_valid('*ABC') == False
    assert is_valid('ABC') == True


def test_first_number_is_zero() -> None:
    assert is_valid('05CS') == False
    assert is_valid('CS05') == False


def test_has_letter_after_a_number() -> None:
    assert is_valid('CS50P') == False
    assert is_valid('CS50P2') == False


def test_valid_plates() -> None:
    assert is_valid('ECTO88') == True
    assert is_valid('NRVOUS') == True
    assert is_valid('CS50') == True