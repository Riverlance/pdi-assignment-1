# On terminal, you should use:
# pip install Pillow


import filters
from PIL import Image
import numpy


# Initial data
print('>> Initial data')
r, g, b = 50, 150, 250
print('> RGB:\n\t({0}, {1}, {2})'.format(r, g, b))
y, i_, q = 131.5, -91.8, 10.1  # YIQ value of RGB(50, 150, 250)
print('> YIQ:\n\t({0}, {1}, {2})'.format(y, i_, q))
brightness = 0.5
print('> Brightness:\n\t{0}'.format(brightness))

# Input image
input_image = Image.open('_lena.png')
width, height = input_image.size
print('> Opened image from path \'{0}\' (width = {1}, height = {2})'.format(input_image.fp.name, width, height))

rgb_channels_size = 3  # 3 because means RGB. Do not change this!

# Generate a matrix filled with 0 value
# float, so we can work with YIQ
rgb_matrix = numpy.zeros((height, width, rgb_channels_size), 'float32')

for i in range(width):
    for j in range(height):
        # print(i, j)
        rgb_matrix[j, i] = input_image.getpixel((i, j))  # (r, g, b)

print()


# 1. Convert RGB to YIQ; convert YIQ to RGB

# From RGB to YIQ
_y, _i, _q = filters.rgb_to_yiq(r, g, b)
print('> From RGB to YIQ:\n\t({0}, {1}, {2}) -> Same YIQ initial value'.format(_y, _i, _q))

# From YIQ to RGB
_r, _g, _b = filters.yiq_to_rgb(_y, _i, _q)
print('> From YIQ to RGB:\n\t({0}, {1}, {2}) -> Same RGB initial value'.format(_r, _g, _b))

print()


# 2. Monochromatic and colored in R, G or B

'''
# Monochromatic in R
monochromatic_r_matrix = numpy.copy(rgb_matrix)
filters.apply_monochromatic_r_filter(monochromatic_r_matrix)
Image.fromarray(monochromatic_r_matrix.astype('uint8')).save('results/monochromatic_r.png')
'''

'''
# Monochromatic in G
monochromatic_g_matrix = numpy.copy(rgb_matrix)
filters.apply_monochromatic_g_filter(monochromatic_g_matrix)
Image.fromarray(monochromatic_g_matrix.astype('uint8')).save('results/monochromatic_g.png')
'''

'''
# Monochromatic in B
monochromatic_b_matrix = numpy.copy(rgb_matrix)
filters.apply_monochromatic_b_filter(monochromatic_b_matrix)
Image.fromarray(monochromatic_b_matrix.astype('uint8')).save('results/monochromatic_b.png')
'''

'''
# Colored in R
colored_r_matrix = numpy.copy(rgb_matrix)
filters.apply_colored_r_filter(colored_r_matrix)
Image.fromarray(colored_r_matrix.astype('uint8')).save('results/colored_r.png')
'''

'''
# Colored in G
colored_g_matrix = numpy.copy(rgb_matrix)
filters.apply_colored_g_filter(colored_g_matrix)
Image.fromarray(colored_g_matrix.astype('uint8')).save('results/colored_g.png')
'''

'''
# Colored in B
colored_b_matrix = numpy.copy(rgb_matrix)
filters.apply_colored_b_filter(colored_b_matrix)
Image.fromarray(colored_b_matrix.astype('uint8')).save('results/colored_b.png')
'''


# 3. Negative filter

# RGB negative filter
_r, _g, _b = filters.rgb_negative_filter(r, g, b)
print('> RGB with negative filter:\n\t({0}, {1}, {2})'.format(_r, _g, _b))

# Y negative filter
_y, _i, _q = filters.y_negative_filter(y), i_, q
_r, _g, _b = filters.yiq_to_rgb(_y, _i, _q)
print('> Y with negative filter:\n\t({0}, {1}, {2}) -> It is RGB value ({3}, {4}, {5})'.format(_y, _i, _q, _r, _g, _b))

print()

'''
# RGB negative filter
rgb_negative_matrix = numpy.copy(rgb_matrix)
filters.apply_rgb_negative_filter(rgb_negative_matrix)
Image.fromarray(rgb_negative_matrix.astype('uint8')).save('results/negative_rgb.png')
'''

