from PIL import Image, ExifTags


def read_exif(input_file):
    image = Image.open(input_file)

    Image.Image

    exif = decode_exif_tags(image)
    gpsinfo = decode_gps_info(exif)

    exif_info = {
        'datetime': exif.get("DateTimeOriginal"),
        'width': exif.get("ExifImageWidth", image.width),
        'height': exif.get("ExifImageHeight", image.height),
        'gps': {
            'longitude': gpsinfo.get("GPSLongitude"),
            'latitude:': gpsinfo.get("GPSLatitude")
        }
    }

    image.close()

    return exif_info


def decode_exif_tags(image):
    # Reading and decoding ExifTags using Pillows ExifTags
    exif_info = image._getexif()
    if(exif_info):
        return {
            ExifTags.TAGS[k]: v
            for k, v in exif_info.items()
            if k in ExifTags.TAGS
        }
    else:
        return {}


def decode_gps_info(exif_tags):
    gpsinfo = {}
    if ("GPSInfo" in exif_tags):
        for key in exif_tags['GPSInfo'].keys():
            decode = ExifTags.GPSTAGS.get(key, key)
            gpsinfo[decode] = exif_tags['GPSInfo'][key]
    return gpsinfo
