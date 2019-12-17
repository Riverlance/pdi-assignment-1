import filter.core


def rgb_negative_filter(r, g, b):
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return r, g, b


def y_negative_filter(y):
    y = 255 - y
    return y


def apply_rgb_negative_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = rgb_negative_filter(r, g, b)
    filter.core.on_pixel(matrix, callback)


def apply_r_negative_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = (255 - r, g, b)
    filter.core.on_pixel(matrix, callback)


def apply_g_negative_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = (r, 255 - g, b)
    filter.core.on_pixel(matrix, callback)


def apply_b_negative_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = (r, g, 255 - b)
    filter.core.on_pixel(matrix, callback)


def apply_y_negative_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        y, i_, q = filter.core.rgb_to_yiq(r, g, b)
        _matrix[j, i] = filter.core.yiq_to_rgb(y_negative_filter(y), i_, q)
    filter.core.on_pixel(matrix, callback)


def apply_iq_negative_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        y, i_, q = filter.core.rgb_to_yiq(r, g, b)
        _matrix[j, i] = filter.core.yiq_to_rgb(y, -i_, -q)
    filter.core.on_pixel(matrix, callback)


def apply_i_negative_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        y, i_, q = filter.core.rgb_to_yiq(r, g, b)
        _matrix[j, i] = filter.core.yiq_to_rgb(y, -i_, q)
    filter.core.on_pixel(matrix, callback)


def apply_q_negative_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        y, i_, q = filter.core.rgb_to_yiq(r, g, b)
        _matrix[j, i] = filter.core.yiq_to_rgb(y, i_, -q)
    filter.core.on_pixel(matrix, callback)
