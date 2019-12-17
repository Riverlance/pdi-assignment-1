import filter.core
import numbers


def apply_rgb_brightness_factor_filter(matrix, brightness):
    if isinstance(brightness, numbers.Number):
        brightness = [brightness, brightness, brightness]

    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]

        r = max(0, min(round(r * brightness[0]), 255))
        g = max(0, min(round(g * brightness[1]), 255))
        b = max(0, min(round(b * brightness[2]), 255))

        _matrix[y, x] = r, g, b
    return filter.core.on_pixel(matrix, callback)


def apply_y_brightness_factor_filter(matrix, brightness):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)

        y_ = max(0, min(round(y_ * brightness), 255))

        _matrix[y, x] = filter.core.yiq_to_rgb(y_, i_, q_)
    return filter.core.on_pixel(matrix, callback)


def apply_rgb_brightness_offset_filter(matrix, brightness):
    if isinstance(brightness, numbers.Number):
        brightness = [brightness, brightness, brightness]

    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]

        r = max(0, min(round(r + brightness[0]), 255))
        g = max(0, min(round(g + brightness[1]), 255))
        b = max(0, min(round(b + brightness[2]), 255))

        _matrix[y, x] = r, g, b
    return filter.core.on_pixel(matrix, callback)


def apply_y_brightness_offset_filter(matrix, brightness):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_, i_, q_ = filter.core.rgb_to_yiq(r, g, b)

        y_ = max(0, min(round(y_ + brightness), 255))

        _matrix[y, x] = filter.core.yiq_to_rgb(y_, i_, q_)
    return filter.core.on_pixel(matrix, callback)
