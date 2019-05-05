from lensor.db.init_db import InitDB
from lensor.processing.imageinfo import ImageInfo


def run():

    db_engine = InitDB().get_engine()
    db_engine.connect()
    print(db_engine)
    image_file = open('./lensor/processing/examples/example.jpg', 'r+b')

    image_info = ImageInfo(image_id="temp_id", image=image_file)
    image_info.process()

    print(str(image_info))
