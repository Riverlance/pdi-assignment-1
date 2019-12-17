import filter.core
import numpy


def get_most_common_from_index(values, index):
    if len(values) < 1:
        return None

    d = dict()

    for key in range(len(values)):
        channel_value = values[key][index]
        if channel_value in d:
            d[channel_value] = (d[channel_value][0] + 1, d[channel_value][1] + (key,))
        else:
            d[channel_value] = (1, (key,))

    most_common_dict_value = None
    for key, value in d.items():
        if most_common_dict_value is not None:
            if value[0] > most_common_dict_value[0]:
                most_common_dict_value = value
        else:
            most_common_dict_value = value

    return most_common_dict_value[1]


def apply_most_common_filter(original_matrix, mask_path, most_common_channel, channels=1):
    def on_mask_values(slice_matrix, mask_matrix, channels=1):
        values = []
        ret = numpy.zeros(channels)

        for y in range(slice_matrix.shape[0]):
            for x in range(slice_matrix.shape[1]):
                values.append(slice_matrix[y, x])

        most_common_indexes = get_most_common_from_index(values, most_common_channel)
        for index in most_common_indexes:
            ret = ret[0] + values[index][0], ret[1] + values[index][1], ret[2] + values[index][2]

        most_common_indexes_size = len(most_common_indexes)
        ret = max(0, min(round(ret[0] / most_common_indexes_size), 255)),\
              max(0, min(round(ret[1] / most_common_indexes_size), 255)),\
              max(0, min(round(ret[2] / most_common_indexes_size), 255))
        return ret

    return filter.core.on_mask_pixel(original_matrix, mask_path, on_mask_values, channels)


def apply_most_common_r_filter(original_matrix, mask_path, channels=1):
    return apply_most_common_filter(original_matrix, mask_path, 0, channels)


def apply_most_common_g_filter(original_matrix, mask_path, channels=1):
    return apply_most_common_filter(original_matrix, mask_path, 1, channels)


def apply_most_common_b_filter(original_matrix, mask_path, channels=1):
    return apply_most_common_filter(original_matrix, mask_path, 2, channels)
