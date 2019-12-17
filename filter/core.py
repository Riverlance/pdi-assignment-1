import os
import numpy


'''
    Core
'''


# Note: It's dividing by 1000 because Python has a huge decimal precision.
# So, the best is to multiply as an integer value and make it as float after. See the example below:
# print(0.274*100)  # 27.400000000000002
# print((274*100)/1000)  # 27.4

def rgb_to_yiq(r, g, b):
    # Y - Luminance, perceived intensity or brightness
    # For curiosity:
    # Y range is from 0 (0.299*0 + 0.587*0 + 0.114*0) to 255 (0.299*255 + 0.587*255 + 0.114*255)
    y = (299*r + 587*g + 114*b) / 1000

    # I - Chrominance
    # For curiosity:
    # I range is from -151.98 (0.596*0 - 0.274*255 - 0.322*255) to 151.98 (0.596*255 - 0.274*0 - 0.322*0)
    i = (596*r - 274*g - 322*b) / 1000

    # Q - Chrominance
    # For curiosity:
    # Q range is from -133.365 (0.211*0 - 0.523*255 + 0.312*0) to 133,365 (0.211*255 - 0.523*0 + 0.312*255)
    q = (211*r - 523*g + 312*b) / 1000

    return y, i, q


def yiq_to_rgb(y, i, q):
    # Red perceived intensity
    r = max(0, min(round(y + ((956*i + 621*q) / 1000)), 255))

    # Green perceived intensity
    g = max(0, min(round(y + ((- 272*i - 647*q) / 1000)), 255))

    # Blue perceived intensity
    b = max(0, min(round(y + ((- 1106*i + 1703*q) / 1000)), 255))

    return r, g, b


'''
    Filters without masks
'''


# Callback for filter without mask
def on_pixel(matrix, on_values_callback):
    _matrix = numpy.copy(matrix)

    for y in range(_matrix.shape[0]):
        for x in range(_matrix.shape[1]):
            on_values_callback(_matrix, x, y)

    return _matrix


'''
    Filters with masks
'''


# Get mask from file
def get_mask(mask_path, channels=1):
    mask = []
    pivot_pos = [0, 0]

    line_count = 0
    if os.path.isfile(mask_path):
        with open(mask_path) as file:
            for line in file:
                line_count += 1

                line = line.rstrip()  # Clear side spaces
                values = line.split(',')  # Split line values
                _values = numpy.zeros(len(values))

                for key in range(len(values)):
                    _values[key] = float(values[key])  # Each value as float

                    # Get pivot position from file (at first line)
                    if line_count == 1:
                        pivot_pos[key] = int(max(.0, _values[key]))

                # Get mask from file (at lines 2+)
                if line_count > 1:
                    mask.append(_values)

    mask = numpy.array(mask)

    # Convert from 1 channel to 'channels' count
    # Eg, if channels=3, it will convert the mask shape channel from 1 to 3
    mask = numpy.stack((mask,)*channels, axis=-1)  # Keep the comma (without, it would multiply instead concatenate)

    return mask, pivot_pos


# Flip horizontally and then vertically
# Convert correlation <-> convolution
def get_flipped_hv(mask_matrix, pivot_pos):
    return numpy.flipud(numpy.fliplr(mask_matrix)),\
           [mask_matrix.shape[0] - pivot_pos[0] + 1, mask_matrix.shape[1] - pivot_pos[1] + 1]


# Expand matrix with zeros around and return it
def get_expanded_matrix(matrix, mask_matrix, pivot_pos, channels=1):
    # New zeros matrix with original matrix size + (mask size - 1)
    expanded_matrix = numpy.zeros((matrix.shape[0] + (mask_matrix.shape[0] - 1),  # Rows
                                   matrix.shape[1] + (mask_matrix.shape[1] - 1),  # Columns
                                   channels))

    # Relocated original matrix according to pivot offsets
    mask_offset_x = pivot_pos[1] - 1
    mask_offset_y = pivot_pos[0] - 1
    expanded_matrix[mask_offset_y:mask_offset_y + matrix.shape[0],
                    mask_offset_x:mask_offset_x + matrix.shape[1]] = matrix

    return expanded_matrix


