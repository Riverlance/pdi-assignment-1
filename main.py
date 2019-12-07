import filters


# 1. Convert RGB to YIQ; convert YIQ to RGB

# Initial data
print('>> Initial data')
r, g, b = 50, 150, 250
print('RGB:\n\t({0}, {1}, {2})'.format(r, g, b))
y, i, q = 131.5, -91.8, 10.1
print('YIQ:\n\t({0}, {1}, {2})'.format(y, i, q))
brightness = 0.7
print('Brightness:\n\t{0}'.format(brightness))
print()

# From RGB to YIQ
_y, _i, _q = filters.rgb_to_yiq(r, g, b)
print('From RGB to YIQ:\n\t({0}, {1}, {2})'.format(_y, _i, _q))

# From YIQ to RGB
_r, _g, _b = filters.yiq_to_rgb(_y, _i, _q)
print('From YIQ to RGB:\n\t({0}, {1}, {2}) -> Same RGB initial value'.format(_r, _g, _b))

print()


# 2. ... (to do)


# 3. Negative filter

# RGB with negative filter
_r, _g, _b = filters.rgb_negative_filter(r, g, b)
print('RGB with negative filter:\n\t({0}, {1}, {2})'.format(_r, _g, _b))

# YIQ with negative filter
_y, _i, _q = filters.yiq_negative_filter(y), i, q
_r, _g, _b = filters.yiq_to_rgb(_y, _i, _q)
print('YIQ with negative filter:\n\t({0}, {1}, {2}) -> It is RGB value ({3}, {4}, {5})'.format(_y, _i, _q, _r, _g, _b))

print()


# 4. Multiplying brightness control

# Multiplying brightness from YIQ
_y, _i, _q = filters.yiq_set_brightness(y, brightness), i, q
print('Multiplying brightness from YIQ:\n\t({0}, {1}, {2})'.format(_y, _i, _q))

# Multiplying brightness from RGB
_r, _g, _b = filters.rgb_set_brightness(r, g, b, brightness)
print('Multiplying brightness from RGB:\n\t({0}, {1}, {2})'.format(_r, _g, _b))
