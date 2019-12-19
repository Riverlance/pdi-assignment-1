# On terminal, you should use:
# pip install Pillow


from PIL import Image
import numpy

import filter.core

import filter.unmasked.gray_scale
import filter.unmasked.monochromatic
import filter.unmasked.colored
import filter.unmasked.negative
import filter.unmasked.brightness
import filter.unmasked.threshold
import filter.unmasked.sub_sampling
import filter.unmasked.equalization_expansion

import filter.masked.sobel
import filter.masked.median
import filter.masked.most_common


# Initial data
print('>> Initial data')
r, g, b = 50, 150, 250
print('> RGB:\n\t({0}, {1}, {2})'.format(r, g, b))
y_, i_, q_ = 131.5, -91.8, 10.1  # YIQ value of RGB(50, 150, 250)
print('> YIQ:\n\t({0}, {1}, {2})'.format(y_, i_, q_))
brightness_factor = 1.5  # 0 to 2
brightness_offset = 100  # -255 to 255
print('> Brightness:\n\tFactor: {0}%%\n\tOffset: {1}'.format(brightness_factor * 100, brightness_offset))

# Input image
input_image = Image.open('_lena.png')
width, height = input_image.size
print('> Opened image from path \'{0}\' (width = {1}, height = {2})'.format(input_image.fp.name, width, height))

rgb_channels_size = 3  # 3 because means RGB. Do not change this!

# Generate a matrix filled with 0 value
# float, so we can work with YIQ
rgb_matrix = numpy.zeros((height, width, rgb_channels_size), 'float32')

for y in range(height):
    for x in range(width):
        # print(x, y)
        pixel = input_image.getpixel((x, y))
        rgb_matrix[y, x] = numpy.array([pixel[0], pixel[1], pixel[2]])  # (r, g, b)

print()


# 1. Convert RGB to YIQ; convert YIQ to RGB

# From RGB to YIQ
_y, _i, _q = filter.core.rgb_to_yiq(r, g, b)
print('> From RGB to YIQ:\n\t({0}, {1}, {2}) -> Same YIQ initial value'.format(_y, _i, _q))

# From YIQ to RGB
_r, _g, _b = filter.core.yiq_to_rgb(_y, _i, _q)
print('> From YIQ to RGB:\n\t({0}, {1}, {2}) -> Same RGB initial value'.format(_r, _g, _b))

print()


# 2. Gray scale, monochromatic and colored in R, G or B

'''
# Gray scale in RGB
gray_scale_matrix = numpy.copy(rgb_matrix)
gray_scale_matrix = filter.unmasked.gray_scale.apply_gray_scale_rgb_filter(gray_scale_matrix)
Image.fromarray(gray_scale_matrix.astype('uint8')).save('results/gray_scale_rgb.png')
'''

'''
# Gray scale in R
gray_scale_matrix = numpy.copy(rgb_matrix)
gray_scale_matrix = filter.unmasked.gray_scale.apply_gray_scale_r_filter(gray_scale_matrix)
Image.fromarray(gray_scale_matrix.astype('uint8')).save('results/gray_scale_r.png')
'''

'''
# Gray scale in G
gray_scale_matrix = numpy.copy(rgb_matrix)
gray_scale_matrix = filter.unmasked.gray_scale.apply_gray_scale_g_filter(gray_scale_matrix)
Image.fromarray(gray_scale_matrix.astype('uint8')).save('results/gray_scale_g.png')
'''

'''
# Gray scale in B
gray_scale_matrix = numpy.copy(rgb_matrix)
gray_scale_matrix = filter.unmasked.gray_scale.apply_gray_scale_b_filter(gray_scale_matrix)
Image.fromarray(gray_scale_matrix.astype('uint8')).save('results/gray_scale_b.png')
'''

'''
# Gray scale in Y
gray_scale_matrix = numpy.copy(rgb_matrix)
gray_scale_matrix = filter.unmasked.gray_scale.apply_gray_scale_y_filter(gray_scale_matrix)
Image.fromarray(gray_scale_matrix.astype('uint8')).save('results/gray_scale_y.png')
'''

