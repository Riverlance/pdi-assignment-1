import filter.core
import math


def apply_sub_sampling_filter(matrix, size_x, size_y=None):
    if size_y is None:
        size_y = size_x

    def callback(_matrix, x, y):
        _x = math.floor(x / size_x) * size_x
        _y = math.floor(y / size_y) * size_y
        r, g, b = _matrix[_y, _x]
        _matrix[y, x] = r, g, b
    return filter.core.on_pixel(matrix, callback)
