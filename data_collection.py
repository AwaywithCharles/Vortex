"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import os
import shutil
import glob

# Set the input and output directories for the collected data
input_dir = '/path/to/input/data/'
output_dir = '/path/to/output/data/'

# Create the output directory if it does not already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Collect the input data and copy it to the output directory
for file in glob.glob(os.path.join(input_dir, '*.jpg')):
    # Parse the file name to get the category or label
    label = file.split('/')[-1].split('_')[0]
    
    # Create the category directory in the output directory if it does not already exist
    if not os.path.exists(os.path.join(output_dir, label)):
        os.makedirs(os.path.join(output_dir, label))
    
    # Copy the file to the category directory in the output directory
    shutil.copy(file, os.path.join(output_dir, label)
            
