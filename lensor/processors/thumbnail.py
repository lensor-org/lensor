from PIL import Image


def create(input_file, size):
    Image.Image
    image = Image.open(input_file)
    image.thumbnail(size, Image.ANTIALIAS)
    return image
