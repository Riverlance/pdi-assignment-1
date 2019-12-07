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
input_image = Image.open('lena.png')
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


# 2. ... (to do)


# 3. Negative filter

# RGB negative filter
_r, _g, _b = filters.rgb_negative_filter(r, g, b)
print('> RGB with negative filter:\n\t({0}, {1}, {2})'.format(_r, _g, _b))

# Y negative filter
_y, _i, _q = filters.y_negative_filter(y), i_, q
_r, _g, _b = filters.yiq_to_rgb(_y, _i, _q)
print('> Y with negative filter:\n\t({0}, {1}, {2}) -> It is RGB value ({3}, {4}, {5})'.format(_y, _i, _q, _r, _g, _b))

print()


# 4. Multiplying brightness control


# Multiplying brightness from RGB
_r, _g, _b = filters.rgb_set_brightness(r, g, b, brightness)
print('Multiplying brightness from RGB:\n\t({0}, {1}, {2})'.format(_r, _g, _b))

# Multiplying brightness from Y
_y, _i, _q = filters.y_set_brightness(y, brightness), i_, q
print('Multiplying brightness from Y:\n\t({0}, {1}, {2})'.format(_y, _i, _q))


# Generate output images


'''
# Monochromatic in R
monochromatic_r_filter_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_monochromatic_r_filter(monochromatic_r_filter_matrix)  # Apply filter
Image.fromarray(monochromatic_r_filter_matrix.astype('uint8')).save('lena_monochromatic_r.png')  # Save output
'''

'''
# Monochromatic in G
monochromatic_g_filter_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_monochromatic_g_filter(monochromatic_g_filter_matrix)  # Apply filter
Image.fromarray(monochromatic_g_filter_matrix.astype('uint8')).save('lena_monochromatic_g.png')  # Save output
'''

'''
# Monochromatic in B
monochromatic_b_filter_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_monochromatic_b_filter(monochromatic_b_filter_matrix)  # Apply filter
Image.fromarray(monochromatic_b_filter_matrix.astype('uint8')).save('lena_monochromatic_b.png')  # Save output
'''

'''
# Colored in R
colored_r_filter_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_colored_r_filter(colored_r_filter_matrix)  # Apply filter
Image.fromarray(colored_r_filter_matrix.astype('uint8')).save('lena_colored_r.png')  # Save output
'''

'''
# Colored in G
colored_g_filter_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_colored_g_filter(colored_g_filter_matrix)  # Apply filter
Image.fromarray(colored_g_filter_matrix.astype('uint8')).save('lena_colored_g.png')  # Save output
'''

'''
# Colored in B
colored_b_filter_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_colored_b_filter(colored_b_filter_matrix)  # Apply filter
Image.fromarray(colored_b_filter_matrix.astype('uint8')).save('lena_colored_b.png')  # Save output
'''

'''
# RGB negative filter
rgb_negative_filter_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_rgb_negative_filter(rgb_negative_filter_matrix)  # Apply filter
Image.fromarray(rgb_negative_filter_matrix.astype('uint8')).save('lena_negative_rgb.png')  # Save output
'''

'''
# Y negative filter
y_negative_filter_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_y_negative_filter(y_negative_filter_matrix)  # Apply filter
Image.fromarray(y_negative_filter_matrix.astype('uint8')).save('lena_negative_yiq.png')  # Save output
'''

'''
# RGB brightness filter
rgb_brightness_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_rgb_set_brightness(rgb_brightness_matrix, brightness)  # Apply filter
Image.fromarray(rgb_brightness_matrix.astype('uint8')).save('lena_brightness_rgb.png')  # Save output
'''

'''
# Y brightness filter
y_brightness_matrix = numpy.copy(rgb_matrix)  # Copy original matrix
filters.apply_rgb_set_brightness(y_brightness_matrix, brightness)  # Apply filter
Image.fromarray(y_brightness_matrix.astype('uint8')).save('lena_brightness_yiq.png')  # Save output
'''
