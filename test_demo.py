import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    [0.1, 0.2, 0.3],
    ])
def test_add(a, b, expected):
    from demo import add
    answer = add(a, b)
    assert answer == pytest.approx(expected)