'''
# Monochromatic in R
monochromatic_r_matrix = numpy.copy(rgb_matrix)
monochromatic_r_matrix = filter.unmasked.monochromatic.apply_monochromatic_r_filter(monochromatic_r_matrix)
Image.fromarray(monochromatic_r_matrix.astype('uint8')).save('results/monochromatic_r.png')
'''

'''
# Monochromatic in G
monochromatic_g_matrix = numpy.copy(rgb_matrix)
monochromatic_g_matrix = filter.unmasked.monochromatic.apply_monochromatic_g_filter(monochromatic_g_matrix)
Image.fromarray(monochromatic_g_matrix.astype('uint8')).save('results/monochromatic_g.png')
'''

'''
# Monochromatic in B
monochromatic_b_matrix = numpy.copy(rgb_matrix)
monochromatic_b_matrix = filter.unmasked.monochromatic.apply_monochromatic_b_filter(monochromatic_b_matrix)
Image.fromarray(monochromatic_b_matrix.astype('uint8')).save('results/monochromatic_b.png')
'''

'''
# Colored in R
colored_r_matrix = numpy.copy(rgb_matrix)
colored_r_matrix = filter.unmasked.colored.apply_colored_r_filter(colored_r_matrix)
Image.fromarray(colored_r_matrix.astype('uint8')).save('results/colored_r.png')
'''

'''
# Colored in G
colored_g_matrix = numpy.copy(rgb_matrix)
colored_g_matrix = filter.unmasked.colored.apply_colored_g_filter(colored_g_matrix)
Image.fromarray(colored_g_matrix.astype('uint8')).save('results/colored_g.png')
'''

'''
# Colored in B
colored_b_matrix = numpy.copy(rgb_matrix)
colored_b_matrix = filter.unmasked.colored.apply_colored_b_filter(colored_b_matrix)
Image.fromarray(colored_b_matrix.astype('uint8')).save('results/colored_b.png')
'''


# 3. Negative filter

'''
# RGB negative filter
rgb_negative_matrix = numpy.copy(rgb_matrix)
rgb_negative_matrix = filter.unmasked.negative.apply_rgb_negative_filter(rgb_negative_matrix)
Image.fromarray(rgb_negative_matrix.astype('uint8')).save('results/negative_rgb.png')
'''

'''
# R negative filter
rgb_negative_matrix = numpy.copy(rgb_matrix)
rgb_negative_matrix = filter.unmasked.negative.apply_r_negative_filter(rgb_negative_matrix)
Image.fromarray(rgb_negative_matrix.astype('uint8')).save('results/negative_r.png')
'''

'''
# G negative filter
rgb_negative_matrix = numpy.copy(rgb_matrix)
rgb_negative_matrix = filter.unmasked.negative.apply_g_negative_filter(rgb_negative_matrix)
Image.fromarray(rgb_negative_matrix.astype('uint8')).save('results/negative_g.png')
'''

'''
# B negative filter
rgb_negative_matrix = numpy.copy(rgb_matrix)
rgb_negative_matrix = filter.unmasked.negative.apply_b_negative_filter(rgb_negative_matrix)
Image.fromarray(rgb_negative_matrix.astype('uint8')).save('results/negative_b.png')
'''

'''
# Y negative filter
y_negative_matrix = numpy.copy(rgb_matrix)
y_negative_matrix = filter.unmasked.negative.apply_y_negative_filter(y_negative_matrix)
Image.fromarray(y_negative_matrix.astype('uint8')).save('results/negative_yiq.png')
'''

'''
# IQ negative filter
y_negative_matrix = numpy.copy(rgb_matrix)
y_negative_matrix = filter.unmasked.negative.apply_iq_negative_filter(y_negative_matrix)
Image.fromarray(y_negative_matrix.astype('uint8')).save('results/negative_iq.png')
'''

