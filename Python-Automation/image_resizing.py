from PIL import Image
import os

fit_size = int(input('Enter size: '))  # the size we would fit the image to
output_folder = input('Enter name of output folder: ')

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# '.' for current folder
for filename in os.listdir('.'):
    if not filename.endswith(('.png', '.jpg', 'jpeg', 'gif')):
        continue

    # Open Image
    image = Image.open(filename)

    # Get Size
    width, height = image.size

    # Resizing
    if width > fit_size and height > fit_size:  # make sure that width and height are greater than fit_size
        if width > height:
            height = int((fit_size/width)*height)
            width = fit_size
        else:
            width = int((fit_size/height)*width)
            height = fit_size

        image = image.resize((width, height))
        image = image.save(os.path.join(output_folder, filename))
