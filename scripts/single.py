import os

def get_image_length(image_path):
    try:
        # Check if the file exists
        if os.path.isfile(image_path):
            # Get the size of the image file
            image_size = os.path.getsize(image_path)
            return image_size
        else:
            print("Image file not found.")
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

# Example usage
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\single.jpg'
image_length = get_image_length(image_path)
if image_length is not None:
    print("Image length:", image_length, "bytes")

def convert_bytes_to_cm(length_in_bytes):
    # 1 byte = 0.00001016 centimeters (approximate conversion)
    conversion_factor = 0.00001016
    length_in_cm = length_in_bytes * conversion_factor
    return length_in_cm

# Example usage
image_length_bytes = image_length
image_length_cm = convert_bytes_to_cm(image_length_bytes)
print(f"The length of the image is {image_length_cm} centimeters.")
