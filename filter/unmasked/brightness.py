import filter.core


def rgb_set_brightness(r, g, b, brightness):
    r = max(0, min(r * brightness, 255))
    g = max(0, min(g * brightness, 255))
    b = max(0, min(b * brightness, 255))
    return r, g, b


def y_set_brightness(y, brightness):
    y = max(0, min(y * brightness, 255))
    return y


def apply_rgb_brightness_filter(matrix, brightness):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        _matrix[j, i] = rgb_set_brightness(r, g, b, brightness)
    filter.core.on_pixel(matrix, callback)


def apply_y_brightness_filter(matrix, brightness):
    def callback(_matrix, i, j):
        r, g, b = _matrix[j, i]
        y, i_, q = filter.core.rgb_to_yiq(r, g, b)
        _matrix[j, i] = filter.core.yiq_to_rgb(y_set_brightness(y, brightness), i_, q)
    filter.core.on_pixel(matrix, callback)
