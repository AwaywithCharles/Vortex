"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import os
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import models
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Set the input and output directories for the additional art data and pre-trained model checkpoint
input_dir = '/path/to/input/data/'
output_dir = '/path/to/output/data/'
checkpoint_path = '/path/to/checkpoint/file.pt'

# Define the hyperparameters for your fine-tuning
batch_size = 32
num_epochs = 50
learning_rate = 0.0001

# Define the custom dataset class for your additional art data
class ArtDataset(Dataset):
    def __init__(self, data_dir):
        self.data = []
        for label in os.listdir(data_dir):
            for file in os.listdir(os.path.join(data_dir, label)):
                self.data.append((os.path.join(data_dir, label, file), label))
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        image = np.load(self.data[idx][0])
        label = self.data[idx][1]
        return image, label

# Define the dataloader for your additional art data
dataset = ArtDataset(input_dir)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Load the pre-trained art generator model and modify the output layer for fine-tuning
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, len(os.listdir(output_dir)))
checkpoint = torch.load(checkpoint_path)
model.load_state_dict(checkpoint['model_state_dict'])
model.fc = nn.Linear(model.fc.in_features, len(os.listdir(output_dir)))

# Define the loss function and optimizer for your fine-tuning
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Fine-tune the art generator model and save checkpoints periodically
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(dataloader):
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        if (i+1) % 10 == 0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'
                  .format(epoch+1, num_epochs, i+1, len(dataset)//batch_size, loss.item()))
    
    # Save a checkpoint of the model weights and optimizer state at the end of each epoch
    checkpoint_path = os.path.join(output_dir, 'checkpoint-{}.pt'.format(epoch+1))
    torch.save({
        'epoch': epoch+1,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': loss.item()
    }, checkpoint_path)
