import auto_face_recognition
import pathlib
import glob
import os

obj = auto_face_recognition.AutoFaceRecognition()


class DatasetCreate:
    def __init__(self, dataset_path='datasets', class_name='Demo',
                 haarcascade_path='haarcascade/haarcascade_frontalface_default.xml',
                 eyecascade_path='haarcascade/haarcascade_eye.xml', eye_detect=False,
                 save_face_only=True, no_of_samples=100,
                 width=128, height=128, color_mode=False):
        self.dataset_path = dataset_path
        self.class_name = class_name
        self.haarcascade_path = haarcascade_path
        self.eyecascade_path = eyecascade_path
        self.eye_detect = eye_detect
        self.save_face_only = save_face_only
        self.no_of_samples = no_of_samples
        self.width = width
        self.height = height
        self.color_mode = color_mode

    def datasetcreate(self):
        obj.datasetcreate(dataset_path=self.dataset_path, class_name=self.class_name,
                          haarcascade_path=self.haarcascade_path,
                          eyecascade_path=self.eyecascade_path, eye_detect=self.eye_detect,
                          save_face_only=self.save_face_only, no_of_samples=self.no_of_samples,
                          width=self.width, height=self.height, color_mode=self.color_mode)


class FaceRecognizerTrain:
    def __init__(self, data_dir='datasets', batch_size=32, img_height=128, img_width=128, epochs=10,
                 model_path='model', pretrained=None, base_model_trainable=False):
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.img_height = img_height
        self.img_width = img_width
        self.class_names = None
        self.epochs = epochs
        self.model_path = model_path
        self.pretrained = pretrained
        self.base_model_trainable = base_model_trainable

    def train(self):
        obj.face_recognition_train(data_dir=self.data_dir, batch_size=self.batch_size, img_height=self.img_height,
                                   img_width=self.img_width, epochs=self.epochs, model_path=self.model_path,
                                   pretrained=self.pretrained, base_model_trainable=self.base_model_trainable)


class Predict:
    def __init__(self, class_name, img_height=128, img_width=128,
                 haarcascade_path='haarcascade/haarcascade_frontalface_default.xml',
                 eyecascade_path='haarcascade/haarcascade_eye.xml', model_path='model',
                 color_mode=False):
        self.img_height = img_height
        self.img_width = img_width
        self.img_src_preprocessed = None
        self.class_name = class_name
        self.haarcascade_path = haarcascade_path
        self.eyecascade_path = eyecascade_path
        self.color_mode = color_mode
        self.model_path = model_path

    def predictfaces(self):
        obj.predict_faces(class_name=self.class_name, img_height=self.img_height, img_width=self.img_width,
                          haarcascade_path=self.haarcascade_path,
                          eyecascade_path=self.eyecascade_path, model_path=self.model_path,
                          color_mode=self.color_mode)
