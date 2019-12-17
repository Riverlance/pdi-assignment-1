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
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        _matrix[y, x] = rgb_negative_filter(r, g, b)
    return filter.core.on_pixel(matrix, callback)


def apply_r_negative_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        _matrix[y, x] = (255 - r, g, b)
    return filter.core.on_pixel(matrix, callback)


def apply_g_negative_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        _matrix[y, x] = (r, 255 - g, b)
    return filter.core.on_pixel(matrix, callback)


def apply_b_negative_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        _matrix[y, x] = (r, g, 255 - b)
    return filter.core.on_pixel(matrix, callback)


def apply_y_negative_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)
        _matrix[y, x] = filter.core.yiq_to_rgb(y_negative_filter(y_), i_, q_)
    return filter.core.on_pixel(matrix, callback)


def apply_iq_negative_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)
        _matrix[y, x] = filter.core.yiq_to_rgb(y_, -i_, -q_)
    return filter.core.on_pixel(matrix, callback)


def apply_i_negative_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)
        _matrix[y, x] = filter.core.yiq_to_rgb(y_, -i_, q_)
    return filter.core.on_pixel(matrix, callback)


def apply_q_negative_filter(matrix):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)
        _matrix[y, x] = filter.core.yiq_to_rgb(y_, i_, -q_)
    return filter.core.on_pixel(matrix, callback)
