import cv2
import numpy as np

def find_gold_kernels(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the gold color in HSV
    lower_gold = np.array([20, 100, 100])
    upper_gold = np.array([30, 255, 255])

    # Create a mask for the gold color
    mask = cv2.inRange(hsv_image, lower_gold, upper_gold)

    # Apply the mask to the original image
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Convert the masked image to grayscale
    gray_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the grayscale image
    _, thresholded_image = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count the number of gold kernels
    num_gold_kernels = len(contours)

    # Display the number of gold kernels
    print(f"Number of gold kernels: {num_gold_kernels}")

    # Draw contours on the original image
    image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 255, 255), 2)

    # Display the output image
    cv2.imshow("gold Kernels", image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the image file
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\11.jpg'

# Call the function to find gold kernels in the image
find_gold_kernels(image_path)
