import filter.core


def rgb_set_brightness(r, g, b, brightness):
    r = max(0, min(round(r * brightness), 255))
    g = max(0, min(round(g * brightness), 255))
    b = max(0, min(round(b * brightness), 255))
    return r, g, b


def y_set_brightness(y, brightness):
    y = max(0, min(round(y * brightness), 255))
    return y


def apply_rgb_brightness_filter(matrix, brightness):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        _matrix[y, x] = rgb_set_brightness(r, g, b, brightness)
    return filter.core.on_pixel(matrix, callback)


def apply_y_brightness_filter(matrix, brightness):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)
        _matrix[y, x] = filter.core.yiq_to_rgb(y_set_brightness(y_, brightness), i_, q_)
    return filter.core.on_pixel(matrix, callback)
