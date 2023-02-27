"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import tkinter as tk
from tkinter import filedialog
from art_generator import generate_art

# Set the default paths for the input and output directories and checkpoint file
default_input_path = '/path/to/input/data/'
default_output_path = '/path/to/output/data/'
default_checkpoint_path = '/path/to/checkpoint/file.pt'

# Define the GUI interface for selecting the input and output directories and checkpoint file
def select_input_path():
    path = filedialog.askdirectory(initialdir=default_input_path, title='Select Input Directory')
    if path:
        input_path_var.set(path)

def select_output_path():
    path = filedialog.askdirectory(initialdir=default_output_path, title='Select Output Directory')
    if path:
        output_path_var.set(path)

def select_checkpoint():
    path = filedialog.askopenfilename(initialdir=default_checkpoint_path, title='Select Checkpoint File')
    if path:
        checkpoint_path_var.set(path)

# Define the wrapper function that ties together all of the previous scripts
def generate_art_wrapper():
    input_dir = input_path_var.get()
    output_dir = output_path_var.get()
    checkpoint_path = checkpoint_path_var.get()
    generate_art(input_dir, output_dir, checkpoint_path)

# Define the main window of the GUI
root = tk.Tk()
root.title('Art Generator')
root.geometry('400x200')
# Define the model architecture selection widget
model_var = tk.StringVar()
model_var.set('ResNet18')
model_label = tk.Label(root, text='Model Architecture:')
model_label.pack()
model_menu = tk.OptionMenu(root, model_var, 'ResNet18', 'VGG16', 'DenseNet121')
model_menu.pack()

# Modify the generate_art() function to use the selected model architecture
def generate_art(input_dir, output_dir, checkpoint_path):
    model_arch = model_var.get()
    if model_arch == 'ResNet18':
        model = models.resnet18(pretrained=False)
    elif model_arch == 'VGG16':
        model = models.vgg16(pretrained=False)
    elif model_arch == 'DenseNet121':
        model = models.densenet121(pretrained=False)

    # Rest of generate_art() function code...


# Define the input and output directory selection widgets
input_path_var = tk.StringVar()
input_path_var.set(default_input_path)
input_path_label = tk.Label(root, text='Input Directory:')
input_path_label.pack()
input_path_entry = tk.Entry(root, textvariable=input_path_var)
input_path_entry.pack()
input_path_button = tk.Button(root, text='Select Directory', command=select_input_path)
input_path_button.pack()

output_path_var = tk.StringVar()
output_path_var.set(default_output_path)
output_path_label = tk.Label(root, text='Output Directory:')
output_path_label.pack()
output_path_entry = tk.Entry(root, textvariable=output_path_var)
output_path_entry.pack()
output_path_button = tk.Button(root, text='Select Directory', command=select_output_path)
output_path_button.pack()

checkpoint_path_var = tk.StringVar()
checkpoint_path_var.set(default_checkpoint_path)
checkpoint_path_label = tk.Label(root, text='Checkpoint File:')
checkpoint_path_label.pack()
checkpoint_path_entry = tk.Entry(root, textvariable=checkpoint_path_var)
checkpoint_path_entry.pack()
checkpoint_path_button = tk.Button(root, text='Select File', command=select_checkpoint)
checkpoint_path_button.pack()

# Define the generate art button
generate_button = tk.Button(root, text='Generate Art', command=generate_art_wrapper)
generate_button.pack()

# Define a progress bar widget
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='indeterminate')

# Define a new generate art wrapper that shows the progress bar during generation
def generate_art_wrapper():
    input_dir = input_path_var.get()
    output_dir = output_path_var.get()
    checkpoint_path = checkpoint_path_var.get()

    progress_bar.pack(side='bottom', fill='x')
    progress_bar.start()

    generate_art(input_dir, output_dir, checkpoint_path)

    progress_bar.stop()
    progress_bar.pack_forget()