'''
# I negative filter
y_negative_matrix = numpy.copy(rgb_matrix)
y_negative_matrix = filter.unmasked.negative.apply_i_negative_filter(y_negative_matrix)
Image.fromarray(y_negative_matrix.astype('uint8')).save('results/negative_i.png')
'''

'''
# Q negative filter
y_negative_matrix = numpy.copy(rgb_matrix)
y_negative_matrix = filter.unmasked.negative.apply_q_negative_filter(y_negative_matrix)
Image.fromarray(y_negative_matrix.astype('uint8')).save('results/negative_q.png')
'''


# 4. Multiplying brightness control

'''
# RGB brightness by factor filter
brightness_matrix = numpy.copy(rgb_matrix)
brightness_matrix = filter.unmasked.brightness.apply_rgb_brightness_factor_filter(brightness_matrix, brightness_factor)
Image.fromarray(brightness_matrix.astype('uint8')).save('results/brightness_factor_rgb.png')
'''

'''
# Y brightness by factor filter
brightness_matrix = numpy.copy(rgb_matrix)
brightness_matrix = filter.unmasked.brightness.apply_y_brightness_factor_filter(brightness_matrix, brightness_factor)
Image.fromarray(brightness_matrix.astype('uint8')).save('results/brightness_factor_yiq.png')
'''

'''
# RGB brightness by offset filter
brightness_matrix = numpy.copy(rgb_matrix)
brightness_matrix = filter.unmasked.brightness.apply_rgb_brightness_offset_filter(brightness_matrix, brightness_offset)
Image.fromarray(brightness_matrix.astype('uint8')).save('results/brightness_offset_rgb.png')
'''

'''
# Y brightness by offset filter
brightness_matrix = numpy.copy(rgb_matrix)
brightness_matrix = filter.unmasked.brightness.apply_y_brightness_offset_filter(brightness_matrix, brightness_offset)
Image.fromarray(brightness_matrix.astype('uint8')).save('results/brightness_offset_yiq.png')
'''


# 5. M x N mask convolution - Average filter, Sobel filter

'''
# Average filter (3x3)
average_matrix = numpy.copy(rgb_matrix)
average_matrix = filter.core.on_mask_pixel(average_matrix,
                                           'masks/average_3x3.txt',
                                           filter.core.default_on_mask_values,
                                           rgb_channels_size)
Image.fromarray(average_matrix.astype('uint8')).save('results/average_3x3.png')
'''

'''
# Average filter (5x5)
average_matrix = numpy.copy(rgb_matrix)
average_matrix = filter.core.on_mask_pixel(average_matrix,
                                           'masks/average_5x5.txt',
                                           filter.core.default_on_mask_values,
                                           rgb_channels_size)
Image.fromarray(average_matrix.astype('uint8')).save('results/average_5x5.png')
'''

'''
# Sobel filter (horizontal and vertical)
sobel_matrix = numpy.copy(rgb_matrix)
sobel_matrix = filter.masked.sobel.apply_sobel_filter(sobel_matrix, None, rgb_channels_size)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel.png')
# Sobel filter (horizontal and vertical + negative)
sobel_matrix = filter.unmasked.negative.apply_rgb_negative_filter(sobel_matrix)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel_negative.png')
# Sobel filter (horizontal and vertical + negative + y gray scale)
sobel_matrix = filter.unmasked.gray_scale.apply_gray_scale_y_filter(sobel_matrix)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel_negative_gray_scale_y.png')
'''

'''
# Sobel filter (horizontal)
sobel_matrix = numpy.copy(rgb_matrix)
sobel_matrix = filter.masked.sobel.apply_sobel_filter(sobel_matrix, 0, rgb_channels_size)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel_horizontal.png')
# Sobel filter (horizontal + negative)
sobel_matrix = filter.unmasked.negative.apply_rgb_negative_filter(sobel_matrix)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel_horizontal_negative.png')
# Sobel filter (horizontal + negative + y gray scale)
sobel_matrix = filter.unmasked.gray_scale.apply_gray_scale_y_filter(sobel_matrix)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel_horizontal_negative_gray_scale_y.png')
'''

