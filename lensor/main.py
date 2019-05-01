from lensor.processors.thumbnail import create as createThumbnail
from lensor.processors.exif import read_exif

def run():
    image_file = open('./lensor/processors/example.jpg', 'r+b')
    
    processImage(image=image_file)

def processImage(image):
    ### Thumbnail
    # Create thumbnail
    thumbnail_pil = createThumbnail(input_file=image, size=(256, 256))
    # Save thumbnail TODO return to response
    thumbnail_pil.save("./thumbnail.jpg", "JPEG")

    ### File information (exif...)
    exif_tags = read_exif(image)
    
    ### Faces

    ### Scene

    ### Location

    ### Things

