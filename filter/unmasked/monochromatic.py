import filter.core


def apply_monochromatic_r_filter(matrix):
    def callback(_matrix, x, y):
        r = _matrix[y, x][0]
        _matrix[y, x] = r, 0, 0
    return filter.core.on_pixel(matrix, callback)


def apply_monochromatic_g_filter(matrix):
    def callback(_matrix, x, y):
        g = _matrix[y, x][1]
        _matrix[y, x] = 0, g, 0
    return filter.core.on_pixel(matrix, callback)


def apply_monochromatic_b_filter(matrix):
    def callback(_matrix, x, y):
        b = _matrix[y, x][2]
        _matrix[y, x] = 0, 0, b
    return filter.core.on_pixel(matrix, callback)
