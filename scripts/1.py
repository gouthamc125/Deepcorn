#kernels count
import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\18.jpg')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for yellow color in HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Threshold the image to get only yellow pixels
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Find contours of the yellow regions
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 255), 2)

# Display the count of seeds
seed_count = len(contours)
print(f"Number of kernels: {seed_count}")

# Display the image with detected seeds
cv2.imshow("Seeds", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
