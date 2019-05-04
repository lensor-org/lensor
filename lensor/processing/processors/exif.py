from datetime import datetime

from PIL import ExifTags
from PIL import Image


class ExifReader:

    def __init__(self, input_file):
        self.file = input_file

    def get_exif_info(self):
        image = Image.open(self.file)

        exif = self._decode_exif_tags(image)
        exif_info = ExifInfo(
            self._datetime_to_timestamp(exif.get("DateTimeOriginal")),
            exif.get("ExifImageWidth", image.width),
            exif.get("ExifImageHeight", image.height),
            GPSInfo(exif)
        )

        image.close()

        return exif_info

    def _decode_exif_tags(self, image):
        exif_info = image._getexif()
        if(exif_info):
            return {
                ExifTags.TAGS[k]: v
                for k, v in exif_info.items()
                if k in ExifTags.TAGS
            }
        return {}

    def _datetime_to_timestamp(self, date):
        return datetime.strptime(date, "%Y:%m:%d %H:%M:%S").timestamp()


class ExifInfo:

    def __init__(self, timestamp, width, height, gps_info):
        self.timestamp = timestamp
        self.width = width
        self.height = height
        self.gps_info = gps_info

    def __str__(self):
        return ("ExifInfo[timestamp={0}, width={1}, "
                "height={2}, gps_info={3}]").format(
                    self.timestamp, self.width, self.height, self.gps_info
                )


class GPSInfo:

    GPS_DIRECTION_NORTH = "N"
    GPS_DIRECTION_EAST = "E"

    latitude = None
    longitude = None

    def __init__(self, exif_tags):
        self.exif_tags = exif_tags
        self._decode_gps_info()

    def _decode_gps_info(self):
        gps_exif = self._decode_gps_exif()
        self._calc_lat_lon(gps_exif)

    def _decode_gps_exif(self):
        gps_exif = {}
        if ("GPSInfo" in self.exif_tags):
            for key in self.exif_tags['GPSInfo'].keys():
                decode = ExifTags.GPSTAGS.get(key, key)
                gps_exif[decode] = self.exif_tags['GPSInfo'][key]
        return gps_exif

    def _calc_lat_lon(self, gps_exif):

        gps_lat = gps_exif.get("GPSLatitude")
        gps_lat_ref = gps_exif.get("GPSLatitudeRef")
        gps_long = gps_exif.get("GPSLongitude")
        gps_long_ref = gps_exif.get("GPSLongitudeRef")

        if gps_lat and gps_lat_ref and gps_long and gps_long_ref:
            self.latitude = self._coords_to_degrees(gps_lat)
            if gps_lat_ref != self.GPS_DIRECTION_NORTH:
                self.latitude = -self.latitude

            self.longitude = self._coords_to_degrees(gps_long)
            if gps_long_ref != self.GPS_DIRECTION_EAST:
                self.longitude = -self.longitude

    def _coords_to_degrees(self, coords):
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

    def __str__(self):
        return "GPSInfo[latitude={0}, longitude={1}]".format(
            self.latitude, self.longitude
        )
