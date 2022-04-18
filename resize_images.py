#I'm bad and can't figure out how to resize images in Markdown/HTML so I'm manually resizing images here

from PIL import Image
import exifread
import glob
import os

def resize_images(new_width):
    pre_images_dir = os.getcwd() + '/pre_images/*'
    save_path = os.getcwd() + '/static/images/misc'

    for file in glob.glob(pre_images_dir):
        # getting the orientation from exif tag
        orientation = None
        f = open(file, 'rb')
        exif_tags = exifread.process_file(f)
        if bool(exif_tags):
            key = 'Image Orientation'
            if key in exif_tags.keys():
                orientation = str(exif_tags[key])

        file_name = file.split('/')[-1]
        img_save_path = save_path + '/' + file_name
        img = Image.open(file)

        if orientation == "Rotated 90 CW":
            img = img.rotate(-90, Image.NEAREST, expand = 1)

        width, height = img.size

        aspect_ration = width/height
        new_height = new_width/aspect_ration

        new_size = (new_width, new_height)

        img.thumbnail(new_size, Image.ANTIALIAS)
        img.save(img_save_path)

if __name__ == '__main__':
    resize_images(500)