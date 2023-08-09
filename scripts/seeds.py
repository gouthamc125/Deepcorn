import cv2

# Load the corn image
image = cv2.imread(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\single.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding to segment the image
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

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

# Display the number of kernels
print(f"Number of kernels: {kernel_count}")

# Display the image with contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow("Corn Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