'''
# Y negative filter
y_negative_matrix = numpy.copy(rgb_matrix)
filters.apply_y_negative_filter(y_negative_matrix)
Image.fromarray(y_negative_matrix.astype('uint8')).save('results/negative_yiq.png')
'''


# 4. Multiplying brightness control

# Multiplying brightness from RGB
_r, _g, _b = filters.rgb_set_brightness(r, g, b, brightness)
print('Multiplying brightness from RGB:\n\t({0}, {1}, {2})'.format(_r, _g, _b))

# Multiplying brightness from Y
_y, _i, _q = filters.y_set_brightness(y, brightness), i_, q
print('Multiplying brightness from Y:\n\t({0}, {1}, {2})'.format(_y, _i, _q))

'''
# RGB brightness filter
rgb_brightness_matrix = numpy.copy(rgb_matrix)
filters.apply_rgb_brightness_filter(rgb_brightness_matrix, brightness)
Image.fromarray(rgb_brightness_matrix.astype('uint8')).save('results/brightness_rgb.png')
'''

'''
# Y brightness filter
y_brightness_matrix = numpy.copy(rgb_matrix)
filters.apply_y_brightness_filter(y_brightness_matrix, brightness)
Image.fromarray(y_brightness_matrix.astype('uint8')).save('results/brightness_yiq.png')
'''


# 5. M x N mask convolution - Average filter, Sobel filter

'''
# Average filter (3x3 or 5x5)
average_matrix = numpy.copy(rgb_matrix)
average_matrix = filters.apply_average_filter(average_matrix, 'masks/average_3x3.txt', rgb_channels_size)
Image.fromarray(average_matrix.astype('uint8')).save('results/average_3x3.png')
'''


'''
# Sobel filter (mode=0 for horizontal, mode=1 for vertical, or mode=None for both)
sobel_matrix = numpy.copy(rgb_matrix)
sobel_matrix = filters.apply_sobel_filter(sobel_matrix, None, rgb_channels_size)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel.png')
'''


# 6. M x N mask convolution - Median filter, Common filter

'''
# Median filter in R (3x3 or 5x5)
median_r_matrix = numpy.copy(rgb_matrix)
median_r_matrix = filters.apply_median_r_filter(median_r_matrix, 'masks/median_3x3.txt', rgb_channels_size)
Image.fromarray(median_r_matrix.astype('uint8')).save('results/median_3x3_r.png')
'''

'''
# Median filter in G (3x3 or 5x5)
median_g_matrix = numpy.copy(rgb_matrix)
median_g_matrix = filters.apply_median_g_filter(median_g_matrix, 'masks/median_3x3.txt', rgb_channels_size)
Image.fromarray(median_g_matrix.astype('uint8')).save('results/median_3x3_g.png')
'''

'''
# Median filter in B (3x3 or 5x5)
median_b_matrix = numpy.copy(rgb_matrix)
median_b_matrix = filters.apply_median_b_filter(median_b_matrix, 'masks/median_3x3.txt', rgb_channels_size)
Image.fromarray(median_b_matrix.astype('uint8')).save('results/median_3x3_b.png')
'''

'''
# Most common filter in R (3x3 or 5x5)
most_common_r_matrix = numpy.copy(rgb_matrix)
most_common_r_matrix = filters.apply_most_common_r_filter(most_common_r_matrix,
                                                          'masks/most_common_3x3.txt',
                                                          rgb_channels_size)
Image.fromarray(most_common_r_matrix.astype('uint8')).save('results/most_common_3x3_r.png')
'''

'''
# Most common filter in G (3x3 or 5x5)
most_common_g_matrix = numpy.copy(rgb_matrix)
most_common_g_matrix = filters.apply_most_common_g_filter(most_common_g_matrix,
                                                          'masks/most_common_3x3.txt',
                                                          rgb_channels_size)
Image.fromarray(most_common_g_matrix.astype('uint8')).save('results/most_common_3x3_g.png')
'''

'''
# Most common filter in B (3x3 or 5x5)
most_common_b_matrix = numpy.copy(rgb_matrix)
most_common_b_matrix = filters.apply_most_common_b_filter(most_common_b_matrix,
                                                          'masks/most_common_3x3.txt',
                                                          rgb_channels_size)
Image.fromarray(most_common_b_matrix.astype('uint8')).save('results/most_common_3x3_b.png')
'''
