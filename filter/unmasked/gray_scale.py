import filter.core


def apply_gray_scale_r_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = r, r, r
    filter.core.on_pixel(matrix, callback)


def apply_gray_scale_g_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = g, g, g
    filter.core.on_pixel(matrix, callback)


def apply_gray_scale_b_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = b, b, b
    filter.core.on_pixel(matrix, callback)


def apply_gray_scale_y_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        y, i_, q = filter.core.rgb_to_yiq(r, g, b)
        _matrix[j, i] = filter.core.yiq_to_rgb(y, 0, 0)
    filter.core.on_pixel(matrix, callback)
