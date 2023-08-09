#Counting the Kernels
import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\single.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank image to draw the seeds
seeds = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

# Draw the contours as seeds on the blank image
cv2.drawContours(seeds, contours, -1, (0, 0, 255), 2)

# Display the original image and the seeds
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(seeds, cv2.COLOR_BGR2RGB)), plt.title('Seeds')
plt.show()
