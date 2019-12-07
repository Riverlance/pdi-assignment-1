import filters


# 1. Convert RGB to YIQ; convert YIQ to RGB

# Initial data
print('>> Initial data')
r, g, b = 50, 150, 250
print('RGB:\n\t({0}, {1}, {2})'.format(r, g, b))
y, i, q = 131.5, -91.8, 10.1
print('YIQ:\n\t({0}, {1}, {2})'.format(y, i, q))
print()

# From RGB to YIQ
_y, _i, _q = filters.rgb_to_yiq(r, g, b)
print('From RGB to YIQ:\n\t({0}, {1}, {2})'.format(_y, _i, _q))

# From YIQ to RGB
_r, _g, _b = filters.yiq_to_rgb(_y, _i, _q)
print('From YIQ to RGB:\n\t({0}, {1}, {2}) -> Same RGB initial value'.format(_r, _g, _b))

print()
