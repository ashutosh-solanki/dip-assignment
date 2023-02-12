from google.colab.patches import cv2_imshow
import cv2
import numpy as np

# Load the grayscale image
img = cv2.imread("lena_color (1).tif", cv2.IMREAD_GRAYSCALE)
planes = [np.zeros(img.shape, np.uint8) for i in range(8)]
# Perform bit plane slicing
while True:
  print("1.Show bit plane images")
  print("2.Show assigned images")
  ch =int(input("##Enter choice"))

  if ch==1:
    for i in range(8):
      planes[i] = (img & (1 << i))

    for i in range(8):
      cv2_imshow(planes[i])

  elif ch==2:
# Display all bit planes
# Reconstruct and display the image using specified bit planes
    img_reconstructed_a = cv2.bitwise_or(planes[7], planes[6])
    cv2_imshow(img_reconstructed_a)

    img_reconstructed_b = cv2.bitwise_or(img_reconstructed_a, planes[5])
    cv2_imshow(img_reconstructed_b)

    img_reconstructed_c = cv2.bitwise_or(img_reconstructed_b, planes[4])
    cv2_imshow(img_reconstructed_c)

cv2.waitKey(0)
cv2.destroyAllWindows()
