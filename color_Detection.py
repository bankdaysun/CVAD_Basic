import cv2
import numpy as np

img = cv2.imread("test.jpg")
hsv = cv2.cvtColor(img, _)

lower_red = np.array([_, _, _])
upper_red = np.array([_, _, _])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red2 = np.array([_, _, _])
upper_red2 = np.array([_, _, _])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = cv2.bitwise_or(mask1, mask2)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original", img)
cv2.imshow("Red Detected", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
