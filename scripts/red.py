#Red color
import cv2
import numpy as np

def find_red_kernels(image):
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for orange color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    # Threshold the image to get only yellow pixels
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    
    # Apply morphological operations to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    
    # Find contours of yellow kernels
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Display the number of orange kernels
    num_kernels = len(contours)
    print(f"Number of red kernels: {num_kernels}")
    
    # Draw contours on the original image
    image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 255, 255), 2)
    
    # Display the output image
    cv2.imshow("Red Kernels", image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load the image
image = cv2.imread(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\20.png')

# Find red kernels in the image
find_red_kernels(image)
