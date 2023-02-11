import cv2
import numpy as np

# Load the image
img = cv2.imread('lena_color.tif')


# Scaling Down using Interpolation
interpolation_scaling_down = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# Create a window for display
window_name = 'Scaling'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)




cv2.imshow(window_name, interpolation_scaling_down)
cv2.waitKey(0)

cv2.destroyAllWindows()
