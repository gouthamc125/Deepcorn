# Import the necessary libraries
import cv2
import numpy as np

# Load the image of the plant
image = cv2.imread(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\single.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Apply a Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Define the lower and upper bounds for yellow color in HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
# Create a mask for yellow color
mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# Apply the mask to the original image
yellow_image = cv2.bitwise_and(image, image, mask=mask)

# Apply adaptive thresholding to segment the image
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

# Apply a threshold to the grayscale image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over each contour and draw a bounding rectangle around it
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a counter to keep track of the number of kernels
kernel_count = 0

# Iterate over the contours and count the kernels
for contour in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(contour)
    
    # If the area is within a certain range, consider it as a kernel
    if area > 100 and area < 1000:
        kernel_count += 1

def measure_image_dimensions(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    dpi = 93  # assuming a standard screen DPI

    # Convert pixels to centimeters
    height_cm = height / dpi * 2.54
    width_cm = width / dpi * 2.54

    print(f"The image dimensions are: {height_cm:.2f} cm x {width_cm:.2f} cm")


# Example usage
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\single.jpg'
measure_image_dimensions(image_path)

# Display the number of kernels
print(f"Number of kernels: {kernel_count}")

# Display the image with the bounding rectangles
cv2.imshow('Plant Seeds', image)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow("Corn Image", image)
cv2.imshow('Yellow Color Image', yellow_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
