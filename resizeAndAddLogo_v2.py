#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.
# _v2 - allows uppercase file extensions and .gif and .bmp formats

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

# create destination directory
os.makedirs('withLogo', exist_ok=True)

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# resize to make logo 100px wide, height adjusted to keep aspect ratio
logoIm = logoIm.resize((100, int(100 * (logoHeight / logoWidth))))
# reassign now smaller width and height to variables
logoWidth, logoHeight = logoIm.size

# Loop over all files in the working directory.
file_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
for filename in os.listdir('.'):
    if not filename.lower().endswith(file_extensions) \
            or filename == LOGO_FILENAME:
        continue  # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % filename)
        im = im.resize((width, height))

    # Add the logo.
    print('Adding logo to %s...' % filename)
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))