# Define a canvas widget for displaying the generated art images
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Modify the generate_art() function to display the generated art images on the canvas
def generate_art(input_dir, output_dir, checkpoint_path):
    # Rest of generate_art() function code...

    # Load the generated art images and display them on the canvas
    for file in os.listdir(output_dir):
        image_path = os.path.join(output_dir, file)
        image = Image.open(image_path)
        image = ImageTk.PhotoImage(image)
        canvas.create_image(150, 150, image=image)

        # Update the canvas to display the new image
        canvas.update()

    # Rest of generate_art() function code...

# Define the number of images selection widget
num_images_var = tk.IntVar()
num_images_var.set(10)
num_images_label = tk.Label(root, text='Number of Images:')
num_images_label.pack()
num_images_entry = tk.Entry(root, textvariable=num_images_var)
num_images_entry.pack()

# Modify the generate_art() function to use the selected number of images
def generate_art(input_dir, output_dir, checkpoint_path):
    num_images = num_images_var.get()

    for i in range(num_images):
        # Rest of generate_art() function code...

# Define the image size selection widget
image_size_var = tk.IntVar()
image_size_var.set(256)
image_size_label = tk.Label(root, text='Image Size:')
image_size_label.pack()
image_size_entry = tk.Entry(root, textvariable=image_size_var)
image_size_entry.pack()

# Modify the generate_art() function to use the selected image size
def generate_art(input_dir, output_dir, checkpoint_path):
    image_size = image_size_var.get()

    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.CenterCrop(image_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    # Rest of generate_art() function code...

# Define the watermark selection widget
watermark_var = tk.StringVar()
watermark_var.set('© My Art')
watermark_label = tk.Label(root, text='Watermark:')
watermark_label.pack()
watermark_entry = tk.Entry(root, textvariable=watermark_var)
watermark_entry.pack()

# Modify the generate_art() function to add the selected watermark to the generated art images
def generate_art(input_dir, output_dir, checkpoint_path):
    watermark_text = watermark_var.get()

    for i in range(num_images):
        # Rest of generate_art() function code...

        # Add the watermark to the generated image
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 20)
        draw.text((10, 10), watermark_text, fill=(255, 255, 255), font=font)

        # Save the image with the watermark
        image.save(os.path.join(output_dir, f'image_{i}.jpg'))

# Define the style image directory selection widget
style_path_var = tk.StringVar()
style_path_label = tk.Label(root, text='Style Image Directory:')
style_path_label.pack()
style_path_entry = tk.Entry(root, textvariable=style_path_var)
style_path_entry.pack()

# Define the content image directory selection widget
content_path_var = tk.StringVar()
content_path_label = tk.Label(root, text='Content Image Directory:')
content_path_label.pack()
content_path_entry = tk.Entry(root, textvariable=content_path_var)
content_path_entry.pack()

# Modify the generate_art() function to use the selected style and content image directories
def generate_art():
    style_path = style_path_var.get()
    content_path = content_path_var.get()

    # Load the style and content images
    style_image = Image.open(style_path)
    content_image = Image.open(content_path)

    # Rest of generate_art() function code...

# Define the filter selection widget
filter_var = tk.StringVar()
filter_var.set('None')
filter_label = tk.Label(root, text='Filter:')
filter_label.pack()
filter_menu = tk.OptionMenu(root, filter_var, 'None', 'Blur', 'Sharpen', 'Contour', 'Edge Enhance', 'Emboss')
filter_menu.pack()

# Modify the generate_art() function to apply the selected filter to the generated art images
def generate_art():
    # Rest of generate_art() function code...

    # Apply the selected filter to the generated image
    filter_name = filter_var.get()
    if filter_name == 'Blur':
        image = image.filter(ImageFilter.BLUR)
    elif filter_name == 'Sharpen':
        image = image.filter(ImageFilter.SHARPEN)
    elif filter_name == 'Contour':
        image = image.filter(ImageFilter.CONTOUR)
    elif filter_name == 'Edge Enhance':
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_name == 'Emboss':
        image = image.filter(ImageFilter.EMBOSS)

    # Save the image with the filter applied
    image.save(os.path.join(output_dir, f'image_{i}.jpg'))
