import numpy
import os
import math


def on_pixel(matrix, callback):
    height = matrix.shape[0]
    width = matrix.shape[1]
    for i in range(width):
        for j in range(height):
            callback(matrix, i, j)


# Additional use when on_mask_pixel is used
# Multiply each value of slice to mask and return the sum (domestic product)
def default_on_mask_values(slice_matrix, mask_matrix, channels=1):
    ret = numpy.zeros(channels)

    for i in range(slice_matrix.shape[0]):
        for j in range(slice_matrix.shape[1]):
            slice_r, slice_g, slice_b = slice_matrix[i, j]
            mask_r, mask_g, mask_b = mask_matrix[i, j]
            ret = ret[0] + slice_r * mask_r, ret[1] + slice_g * mask_g, ret[2] + slice_b * mask_b

    ret = max(0, min(round(ret[0]), 255)),\
          max(0, min(round(ret[1]), 255)),\
          max(0, min(round(ret[2]), 255))
    return ret


def on_mask_pixel(original_matrix, mask_path, on_mask_values, channels=1):
    # Mask
    if not os.path.isfile(mask_path):
        print('> Mask file not found at path \'{0}\''.format(mask_path))
        return None
    mask_matrix, pivot_pos = get_mask(mask_path, channels)
    mask_matrix = get_flipped_hv(mask_matrix)  # Converting from correlation to convolution

    expanded_matrix = get_expanded_matrix(original_matrix, mask_matrix, pivot_pos, channels)
    matrix = numpy.zeros((expanded_matrix.shape[0], expanded_matrix.shape[1], channels))  # Expanded, but with zeros

    margin_top = pivot_pos[0] - 1
    margin_bottom = mask_matrix.shape[0] - pivot_pos[0]
    margin_left = pivot_pos[1] - 1
    margin_right = mask_matrix.shape[1] - pivot_pos[1]

    # Each pixel based on its position
    initial_margin_top = int(margin_top)
    initial_margin_left = int(margin_left)
    slice_matrix = numpy.zeros_like(mask_matrix)
    for i in range(initial_margin_top, int(expanded_matrix.shape[0] - margin_bottom)):
        for j in range(initial_margin_left, int(expanded_matrix.shape[1] - margin_right)):
            # Each pixel based on mask position

            margin_i = i - initial_margin_top
            margin_j = j - initial_margin_left
            for _i in range(mask_matrix.shape[0]):
                for _j in range(mask_matrix.shape[1]):
                    # Each pixel based on mask position

                    mask_margin_i = margin_i + _i
                    mask_margin_j = margin_j + _j
                    slice_matrix[_i, _j] = expanded_matrix[mask_margin_i, mask_margin_j]  # Get slice area of matrix

            # Get pixel according to on_mask_values callback
            pixel = on_mask_values(slice_matrix, mask_matrix, channels)

            matrix[i, j] = pixel

    matrix = get_matrix(matrix, mask_matrix, pivot_pos)
    return matrix


# Flip horizontally and then vertically
def get_flipped_hv(matrix):
    return numpy.flipud(numpy.fliplr(matrix))  # Convert correlation <-> convolution


# Get mask from file
def get_mask(mask_path, channels=1):
    mask = []
    pivot_pos = [0, 0]

    line_count = 0
    if os.path.isfile(mask_path):
        with open(mask_path) as file:
            for line in file:
                line_count += 1

                line = line.rstrip()  # Clear spaces
                values = line.split(',')  # Split line values
                _values = numpy.zeros(len(values))

                for key in range(len(values)):
                    _values[key] = float(values[key])  # Convert each value to float

                    # Get pivot position from file (at first line)
                    if line_count == 1:
                        pivot_pos[key] = max(.0, _values[key])

                # Get mask from file (at lines 2+)
                if line_count > 1:
                    mask.append(_values)

    mask = numpy.array(mask)

    # Convert from 1 channel to 'channels' count
    # Eg, if channels=3, it will convert the mask shape channel from 1 to 3
    mask = numpy.stack((mask,)*channels, axis=-1)  # Keep the comma (without, it would multiply instead concatenate)

    return mask, pivot_pos


