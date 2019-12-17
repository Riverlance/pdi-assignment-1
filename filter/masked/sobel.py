import filter.core
import numpy


def apply_sobel_filter(original_matrix, mode=None, channels=1):
    def on_mask_values(slice_matrix, mask_matrix, channels=1):  # Like default_on_mask_values, but with abs on result
        ret = numpy.zeros(channels)

        for y in range(slice_matrix.shape[0]):
            for x in range(slice_matrix.shape[1]):
                slice_r, slice_g, slice_b = slice_matrix[y, x]
                mask_r, mask_g, mask_b = mask_matrix[y, x]
                ret = ret[0] + slice_r * mask_r, ret[1] + slice_g * mask_g, ret[2] + slice_b * mask_b

        ret = max(0, min(round(abs(ret[0])), 255)), \
              max(0, min(round(abs(ret[1])), 255)), \
              max(0, min(round(abs(ret[2])), 255))
        return ret

    # Apply Sobel vertical border detection
    vertical = filter.core.on_mask_pixel(original_matrix, 'masks/sobel_vertical.txt', on_mask_values, channels)
    if mode is 1:
        return vertical

    # Apply Sobel horizontal border detection
    horizontal = filter.core.on_mask_pixel(original_matrix, 'masks/sobel_horizontal.txt', on_mask_values, channels)
    if mode is 0:
        return horizontal

    ret = numpy.zeros_like(original_matrix)

    # Sum both, vertical and horizontal
    for y in range(ret.shape[0]):
        for x in range(ret.shape[1]):
            vertical_r, vertical_g, vertical_b = vertical[y, x]
            horizontal_r, horizontal_g, horizontal_b = horizontal[y, x]
            ret[y, x] = max(0, min(vertical_r + horizontal_r, 255)),\
                        max(0, min(vertical_g + horizontal_g, 255)),\
                        max(0, min(vertical_b + horizontal_b, 255))

    return ret
