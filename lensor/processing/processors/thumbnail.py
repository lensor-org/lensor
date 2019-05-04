import base64
from io import BytesIO

from PIL import Image


class Thumbnail:

    def __init__(self, input_file, size):
        self.file = input_file
        self.size = size

    def get_thumbnail(self):
        image = Image.open(self.file)
        image.thumbnail(self.size, Image.ANTIALIAS)
        return image

    def get_thumbnail_base64(self):
        thumbnail = self.get_thumbnail()
        thumbnail_buffer = BytesIO()
        thumbnail.save(thumbnail_buffer, format="JPEG")

        return base64.b64encode(thumbnail_buffer.getvalue())
