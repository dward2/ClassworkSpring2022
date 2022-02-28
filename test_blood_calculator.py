# test_blood_calculator.py

import pytest


@pytest.mark.parametrize("input_HDL, expected", [
    [70, "Normal"],
    [20, "Low"]
    ])
def test_check_HDL(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected
