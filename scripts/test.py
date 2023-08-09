import cv2
import numpy as np

def find_colors(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the color you want to find
    lower_bound = np.array([0, 0, 0])  # Replace with your desired lower bound
    upper_bound = np.array([255, 255, 255])  # Replace with your desired upper bound

    # Create a mask based on the color range
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Apply the mask to the original image
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image and the masked image
    cv2.imshow("Original Image", image)
    cv2.imshow("Masked Image", masked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'image_path' with the path to your image file
find_colors(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\10.jpeg')
