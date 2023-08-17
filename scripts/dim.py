import cv2

def measure_image_dimensions(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    dpi = 96  # assuming a standard screen DPI

    # Convert pixels to centimeters
    height_cm = height / dpi * 2.54
    width_cm = width / dpi * 2.54

    print(f"The image dimensions are: {height_cm:.2f} cm x {width_cm:.2f} cm")

# Example usage
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\test3.jpg'
measure_image_dimensions(image_path)
