import services


def test_single_roman_number_translation():
    assert services.from_roman_to_decimal("I") == 1


def test_asceding_roman_number_translation():
    assert services.from_roman_to_decimal("VII") == 7


def test_desceding_roman_number_translation():
    assert services.from_roman_to_decimal("IX") == 9


def test_ascending_and_desceding_roman_number_translation():
    assert services.from_roman_to_decimal("XCVI") == 96
