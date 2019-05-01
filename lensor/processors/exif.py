import exifread


def read_exif(file):
    tags = exifread.process_file(file, details=False)

    # Read GPS data if available (GPS GPSLatitude, GPS GPSLongitude),
    # original time captured (EXIF DateTimeOriginal)

    print(tags.keys())
