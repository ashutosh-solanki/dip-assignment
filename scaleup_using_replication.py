import cv2
import numpy as np

# Load the image
img = cv2.imread('lena_color.tif')

# Scaling Up using Replication
replication_scaling_up = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)


# Create a window for display
window_name = 'Scaling'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

# Show the images in the window
cv2.imshow(window_name, replication_scaling_up)
cv2.waitKey(0)


cv2.destroyAllWindows()


