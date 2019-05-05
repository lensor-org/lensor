from PIL import Image
import face_recognition
import numpy as np
from PIL import Image
from PIL import ImageDraw


class FaceDetection:
    IMAGE_SCALING_FACTOR = 0.25
    FACE_MATCHING_THRESHOLD = 0.6

    def __init__(self, user_id, image_id):
        self.user_id = user_id
        self.image_id = image_id
        self.known_persons = dict(zip(
            self._get_known_faces(), self._get_known_names()))
        self.loaded_image = self._load_image()

    def _get_known_faces(self):
        # TODO Db call
        return

    def _get_known_names(self):
        # TODO Db call
        return

    def _load_image(self):
        # TODO Db call to retrive the image path by image id
        image_path = './lensor/processors/example_faces.jpg'
        image = Image.open(image_path)
        width, height = image.size

        # make image smaller for faster processing
        image.resize(
            (int(width * FaceDetection.IMAGE_SCALING_FACTOR),
             int(height * FaceDetection.IMAGE_SCALING_FACTOR)))
        image.convert('RGB')
        return list(image.getdata())

    def get_faces(self):
        face_locations = face_recognition.face_locations(self.loaded_image)
        detected_faces = face_recognition.face_encodings(
            self.loaded_image, face_locations)    
        unknown_faces = []
        known_faces = []

        for index, face in detected_faces:
            face_distances = face_recognition.face_distance(
                self.known_faces, face)
            best_match = np.argmin(face_distances)
            location = tuple(
                x / FaceDetection.IMAGE_SCALING_FACTOR
                for x in face_locations[index])

            # is the face unknown?
            if (best_match >= FaceDetection.FACE_MATCHING_THRESHOLD):
                unknown_faces.append((face, location))
            else:
                known_faces.append(self.known_persons[face], face, location)

        # TODO save_unknown_faces(self.user_id, self.image_id, unknown_faces)
        # to db, best async
        return zip(unknown_faces, known_faces)
