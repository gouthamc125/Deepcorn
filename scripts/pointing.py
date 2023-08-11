#Mapping of the kernels
import cv2

# Load the image
image = cv2.imread(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\14.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours of the kernels
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display the number of kernels
num_kernels = len(contours)
print(f"Number of kernels: {num_kernels}")

# Display the image with contours
cv2.imshow("Corn Kernels", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
