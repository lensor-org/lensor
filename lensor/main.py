from lensor.processors.exif import ExifReader
from lensor.processors.thumbnail import Thumbnail
# from lensor.processors.faces import show_faces


def run():
    image_file = open('./lensor/processors/example.jpg', 'r+b')

    processImage(image=image_file)


def processImage(image):
    image_info = {}

    # Thumbnail
    thumbnail = Thumbnail(input_file=image, size=(256, 256))
    image_info['thumbnail'] = thumbnail.get_thumbnail_base64()

    # File information (exif...)
    exif_reader = ExifReader(input_file=image)
    image_info['exif'] = exif_reader.read_exif()

    # Faces
    # show_faces()

    # Scene

    # Location

    # Things

    print("Image info: " + str(image_info))
