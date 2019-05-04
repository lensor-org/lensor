import face_recognition
from PIL import Image
from PIL import ImageDraw


def show_faces():
    image = face_recognition.load_image_file(
        "./lensor/processors/example_faces.jpg"
    )
    face_locations = face_recognition.face_locations(image)

    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location

        draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0), )

    del draw
    pil_image.save("./temp/out.jpg", "JPEG")
