from lensor.processing.imageinfo import ImageInfo


def run():
    image_file = open('./lensor/processing/examples/example.jpg', 'r+b')

    image_info = ImageInfo(id="temp_id", image=image_file)
    image_info.process()

    print(str(image_info))
