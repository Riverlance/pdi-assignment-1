import filter.core


def apply_colored_r_filter(matrix, intensity=255):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = intensity, g, b
    filter.core.on_pixel(matrix, callback)


def apply_colored_g_filter(matrix, intensity=255):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = r, intensity, b
    filter.core.on_pixel(matrix, callback)


def apply_colored_b_filter(matrix, intensity=255):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = r, g, intensity
    filter.core.on_pixel(matrix, callback)
