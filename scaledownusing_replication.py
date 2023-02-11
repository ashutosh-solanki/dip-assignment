import cv2
import numpy as np

# Load the image
img = cv2.imread('lena_color.tif')

replication_scaling_down = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_NEAREST)


window_name = 'Scaling'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)






cv2.imshow(window_name, replication_scaling_down)
cv2.waitKey(0)


cv2.destroyAllWindows()