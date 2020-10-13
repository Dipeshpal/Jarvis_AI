import tensorflow as tf
import numpy as np
from tensorflow import keras
import cv2
import os


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
        self.model = keras.models.load_model(f'{self.model_path}/model.h5')

    def preprocessing(self, img_path):
        img = keras.preprocessing.image.load_img(
            img_path, target_size=(self.img_height, self.img_width)
        )
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        self.img_src_preprocessed = img_array

    def predict(self, img_path):
        self.preprocessing(img_path)
        predictions = self.model.predict(self.img_src_preprocessed)
        score = tf.nn.softmax(predictions[0])
        cls = self.class_name[np.argmax(score)]
        confidence = 100 * np.max(score)
        return cls, confidence

    def show(self, img):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cls, confidence = self.predict('tmp.png')
        print(cls, confidence)
        cv2.putText(img, cls + ' ' + str(confidence)[:5] + '%', (50, 50), font,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('img', img)
        os.remove('tmp.png')

    def cap_and_predict(self):
        face_cascade = cv2.CascadeClassifier(self.haarcascade_path)
        eye_cascade = cv2.CascadeClassifier(self.eyecascade_path)
        cap = cv2.VideoCapture(0)

        while True:
            _, img = cap.read()
            if not self.color_mode:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(img, 1.1, 4)

            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_color = img[y:y + h, x:x + w]

                eyes = eye_cascade.detectMultiScale(roi_color)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                cv2.imwrite('tmp.png', roi_color)
                self.show(img)

            # Stop if 'q' key is pressed
            key = cv2.waitKey(30) & 0xFF
            if key == ord("q"):
                cap.release()
                cv2.destroyAllWindows()
                break
        # Release the VideoCapture object
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    class_name = ['Dipesh', 'Jay']
    obj = Predict(class_name=class_name, color_mode=False)
    obj.cap_and_predict()
