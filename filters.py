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
