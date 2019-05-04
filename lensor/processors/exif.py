from PIL import Image, ExifTags
from datetime import datetime


def read_exif(input_file):
    image = Image.open(input_file)

    exif = decode_exif_tags(image)
    gps_info = decode_gps_info(exif)

    exif_info = {
        'timestamp': (
            datetime_to_timestamp(exif.get("DateTimeOriginal"))
            if "DateTimeOriginal" in exif
            else None
        ),
        'width': exif.get("ExifImageWidth", image.width),
        'height': exif.get("ExifImageHeight", image.height),
        'gps': get_lat_lon(gps_info)
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
    return {}


def decode_gps_info(exif_tags):
    gpsinfo = {}
    if ("GPSInfo" in exif_tags):
        for key in exif_tags['GPSInfo'].keys():
            decode = ExifTags.GPSTAGS.get(key, key)
            gpsinfo[decode] = exif_tags['GPSInfo'][key]
    return gpsinfo


def get_lat_lon(gps_info):
    latitude = None
    longitude = None

    gps_lat = gps_info.get("GPSLatitude")
    gps_lat_ref = gps_info.get("GPSLatitudeRef")
    gps_long = gps_info.get("GPSLongitude")
    gps_long_ref = gps_info.get("GPSLongitudeRef")

    if gps_lat and gps_lat_ref and gps_long and gps_long_ref:
        latitude = coords_to_degrees(gps_lat)
        if gps_lat_ref != "N":
            latitude = -latitude

        longitude = coords_to_degrees(gps_long)
        if gps_long_ref != "E":
            longitude = -longitude

    return {
        'latitude:': latitude,
        'longitude': longitude
    }


def coords_to_degrees(coords):
    d0 = coords[0][0]
    d1 = coords[0][1]
    d = float(d0) / float(d1)

    m0 = coords[1][0]
    m1 = coords[1][1]
    m = float(m0) / float(m1)

    s0 = coords[2][0]
    s1 = coords[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)


def datetime_to_timestamp(date):
    return datetime.strptime(date, "%Y:%m:%d %H:%M:%S").timestamp()
