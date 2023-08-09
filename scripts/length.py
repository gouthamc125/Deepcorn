import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_color_palette(image_path, num_colors):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels
    pixels = image_rgb.reshape(-1, 3)

    # Perform k-means clustering to extract the dominant colors
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(pixels.astype(np.float32), num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert the centers to integers
    colors = centers.astype(np.uint8)

    return colors

def display_color_gradient(colors):
    # Create a gradient image using the extracted colors
    gradient = np.zeros((100, len(colors), 3), dtype=np.uint8)
    for i, color in enumerate(colors):
        gradient[:, i, :] = color

    # Display the gradient image
    plt.imshow(gradient)
    plt.axis('off')
    plt.show()

# Path to the image file
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\4.jpg'

# Number of colors to extract
num_colors = 4

# Extract the color palette
colors = extract_color_palette(image_path, num_colors)

# Display the color gradient
display_color_gradient(colors)
