from lensor.processors.thumbnail import create as createThumbnail
from lensor.processors.exif import read_exif
from lensor.processors.faces import show_faces


def run():
    image_file = open('./lensor/processors/example.jpg', 'r+b')

    processImage(image=image_file)


def processImage(image):
    # Thumbnail
    # Create thumbnail
    thumbnail_pil = createThumbnail(input_file=image, size=(256, 256))
    # Save thumbnail TODO return to response
    thumbnail_pil.save("./temp/thumbnail.jpg", "JPEG")

    # File information (exif...)
    exif_tags = read_exif(image)
    print(exif_tags)

    # Faces
    show_faces()

    # Scene

    # Location

    # Things
