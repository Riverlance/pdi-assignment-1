import filter.core
import math


def apply_median_filter(original_matrix, mask_path, sort_channel, channels=1):
    def on_mask_values(slice_matrix, mask_matrix, channels=1):
        values = []

        for y in range(slice_matrix.shape[0]):
            for x in range(slice_matrix.shape[1]):
                values.append(slice_matrix[y, x])

        def get_key(tuple):
            return tuple[sort_channel]

        values = sorted(values, key=get_key)

        ret = values[math.floor(len(values) / 2)]
        return ret

    return filter.core.on_mask_pixel(original_matrix, mask_path, on_mask_values, channels)


def apply_median_r_filter(original_matrix, mask_path, channels=1):
    return apply_median_filter(original_matrix, mask_path, 0, channels)  # Sort by red channel


def apply_median_g_filter(original_matrix, mask_path, channels=1):
    return apply_median_filter(original_matrix, mask_path, 1, channels)  # Sort by green channel


def apply_median_b_filter(original_matrix, mask_path, channels=1):
    return apply_median_filter(original_matrix, mask_path, 2, channels)  # Sort by blue channel