'''
# Sobel filter (vertical)
sobel_matrix = numpy.copy(rgb_matrix)
sobel_matrix = filter.masked.sobel.apply_sobel_filter(sobel_matrix, 1, rgb_channels_size)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel_vertical.png')
# Sobel filter (vertical + negative)
sobel_matrix = filter.unmasked.negative.apply_rgb_negative_filter(sobel_matrix)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel_vertical_negative.png')
# Sobel filter (horizontal + negative + y gray scale)
sobel_matrix = filter.unmasked.gray_scale.apply_gray_scale_y_filter(sobel_matrix)
Image.fromarray(sobel_matrix.astype('uint8')).save('results/sobel_vertical_negative_gray_scale_y.png')
'''


# 6. M x N mask convolution - Median filter, Common filter

'''
# Median filter in R (3x3)
median_r_matrix = numpy.copy(rgb_matrix)
median_r_matrix = filter.masked.median.apply_median_r_filter(median_r_matrix, 'masks/3x3.txt', rgb_channels_size)
Image.fromarray(median_r_matrix.astype('uint8')).save('results/median_3x3_r.png')
'''

'''
# Median filter in R (5x5)
median_r_matrix = numpy.copy(rgb_matrix)
median_r_matrix = filter.masked.median.apply_median_r_filter(median_r_matrix, 'masks/5x5.txt', rgb_channels_size)
Image.fromarray(median_r_matrix.astype('uint8')).save('results/median_5x5_r.png')
'''

'''
# Median filter in G (3x3)
median_g_matrix = numpy.copy(rgb_matrix)
median_g_matrix = filter.masked.median.apply_median_g_filter(median_g_matrix, 'masks/3x3.txt', rgb_channels_size)
Image.fromarray(median_g_matrix.astype('uint8')).save('results/median_3x3_g.png')
'''

'''
# Median filter in G (5x5)
median_g_matrix = numpy.copy(rgb_matrix)
median_g_matrix = filter.masked.median.apply_median_g_filter(median_g_matrix, 'masks/5x5.txt', rgb_channels_size)
Image.fromarray(median_g_matrix.astype('uint8')).save('results/median_5x5_g.png')
'''

'''
# Median filter in B (3x3)
median_b_matrix = numpy.copy(rgb_matrix)
median_b_matrix = filter.masked.median.apply_median_b_filter(median_b_matrix, 'masks/3x3.txt', rgb_channels_size)
Image.fromarray(median_b_matrix.astype('uint8')).save('results/median_3x3_b.png')
'''

'''
# Median filter in B (5x5)
median_b_matrix = numpy.copy(rgb_matrix)
median_b_matrix = filter.masked.median.apply_median_b_filter(median_b_matrix, 'masks/5x5.txt', rgb_channels_size)
Image.fromarray(median_b_matrix.astype('uint8')).save('results/median_5x5_b.png')
'''

'''
# Most common filter in R (3x3)
most_common_r_matrix = numpy.copy(rgb_matrix)
most_common_r_matrix = filter.masked.most_common.apply_most_common_r_filter(most_common_r_matrix,
                                                                            'masks/3x3.txt',
                                                                            rgb_channels_size)
Image.fromarray(most_common_r_matrix.astype('uint8')).save('results/most_common_3x3_r.png')
'''

'''
# Most common filter in R (5x5)
most_common_r_matrix = numpy.copy(rgb_matrix)
most_common_r_matrix = filter.masked.most_common.apply_most_common_r_filter(most_common_r_matrix,
                                                                            'masks/5x5.txt',
                                                                            rgb_channels_size)
Image.fromarray(most_common_r_matrix.astype('uint8')).save('results/most_common_5x5_r.png')
'''

