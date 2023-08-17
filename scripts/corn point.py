# corn point
# Import the required libraries
import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained CNN model
model = tf.keras.models.load_model(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\scripts\sample1.h5')

# Function to detect seeds and point them
def detect_seeds(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Preprocess the image
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    
    # Predict the seeds using the CNN model
    predictions = model.predict(image)
    
    # Get the number of kernels
    num_kernels = np.argmax(predictions)
    
    # Display the output
    print("Number of kernels:", num_kernels)

# Specify the image path
image_path = r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\test1.jpg'

# Call the function to detect seeds and point them
detect_seeds(image_path)
