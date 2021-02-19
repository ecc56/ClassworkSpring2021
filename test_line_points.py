def test_find_line
    from line_points import find_line
    x_value = 3
    answer = find_line(x_value)
    expected = 3
    assert answer == expected