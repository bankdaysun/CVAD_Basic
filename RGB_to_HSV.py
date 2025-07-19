import numpy as np
import cv2

def rgb_to_hsv_range(r, g, b, h_margin=10, s_margin=100, v_margin=100):
    color_bgr = np.uint8([[[b, g, r]]])
    hsv_color = cv2.cvtColor(color_bgr, cv2.COLOR_BGR2HSV)[0][0]

    h, s, v = hsv_color
    print(f"HSV center: {h}, {s}, {v}")
    lower = np.array([max(h - h_margin, 0),
                      max(s - s_margin, 0),
                      max(v - v_margin, 0)])

    upper = np.array([min(h + h_margin, 179),
                      min(s + s_margin, 255),
                      min(v + v_margin, 255)])

    return lower, upper

r, g, b = 255, 0, 0

lower_hsv, upper_hsv = rgb_to_hsv_range(r, g, b)
print("Lower HSV:", lower_hsv)
print("Upper HSV:", upper_hsv)
