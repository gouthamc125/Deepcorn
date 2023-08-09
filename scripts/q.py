import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\16.jpg')

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for yellow color in HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Create a mask for yellow color
mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# Apply the mask to the original image
yellow_image = cv2.bitwise_and(image, image, mask=mask)

# Display the yellow color image
cv2.imshow('Yellow Color Image', yellow_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