def get_expanded_matrix(original_matrix, mask_matrix, pivot_pos, channels=1):
    # New zeros matrix with original matrix size + (mask size - 1)
    expanded_matrix = numpy.zeros((original_matrix.shape[0] + (mask_matrix.shape[0] - 1),  # Rows
                                   original_matrix.shape[1] + (mask_matrix.shape[1] - 1),  # Columns
                                   channels))

    # Relocated original matrix according to pivot offsets
    mask_offset_x = int(pivot_pos[1] - 1)
    mask_offset_y = int(pivot_pos[0] - 1)
    expanded_matrix[mask_offset_y:mask_offset_y + original_matrix.shape[0],
                    mask_offset_x:mask_offset_x + original_matrix.shape[1]] = original_matrix

    return expanded_matrix


def get_matrix(expanded_matrix, mask_matrix, pivot_pos):
    rows = expanded_matrix.shape[0]
    columns = expanded_matrix.shape[1]

    margin_top = pivot_pos[0] - 1
    margin_bottom = mask_matrix.shape[0] - pivot_pos[0]
    margin_left = pivot_pos[1] - 1
    margin_right = mask_matrix.shape[1] - pivot_pos[1]

    if margin_right > 0:
        expanded_matrix = numpy.delete(expanded_matrix, [columns - margin_right, columns - 1], axis=1)
    if margin_left > 0:
        expanded_matrix = numpy.delete(expanded_matrix, [0, margin_left - 1], axis=1)
    if margin_bottom > 0:
        expanded_matrix = numpy.delete(expanded_matrix, [rows - margin_bottom, rows - 1], axis=0)
    if margin_top > 0:
        expanded_matrix = numpy.delete(expanded_matrix, [0, margin_top - 1], axis=0)

    return expanded_matrix


# 1. Convert RGB to YIQ; convert YIQ to RGB

def rgb_to_yiq(r, g, b):
    # Y - Luminance, perceived intensity or brightness
    # Range is 0 (0.299*0 + 0.587*0 + 0.114*0) to 255 (0.299*255 + 0.587*255 + 0.114*255)
    y = max(0, min((299*r + 587*g + 114*b) / 1000, 255))
    # I - Chrominance
    # Range is -151.98 (0.596*0 - 0.274*255 - 0.322*255) to 151.98 (0.596*255 - 0.274*0 - 0.322*0)
    i = max(-151.98, min((596*r - 274*g - 322*b) / 1000, 151.98))
    # Q - Chrominance
    # Range is -133.365 (0.211*0 - 0.523*255 + 0.312*0) to 133,365 (0.211*255 - 0.523*0 + 0.312*255)
    q = max(-133.365, min((211*r - 523*g + 312*b) / 1000, 133.365))
    return y, i, q

# Note: It's dividing by 1000 because Python has a huge decimal precision.
# So, the best is to multiply as an integer value and make it as float after. See the example below:
# print(0.274*100)  # 27.400000000000002
# print((274*100)/1000)  # 27.4


def yiq_to_rgb(y, i, q):
    r = max(0, min(round(y + .956*i + .621*q), 255))  # Red perceived intensity
    g = max(0, min(round(y - .272*i - .647*q), 255))  # Green perceived intensity
    b = max(0, min(round(y - 1.106*i + 1.703*q), 255))  # Blue perceived intensity
    return r, g, b


# 2. Monochromatic and colored in R, G or B

def apply_monochromatic_r_filter(matrix):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        matrix[j, i] = r, 0, 0
    on_pixel(matrix, callback)


def apply_monochromatic_g_filter(matrix):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        matrix[j, i] = 0, g, 0
    on_pixel(matrix, callback)


def apply_monochromatic_b_filter(matrix):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        matrix[j, i] = 0, 0, b
    on_pixel(matrix, callback)


def apply_colored_r_filter(matrix, intensity=255):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        matrix[j, i] = intensity, g, b
    on_pixel(matrix, callback)


def apply_colored_g_filter(matrix, intensity=255):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        matrix[j, i] = r, intensity, b
    on_pixel(matrix, callback)


def apply_colored_b_filter(matrix, intensity=255):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        matrix[j, i] = r, g, intensity
    on_pixel(matrix, callback)


# 3. Negative filter

def rgb_negative_filter(r, g, b):
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return r, g, b


def y_negative_filter(y):
    y = 255 - y
    return y


def apply_rgb_negative_filter(matrix):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        matrix[j, i] = rgb_negative_filter(r, g, b)
    on_pixel(matrix, callback)


def apply_y_negative_filter(matrix):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        y, i_, q = rgb_to_yiq(r, g, b)
        matrix[j, i] = yiq_to_rgb(y_negative_filter(y), i_, q)
    on_pixel(matrix, callback)


# 4. Multiplying brightness control

