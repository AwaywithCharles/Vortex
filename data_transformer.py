"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""
import os
import numpy as np
from PIL import Image
from torchvision import transforms

# Set the input and output directories for the transformed data
input_dir = '/path/to/input/data/'
output_dir = '/path/to/output/data/'

# Create the output directory if it does not already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the transformation pipeline for your art generator model
transform_pipeline = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Transform the preprocessed data and save it to the output directory
for label in os.listdir(input_dir):
    # Create the category directory in the output directory if it does not already exist
    if not os.path.exists(os.path.join(output_dir, label)):
        os.makedirs(os.path.join(output_dir, label))
    
    # Transform each image in the category directory
    for file in os.listdir(os.path.join(input_dir, label)):
        # Load the preprocessed image as a PIL Image object
        image = Image.open(os.path.join(input_dir, label, file))
        
        # Apply the transformation pipeline to the image
        image = transform_pipeline(image)
        
        # Save the transformed image to the output directory
        np.save(os.path.join(output_dir, label, file.replace('.jpg', '.npy')), image)
