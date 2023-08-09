import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_color_palette(image_path, num_colors):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels
    pixels = image_rgb.reshape(-1, 3)

    # Perform k-means clustering to find the dominant colors
    _, labels, centers = cv2.kmeans(pixels.astype(np.float32), num_colors, None, criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2), attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)

    # Convert the centers to integers
    centers = np.uint8(centers)

    # Create a color palette using the dominant colors
    palette = centers[labels.flatten()]

    # Reshape the palette to match the original image shape
    palette = palette.reshape(image_rgb.shape)

    # Display the color palette
    plt.imshow(palette)
    plt.axis('off')
    plt.show()

# Example usage
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\4.jpg'
num_colors = 4
find_color_palette(image_path, num_colors)