def rgb_set_brightness(r, g, b, brightness):
    r = max(0, min(r * brightness, 255))
    g = max(0, min(g * brightness, 255))
    b = max(0, min(b * brightness, 255))
    return r, g, b


def y_set_brightness(y, brightness):
    y = max(0, min(y * brightness, 255))
    return y


def apply_rgb_brightness_filter(matrix, brightness):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        matrix[j, i] = rgb_set_brightness(r, g, b, brightness)
    on_pixel(matrix, callback)


def apply_y_brightness_filter(matrix, brightness):
    def callback(matrix, i, j):
        r, g, b = matrix[j, i]
        y, i_, q = rgb_to_yiq(r, g, b)
        matrix[j, i] = yiq_to_rgb(y_set_brightness(y, brightness), i_, q)
    on_pixel(matrix, callback)


# 5. M x N mask convolution - Average filter, Sobel filter

def apply_average_filter(original_matrix, mask_path, channels=1):
    return on_mask_pixel(original_matrix, mask_path, default_on_mask_values, channels)


def apply_sobel_filter(original_matrix, mode=None, channels=1):
    # Apply Sobel vertical border detection
    vertical = on_mask_pixel(original_matrix, 'masks/sobel_vertical.txt', default_on_mask_values, channels)
    if mode is 1:
        return vertical

    # Apply Sobel horizontal border detection
    horizontal = on_mask_pixel(original_matrix, 'masks/sobel_horizontal.txt', default_on_mask_values, channels)
    if mode is 0:
        return horizontal

    ret = numpy.zeros_like(original_matrix)

    # Sum both, vertical and horizontal
    for i in range(ret.shape[0]):
        for j in range(ret.shape[1]):
            vertical_r, vertical_g, vertical_b = vertical[i, j]
            horizontal_r, horizontal_g, horizontal_b = horizontal[i, j]
            ret[i, j] = max(0, min(vertical_r + horizontal_r, 255)),\
                        max(0, min(vertical_g + horizontal_g, 255)),\
                        max(0, min(vertical_b + horizontal_b, 255))

    return ret


# 6. M x N mask convolution - Median filter, Common filter

def apply_median_filter(original_matrix, mask_path, sort_channel, channels=1):
    def on_mask_values(slice_matrix, mask_matrix, channels=1):
        values = []

        for i in range(slice_matrix.shape[0]):
            for j in range(slice_matrix.shape[1]):
                values.append(slice_matrix[i, j])

        def get_key(tuple):
            return tuple[sort_channel]

        values = sorted(values, key=get_key)

        ret = values[math.floor(len(values) / 2)]
        return ret

    return on_mask_pixel(original_matrix, mask_path, on_mask_values, channels)


def apply_median_r_filter(original_matrix, mask_path, channels=1):
    return apply_median_filter(original_matrix, mask_path, 0, channels)  # Sort by red channel


def apply_median_g_filter(original_matrix, mask_path, channels=1):
    return apply_median_filter(original_matrix, mask_path, 1, channels)  # Sort by green channel


def apply_median_b_filter(original_matrix, mask_path, channels=1):
    return apply_median_filter(original_matrix, mask_path, 2, channels)  # Sort by blue channel


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

        for i in range(slice_matrix.shape[0]):
            for j in range(slice_matrix.shape[1]):
                values.append(slice_matrix[i, j])

        most_common_indexes = get_most_common_from_index(values, most_common_channel)
        for index in most_common_indexes:
            ret = ret[0] + values[index][0], ret[1] + values[index][1], ret[2] + values[index][2]

        mask_cells_count = mask_matrix.shape[0] * mask_matrix.shape[1]

        most_common_indexes_size = len(most_common_indexes)
        ret = max(0, min(round(ret[0] / most_common_indexes_size), 255)),\
              max(0, min(round(ret[1] / most_common_indexes_size), 255)),\
              max(0, min(round(ret[2] / most_common_indexes_size), 255))
        return ret

    return on_mask_pixel(original_matrix, mask_path, on_mask_values, channels)


def apply_most_common_r_filter(original_matrix, mask_path, channels=1):
    return apply_most_common_filter(original_matrix, mask_path, 0, channels)


def apply_most_common_g_filter(original_matrix, mask_path, channels=1):
    return apply_most_common_filter(original_matrix, mask_path, 1, channels)


def apply_most_common_b_filter(original_matrix, mask_path, channels=1):
    return apply_most_common_filter(original_matrix, mask_path, 2, channels)
