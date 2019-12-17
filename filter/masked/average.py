import filter.core


def apply_average_filter(original_matrix, mask_path, channels=1):
    return filter.core.on_mask_pixel(original_matrix, mask_path, filter.core.default_on_mask_values, channels)