# Define the color palette selection widget
palette_var = tk.StringVar()
palette_var.set('Default')
palette_label = tk.Label(root, text='Color Palette:')
palette_label.pack()
palette_menu = tk.OptionMenu(root, palette_var, 'Default', 'Grayscale', 'Cool', 'Warm', 'Pastel')
palette_menu.pack()

# Modify the generate_art() function to apply the selected color palette to the generated art images
def generate_art():
    # Rest of generate_art() function code...

    # Apply the selected color palette to the generated image
    palette_name = palette_var.get()
    if palette_name == 'Grayscale':
        image = ImageOps.grayscale(image)
    elif palette_name == 'Cool':
        image = ImageOps.colorize(image, (0, 0, 255), (255, 255, 255))
    elif palette_name == 'Warm':
        image = ImageOps.colorize(image, (255, 0, 0), (255, 255, 255))
    elif palette_name == 'Pastel':
        image = ImageOps.posterize(image, 2)

    # Save the image with the color palette applied
    image.save(os.path.join(output_dir, f'image_{i}.jpg'))
# Define the text input widget
text_var = tk.StringVar()
text_label = tk.Label(root, text='Text:')
text_label.pack()
text_entry = tk.Entry(root, textvariable=text_var)
text_entry.pack()

# Modify the generate_art() function to add the selected text to the generated art images
def generate_art():
    # Rest of generate_art() function code...

    # Add the selected text to the generated image
    text = text_var.get()
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 20)
    text_width, text_height = draw.textsize(text, font=font)
    draw.text(((image_size - text_width) // 2, (image_size - text_height) // 2), text, fill=(255, 255, 255), font=font)

    # Save the image with the text added
    image.save(os.path.join(output_dir, f'image_{i}.jpg'))

# Define the brightness slider widget
brightness_var = tk.DoubleVar()
brightness_var.set(1.0)
brightness_label = tk.Label(root, text='Brightness:')
brightness_label.pack()
brightness_slider = tk.Scale(root, variable=brightness_var, from_=0.0, to=2.0, resolution=0.1, orient='horizontal')
brightness_slider.pack()

# Define the contrast slider widget
contrast_var = tk.DoubleVar()
contrast_var.set(1.0)
contrast_label = tk.Label(root, text='Contrast:')
contrast_label.pack()
contrast_slider = tk.Scale(root, variable=contrast_var, from_=0.0, to=2.0, resolution=0.1, orient='horizontal')
contrast_slider.pack()

# Define the saturation slider widget
saturation_var = tk.DoubleVar()
saturation_var.set(1.0)
saturation_label = tk.Label(root, text='Saturation:')
saturation_label.pack()
saturation_slider = tk.Scale(root, variable=saturation_var, from_=0.0, to=2.0, resolution=0.1, orient='horizontal')
saturation_slider.pack()

# Modify the generate_art() function to adjust the brightness, contrast, and saturation of the generated art images
def generate_art():
    # Rest of generate_art() function code...

    # Adjust the brightness, contrast, and saturation of the generated image
    brightness = brightness_var.get()
    contrast = contrast_var.get()
    saturation = saturation_var.get()
    image = ImageEnhance.Brightness(image).enhance(brightness)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Color(image).enhance(saturation)

    # Save the image with the brightness, contrast, and saturation adjusted
    image.save(os.path.join(output_dir, f'image_{i}.jpg'))
# Define the settings file input widget
settings_var = tk.StringVar()
settings_label = tk.Label(root, text='Settings File:')
settings_label.pack()
settings_entry = tk.Entry(root, textvariable=settings_var)
settings_entry.pack()

# Define the save settings button
def save_settings():
    settings = {
        'num_images': num_images_var.get(),
        'image_size': image_size_var.get(),
        'watermark': watermark_var.get(),
        'style_path': style_path_var.get(),
        'content_path': content_path


# Run the GUI main loop

root.mainloop()