'''
# Most common filter in G (3x3)
most_common_g_matrix = numpy.copy(rgb_matrix)
most_common_g_matrix = filter.masked.most_common.apply_most_common_g_filter(most_common_g_matrix,
                                                                            'masks/3x3.txt',
                                                                            rgb_channels_size)
Image.fromarray(most_common_g_matrix.astype('uint8')).save('results/most_common_3x3_g.png')
'''

'''
# Most common filter in G (5x5)
most_common_g_matrix = numpy.copy(rgb_matrix)
most_common_g_matrix = filter.masked.most_common.apply_most_common_g_filter(most_common_g_matrix,
                                                                            'masks/5x5.txt',
                                                                            rgb_channels_size)
Image.fromarray(most_common_g_matrix.astype('uint8')).save('results/most_common_5x5_g.png')
'''

'''
# Most common filter in B (3x3)
most_common_b_matrix = numpy.copy(rgb_matrix)
most_common_b_matrix = filter.masked.most_common.apply_most_common_b_filter(most_common_b_matrix,
                                                                            'masks/3x3.txt',
                                                                            rgb_channels_size)
Image.fromarray(most_common_b_matrix.astype('uint8')).save('results/most_common_3x3_b.png')
'''

'''
# Most common filter in B (5x5)
most_common_b_matrix = numpy.copy(rgb_matrix)
most_common_b_matrix = filter.masked.most_common.apply_most_common_b_filter(most_common_b_matrix,
                                                                            'masks/5x5.txt',
                                                                            rgb_channels_size)
Image.fromarray(most_common_b_matrix.astype('uint8')).save('results/most_common_5x5_b.png')
'''


# 7. M x N mask convolution - Gaussian filter

'''
# Gaussian filter (3x3)
gaussian_matrix = numpy.copy(rgb_matrix)
gaussian_matrix = filter.core.on_mask_pixel(gaussian_matrix,
                                            'masks/gaussian_3x3.txt',
                                            filter.core.default_on_mask_values,
                                            rgb_channels_size)
Image.fromarray(gaussian_matrix.astype('uint8')).save('results/gaussian_3x3.png')
'''

'''
# Gaussian filter (3x3)
gaussian_matrix = numpy.copy(rgb_matrix)
gaussian_matrix = filter.core.on_mask_pixel(gaussian_matrix,
                                            'masks/gaussian_5x5.txt',
                                            filter.core.default_on_mask_values,
                                            rgb_channels_size)
Image.fromarray(gaussian_matrix.astype('uint8')).save('results/gaussian_5x5.png')
'''


# 8. Threshold filter, Sharpen filter, Sub Sampling (mosaic)

'''
# Threshold in RGB
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_rgb_filter(threshold_matrix, 127)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_rgb.png')
'''

'''
# Leveled threshold in RGB
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_rgb_filter(threshold_matrix, 4)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_rgb_4.png')
'''

'''
# Leveled threshold in RGB
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_rgb_filter(threshold_matrix, 8)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_rgb_8.png')
'''

'''
# Leveled threshold in RGB
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_rgb_filter(threshold_matrix, 16)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_rgb_16.png')
'''

'''
# Leveled threshold in RGB
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_rgb_filter(threshold_matrix, 32)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_rgb_32.png')
'''

'''
# Leveled threshold in RGB
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_rgb_filter(threshold_matrix, 64)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_rgb_64.png')
'''

'''
# Leveled threshold in RGB
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_rgb_filter(threshold_matrix, 128)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_rgb_128.png')
'''

'''
# Leveled threshold in RGB
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_rgb_filter(threshold_matrix, 256)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_rgb_256.png')
'''

'''
# Threshold in Y
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_y_filter(threshold_matrix, 127)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_yiq.png')
'''

'''
# Leveled threshold in Y
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_y_filter(threshold_matrix, 4)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_yiq_4.png')
'''

'''
# Leveled threshold in Y
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_y_filter(threshold_matrix, 8)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_yiq_8.png')
'''

