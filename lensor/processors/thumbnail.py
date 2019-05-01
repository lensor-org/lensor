from PIL import Image

def create(input_file, size):
    image = Image.open(input_file)
    image.thumbnail(size, Image.ANTIALIAS)
    return image