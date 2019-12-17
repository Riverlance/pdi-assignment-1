import filter.core


def apply_monochromatic_r_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = r, 0, 0
    filter.core.on_pixel(matrix, callback)


def apply_monochromatic_g_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = 0, g, 0
    filter.core.on_pixel(matrix, callback)


def apply_monochromatic_b_filter(matrix):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = 0, 0, b
    filter.core.on_pixel(matrix, callback)
