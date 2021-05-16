import pytest

import currency_scrapper


def test_get_currency_data_with_wrong_data_type_fails() -> None:
    """
    Test if get_currency_data fails with non string argument
    """
    import datetime

    input = datetime.datetime.now().date()
    expected_output = "Date is not string"

    with pytest.raises(TypeError) as e:
        assert currency_scrapper.get_currency_data(input)

    assert expected_output in str(e)


def test_get_currency_data_with_wrong_format_fails() -> None:
    """
    Test if get_currency_data fails with wrong format argument
    """
    inputs = [
        "27101981",  # DDMMYYYY
        "10271981",  # MMDDYYYY
        "19812710",  # YYYYDDMM
        "20219901",  # Out of range month
        "20211299",  # Out of range day
    ]
    expected_output = "Incorrect date value or format, use YYYYMMDD"

    for i in inputs:
        with pytest.raises(ValueError) as e:
            assert currency_scrapper.get_currency_data(i)

        assert expected_output in str(e)