# Remove matrix zeros expansion and return it
# 'matrix' param should be expanded with zeros already
def get_matrix(matrix, mask_matrix, pivot_pos):
    margin_top = pivot_pos[0] - 1
    margin_bottom = mask_matrix.shape[0] - pivot_pos[0]
    margin_left = pivot_pos[1] - 1
    margin_right = mask_matrix.shape[1] - pivot_pos[1]

    # Remove columns from right
    if margin_right > 0:
        matrix = numpy.delete(matrix, [matrix.shape[1] - margin_right, matrix.shape[1] - 1], axis=1)

    # Remove columns from left
    if margin_left > 0:
        matrix = numpy.delete(matrix, [0, margin_left - 1], axis=1)

    # Remove rows from bottom
    if margin_bottom > 0:
        matrix = numpy.delete(matrix, [matrix.shape[0] - margin_bottom, matrix.shape[0] - 1], axis=0)

    # Remove rows from top
    if margin_top > 0:
        matrix = numpy.delete(matrix, [0, margin_top - 1], axis=0)

    return matrix


def on_mask_pixel(original_matrix, mask_path, on_mask_values_callback, channels=1):
    # Get mask and pivot
    if not os.path.isfile(mask_path):
        print('> Mask file not found at path \'{0}\''.format(mask_path))
        return None
    mask_matrix, pivot_pos = get_mask(mask_path, channels)
    # Converting from correlation to convolution
    mask_matrix, pivot_pos = get_flipped_hv(mask_matrix, pivot_pos)

    # Original expanded matrix
    expanded_matrix = get_expanded_matrix(original_matrix, mask_matrix, pivot_pos, channels)
    # Zeros expanded matrix
    output_matrix = numpy.zeros((expanded_matrix.shape[0], expanded_matrix.shape[1], channels))
    # Zeros matrix based on mask size
    slice_matrix = numpy.zeros_like(mask_matrix)

    margin_top = pivot_pos[0] - 1
    margin_bottom = mask_matrix.shape[0] - pivot_pos[0]
    margin_left = pivot_pos[1] - 1
    margin_right = mask_matrix.shape[1] - pivot_pos[1]

    # Each pixel based on its position
    initial_margin_top = margin_top
    initial_margin_left = margin_left

    for y in range(initial_margin_top, int(expanded_matrix.shape[0] - margin_bottom)):
        for x in range(initial_margin_left, int(expanded_matrix.shape[1] - margin_right)):

            # Each pixel based on mask position

            margin_x = x - initial_margin_left
            margin_y = y - initial_margin_top

            for _y in range(mask_matrix.shape[0]):
                for _x in range(mask_matrix.shape[1]):
                    # Each pixel based on mask position

                    mask_margin_x = margin_x + _x
                    mask_margin_y = margin_y + _y

                    # Get slice area of matrix
                    slice_matrix[_y, _x] = expanded_matrix[mask_margin_y, mask_margin_x]

            # Get pixel according to on_mask_values_callback
            output_matrix[y, x] = on_mask_values_callback(slice_matrix, mask_matrix, channels)

    # Remove matrix zeros expansion
    output_matrix = get_matrix(output_matrix, mask_matrix, pivot_pos)

    return output_matrix


# Additional use when on_mask_pixel is used
# Multiply each value of slice to mask and return the sum
def default_on_mask_values(slice_matrix, mask_matrix, channels=1):
    ret = numpy.zeros(channels)

    for y in range(slice_matrix.shape[0]):
        for x in range(slice_matrix.shape[1]):
            slice_r, slice_g, slice_b = slice_matrix[y, x]
            mask_r, mask_g, mask_b = mask_matrix[y, x]
            ret = ret[0] + slice_r * mask_r, ret[1] + slice_g * mask_g, ret[2] + slice_b * mask_b

    ret = max(0, min(round(ret[0]), 255)),\
          max(0, min(round(ret[1]), 255)),\
          max(0, min(round(ret[2]), 255))
    return ret
