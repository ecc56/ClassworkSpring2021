
import pytest

@pytest.mark.parametrize("value,expected",[(65,"Normal"),(45,"Borderline Low"),(35,"Low")])


def test_analyze_HDL(value,expected):
    from blood_tests import analyze_HDL
    answer = analyze_HDL(value)
    assert answer == expected
