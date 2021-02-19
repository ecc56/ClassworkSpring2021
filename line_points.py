def find_line(x1, y1, x2, y2, x_value):
    m = (y2-y1)/(x2-x1)
    y_value = m*(x_value-x1) + y1
    return y_value
    
