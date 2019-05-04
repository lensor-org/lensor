from lensor.processing.processors.exif import ExifReader
from lensor.processing.processors.thumbnail import Thumbnail


class ImageInfo:

    def __init__(self, image_id, image):
        self.image_id = image_id
        self.image = image

    def process(self):
        # Thumbnail
        thumbnail = Thumbnail(input_file=self.image, size=(256, 256))
        self.thumbnail = thumbnail.get_thumbnail_base64()

        # File information (exif...)
        exif_reader = ExifReader(input_file=self.image)
        self.exif = exif_reader.get_exif_info()

        # Faces TODO
        # Scene TODO
        # Location TODO
        # Things TODO

    def __str__(self):
        return "ImageInfo[id={0}, thumbnail={1}, exif={2}]".format(
            self.image_id, self.thumbnail, self.exif
        )
