import cv2
import numpy as np

def detect_color_kernels(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper thresholds for yellow color
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])

    # Define the lower and upper thresholds for red color
    red_lower1 = np.array([0, 100, 100])
    red_upper1 = np.array([10, 255, 255])
    red_lower2 = np.array([160, 100, 100])
    red_upper2 = np.array([179, 255, 255])

    # Create masks for yellow and red color ranges
    yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    red_mask1 = cv2.inRange(hsv_image, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv_image, red_lower2, red_upper2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    # Apply the masks to the original image
    yellow_result = cv2.bitwise_and(image, image, mask=yellow_mask)
    red_result = cv2.bitwise_and(image, image, mask=red_mask)

    # Count the number of yellow and red color kernels
    yellow_count = np.count_nonzero(yellow_result)
    red_count = np.count_nonzero(red_result)

    # Display the number of yellow and red color kernels
    print("Number of yellow color kernels:", yellow_count)
    print("Number of red color kernels:", red_count)

# Example usage
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\test5.jpg'
detect_color_kernels(image_path)
