import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_colors(image_path, num_colors):
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

    # Create the color palette
    palette = np.zeros((50, num_colors, 3), dtype=np.uint8)
    palette[:, :, :] = colors.reshape(1, num_colors, 3)

    return palette

# Path to the image
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\11.jpg'

# Number of colors to extract
num_colors = 5

# Extract the colors and display the color palette
palette = extract_colors(image_path, num_colors)
plt.imshow(palette)
plt.axis('off')
plt.show()