'''
# Leveled threshold in Y
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_y_filter(threshold_matrix, 16)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_yiq_16.png')
'''

'''
# Leveled threshold in Y
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_y_filter(threshold_matrix, 32)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_yiq_32.png')
'''

'''
# Leveled threshold in Y
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_y_filter(threshold_matrix, 64)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_yiq_64.png')
'''

'''
# Leveled threshold in Y
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_y_filter(threshold_matrix, 128)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_yiq_128.png')
'''

'''
# Leveled threshold in Y
threshold_matrix = numpy.copy(rgb_matrix)
threshold_matrix = filter.unmasked.threshold.apply_threshold_levels_y_filter(threshold_matrix, 256)
Image.fromarray(threshold_matrix.astype('uint8')).save('results/threshold_leveled_yiq_256.png')
'''

'''
# Sharpen filter (11x11)
sharpen_matrix = numpy.copy(rgb_matrix)
sharpen_matrix = filter.core.on_mask_pixel(sharpen_matrix,
                                           'masks/sharpen_11x11.txt',
                                           filter.core.default_on_mask_values,
                                           rgb_channels_size)
Image.fromarray(sharpen_matrix.astype('uint8')).save('results/sharpen.png')
'''

'''
# Sub Sampling (mosaic, 5x5)
sub_sampling_matrix = numpy.copy(rgb_matrix)
sub_sampling_matrix = filter.unmasked.sub_sampling.apply_sub_sampling_filter(sub_sampling_matrix, 5)
Image.fromarray(sub_sampling_matrix.astype('uint8')).save('results/sub_sampling_5x5.png')
'''

'''
# Sub Sampling (mosaic, 10x20)
sub_sampling_matrix = numpy.copy(rgb_matrix)
sub_sampling_matrix = filter.unmasked.sub_sampling.apply_sub_sampling_filter(sub_sampling_matrix, 10, 20)
Image.fromarray(sub_sampling_matrix.astype('uint8')).save('results/sub_sampling_10x20.png')
'''

'''
# Sub Sampling (mosaic, 20x20)
sub_sampling_matrix = numpy.copy(rgb_matrix)
sub_sampling_matrix = filter.unmasked.sub_sampling.apply_sub_sampling_filter(sub_sampling_matrix, 20)
Image.fromarray(sub_sampling_matrix.astype('uint8')).save('results/sub_sampling_20x20.png')
'''

# 9. Equalization, Expansion

'''
# RGB Equalization
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_equalization_rgb_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/equalization_rgb.png')

# RGB Expansion
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_expansion_rgb_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/expansion_rgb.png')

# RGB Equalization -> Expansion
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_equalization_rgb_filter(eq_exp_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_expansion_rgb_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/equalization_expansion_rgb.png')
'''

'''
# Y Equalization (keeping chroma)
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_equalization_y_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/equalization_y_chroma.png')

# Y Expansion (keeping chroma)
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_expansion_y_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/expansion_y_chroma.png')

# Y Equalization -> Expansion (keeping chroma)
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_equalization_y_filter(eq_exp_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_expansion_y_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/equalization_expansion_y_chroma.png')
'''

'''
# Y Equalization (no chroma)
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.gray_scale.apply_gray_scale_y_filter(eq_exp_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_equalization_y_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/equalization_y.png')

# Y Expansion (no chroma)
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.gray_scale.apply_gray_scale_y_filter(eq_exp_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_expansion_y_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/expansion_y.png')

# Y Equalization -> Expansion (no chroma)
eq_exp_matrix = numpy.copy(rgb_matrix)
eq_exp_matrix = filter.unmasked.gray_scale.apply_gray_scale_y_filter(eq_exp_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_equalization_y_filter(eq_exp_matrix)
eq_exp_matrix = filter.unmasked.equalization_expansion.apply_expansion_y_filter(eq_exp_matrix)
Image.fromarray(eq_exp_matrix.astype('uint8')).save('results/equalization_expansion_y.png')
'''
