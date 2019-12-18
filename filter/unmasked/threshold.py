import filter.core
import math


def apply_threshold_rgb_filter(matrix, black_level=127):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]

        if r <= black_level or g <= black_level or b <= black_level:
            r, g, b = (0, 0, 0)
        else:
            r, g, b = (255, 255, 255)

        _matrix[y, x] = r, r, r
    return filter.core.on_pixel(matrix, callback)


def apply_threshold_y_filter(matrix, slice_level=127):
    def callback(_matrix, x, y):
        r, g, b = _matrix[y, x]
        y_ = filter.core.rgb_to_yiq(r, g, b)[0]

        if y_ <= slice_level:
            y_ = 0
        else:
            y_ = 255

        _matrix[y, x] = filter.core.yiq_to_rgb(y_, 0, 0)
    return filter.core.on_pixel(matrix, callback)


def apply_threshold_levels_rgb_filter(matrix, gray_levels=2):  # gray_levels is between 2 and 255
    slice_range = math.floor(256 / gray_levels)
    slice_value = math.floor(255 / (gray_levels - 1))

    def callback(_matrix, x, y):

        r, g, b = _matrix[y, x]
        average = round((r + g + b) / 3)

        if slice_range <= 1:
            _matrix[y, x] = average, average, average
            return

        for level in reversed(range(1, gray_levels + 1)):
            slice_range_min = slice_range * (level - 1)
            slice_range_max = slice_range * level

            if level is gray_levels:
                slice_range_max = 255

            if slice_range_min <= r < slice_range_max:
                r = slice_value * (level - 1)
                break

        _matrix[y, x] = r, r, r
    return filter.core.on_pixel(matrix, callback)


def apply_threshold_levels_y_filter(matrix, gray_levels=2):  # gray_levels is between 2 and 255
    slice_range = math.floor(256 / gray_levels)
    slice_value = math.floor(255 / (gray_levels - 1))

    def callback(_matrix, x, y):

        r, g, b = _matrix[y, x]
        y_ = filter.core.rgb_to_yiq(r, g, b)[0]

        if slice_range <= 1:
            _matrix[y, x] = filter.core.yiq_to_rgb(y_, 0, 0)
            return

        for level in reversed(range(1, gray_levels + 1)):
            slice_range_min = slice_range * (level - 1)
            slice_range_max = slice_range * level

            if level is gray_levels:
                slice_range_max = 255

            if slice_range_min <= y_ < slice_range_max:
                y_ = slice_value * (level - 1)
                break

        _matrix[y, x] = filter.core.yiq_to_rgb(y_, 0, 0)
    return filter.core.on_pixel(matrix, callback)
