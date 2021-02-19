def test_find_line():
    from line_points import find_line
    x1 = 1
    y1 = 2
    x2 = 2
    y2 = 3
    x_value = 7
    answer = find_line(x1, y1, x2, y2, x_value)
    expected = 8
    assert answer == expected
