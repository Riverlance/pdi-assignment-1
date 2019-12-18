import filter.core


def apply_gray_scale_rgb_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        average = round((r + g + b) / 3)
        _matrix[y, x] = average, average, average
    return filter.core.on_pixel(matrix, callback)


def apply_gray_scale_r_filter(matrix):
    def callback(_matrix, x, y):
        r = _matrix[y, x][0]
        _matrix[y, x] = r, r, r
    return filter.core.on_pixel(matrix, callback)


def apply_gray_scale_g_filter(matrix):
    def callback(_matrix, x, y):
        g = _matrix[y, x][1]
        _matrix[y, x] = g, g, g
    return filter.core.on_pixel(matrix, callback)


def apply_gray_scale_b_filter(matrix):
    def callback(_matrix, x, y):
        b = _matrix[y, x][2]
        _matrix[y, x] = b, b, b
    return filter.core.on_pixel(matrix, callback)


def apply_gray_scale_y_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_ = filter.core.rgb_to_yiq(r, g, b)[0]
        _matrix[y, x] = filter.core.yiq_to_rgb(y_, 0, 0)
    return filter.core.on_pixel(matrix, callback)
