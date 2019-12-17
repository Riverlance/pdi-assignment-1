import filter.core


def apply_colored_r_filter(matrix, intensity=255):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        _matrix[y, x] = intensity, g, b
    return filter.core.on_pixel(matrix, callback)


def apply_colored_g_filter(matrix, intensity=255):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        _matrix[y, x] = r, intensity, b
    return filter.core.on_pixel(matrix, callback)


def apply_colored_b_filter(matrix, intensity=255):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        _matrix[y, x] = r, g, intensity
    return filter.core.on_pixel(matrix, callback)
