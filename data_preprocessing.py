"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import os
import cv2
import numpy as np

# Set the input and output directories for the preprocessed data
input_dir = '/path/to/input/data/'
output_dir = '/path/to/output/data/'

# Create the output directory if it does not already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Preprocess the input data and save it to the output directory
for label in os.listdir(input_dir):
    # Create the category directory in the output directory if it does not already exist
    if not os.path.exists(os.path.join(output_dir, label)):
        os.makedirs(os.path.join(output_dir, label))
    
    # Preprocess each image in the category directory
    for file in os.listdir(os.path.join(input_dir, label)):
        # Load the image and resize it to a fixed size (e.g. 256x256)
        image = cv2.imread(os.path.join(input_dir, label, file))
        image = cv2.resize(image, (256, 256))
        
        # Normalize the pixel values to the range [0, 1]
        image = image.astype(np.float32) / 255.0
        
        # Save the preprocessed image to the output directory
        cv2.imwrite(os.path.join(output_dir, label, file), image)
