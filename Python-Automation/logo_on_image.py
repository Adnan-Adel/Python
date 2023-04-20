import os
from PIL import Image

# Get Logo Name
LOGO_NAME = input('Enter Name of Logo(With Extension): ')

# Get Name of Output Folder
OUTPUT_FOLDER_NAME = input('Enter Name of Output Folder: ')

# Get Logo Info
logo_image = Image.open(LOGO_NAME)
logo_width, logo_height = logo_image.size

# Creat Output Folder
if not os.path.exists(OUTPUT_FOLDER_NAME):
    os.mkdir(OUTPUT_FOLDER_NAME)

for filename in os.listdir('.'):  # '.' for current path
    if not (filename.endswith(('.png', '.jpg', 'jpeg', 'gif')) or filename == LOGO_NAME):
        continue

    img = Image.open(filename)
    img_width, img_height = img.size

    # Add Logo to Image
    img.paste(logo_image, (img_width - logo_width, img_height - logo_height))

    img.save(os.path.join(OUTPUT_FOLDER_NAME, filename))
