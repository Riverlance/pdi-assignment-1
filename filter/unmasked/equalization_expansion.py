import filter.core
import math


# s = T(v) =
# = round(((L - 1) / (rows*columns)) * sum(n_l))
# = round((255 / (rows*columns)) * sum(n_l))
def apply_equalization_rgb_filter(matrix):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    r_c = rows*columns
    l_r_c = 255 / r_c

    d = dict()
    _d = dict()

    # Get pixel levels frequency
    for _y in range(matrix.shape[0]):
        for _x in range(matrix.shape[1]):
            r, g, b = matrix[_y, _x]
            c = (r + g + b) / 3

            index = math.floor(c)
            if index in d:
                d[index] += 1
            else:
                d[index] = 1

    # Sum pixel levels frequency
    sum = 0
    d = sorted(d.items(), key=lambda x: x[0])
    for key, value in d:
        _d[key] = value + sum
        sum += value

    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        c = (r + g + b) / 3

        # Get sum value from _d
        _sum = 0
        key = math.floor(c)
        if key in _d:
            _sum = _d[key]

        s = l_r_c * _sum

        _matrix[y, x] = s, s, s
    return filter.core.on_pixel(matrix, callback)


# s = T(v) =
# = round(((L - 1) / (rows*columns)) * sum(n_l))
# = round((255 / (rows*columns)) * sum(n_l))
def apply_equalization_y_filter(matrix):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    r_c = rows*columns
    l_r_c = 255 / r_c

    d = dict()
    _d = dict()

    # Get pixel levels frequency
    for _y in range(matrix.shape[0]):
        for _x in range(matrix.shape[1]):
            r, g, b = matrix[_y, _x]
            y_ = filter.core.rgb_to_yiq(r, g, b)[0]

            index = math.floor(y_)
            if index in d:
                d[index] += 1
            else:
                d[index] = 1

    # Sum pixel levels frequency
    sum = 0
    d = sorted(d.items(), key=lambda x: x[0])
    for key, value in d:
        _d[key] = value + sum
        sum += value

    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)

        # Get sum value from _d
        _sum = 0
        key = math.floor(y_)
        if key in _d:
            _sum = _d[key]

        s = l_r_c * _sum

        _matrix[y, x] = filter.core.yiq_to_rgb(s, i_, q_)
    return filter.core.on_pixel(matrix, callback)


# s = T(v) =
# = round(( (v - v_min) / (v_max - v_min) ) * (L - 1))
# = round(( (v - v_min) / (v_max - v_min) ) * 255)
def apply_expansion_rgb_filter(matrix):
    v_min, v_max = 255, 0

    # Get v_min and v_max
    for _y in range(matrix.shape[0]):
        for _x in range(matrix.shape[1]):
            r, g, b = matrix[_y, _x]
            c = math.floor((r + g + b) / 3)

            if c < v_min:  # Get v_min
                v_min = c
            if c > v_max:  # Get v_max
                v_max = c

    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        c = math.floor((r + g + b) / 3)

        s = ((c - v_min) / (v_max - v_min)) * 255  # v is c

        _matrix[y, x] = s, s, s
    return filter.core.on_pixel(matrix, callback)


# s = T(v) =
# = round(( (v - v_min) / (v_max - v_min) ) * (L - 1))
# = round(( (v - v_min) / (v_max - v_min) ) * 255)
def apply_expansion_y_filter(matrix):
    v_min, v_max = 255, 0

    # Get v_min and v_max
    for _y in range(matrix.shape[0]):
        for _x in range(matrix.shape[1]):
            r, g, b = matrix[_y, _x]
            y_ = filter.core.rgb_to_yiq(r, g, b)[0]

            if y_ < v_min:  # Get v_min
                v_min = y_
            if y_ > v_max:  # Get v_max
                v_max = y_

    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)

        s = ((y_ - v_min) / (v_max - v_min)) * 255  # v is y_

        _matrix[y, x] = filter.core.yiq_to_rgb(s, i_, q_)
    return filter.core.on_pixel(matrix, callback)
