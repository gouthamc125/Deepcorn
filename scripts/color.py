import cv2
import numpy as np

def get_dominant_color(image):
    # Load the image
    img = cv2.imread(image)

    # Convert the image from BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels
    pixels = img_rgb.reshape(-1, 3)

    # Calculate the mean of each channel (R, G, B)
    color = np.mean(pixels, axis=0)

    # Convert the color values from float to integer
    color = color.astype(int)

    return color

# Path to the image file
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\10.jpeg'
# Get the dominant color of the image
dominant_color = get_dominant_color(image_path)

# Print the dominant color
print(f"The dominant color of the image is RGB({dominant_color[0]}, {dominant_color[1]}, {dominant_color[2]})")