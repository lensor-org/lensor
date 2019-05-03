from lensor.processors.exif import read_exif
# from lensor.processors.faces import show_faces
from lensor.processors.thumbnail import create as createThumbnail
import base64
from io import BytesIO


def run():
    image_file = open('./lensor/processors/example.jpg', 'r+b')

    processImage(image=image_file)


def processImage(image):
    image_info = {}

    # Thumbnail
    thumbnail = createThumbnail(input_file=image, size=(256, 256))
    # Converting image to base64 string and storing in dict
    thumbnail_buffer = BytesIO()
    thumbnail.save(thumbnail_buffer, format="JPEG")
    image_info['thumbnail'] = base64.b64encode(thumbnail_buffer.getvalue())

    # File information (exif...)
    image_info['exif'] = read_exif(image)

    # Faces
    # show_faces()

    # Scene

    # Location

    # Things

    print("Image info: " + str(image_info))
