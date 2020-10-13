import cv2
import os


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

    def save_and_show(self, count, img):
        print(f'Generated {self.dataset_path}/{self.class_name}/frame_{count}.png')
        img = cv2.resize(img, (self.width, self.height))
        cv2.imshow('img', img)
        cv2.imwrite(f"{self.dataset_path}/{self.class_name}/" + f"frame_{count}.png", img)
        count += 1
        return count

    def create(self):
        face_cascade = cv2.CascadeClassifier(self.haarcascade_path)
        eye_cascade = cv2.CascadeClassifier(self.eyecascade_path)
        cap = cv2.VideoCapture(0)

        count = 0

        if not os.path.exists(self.dataset_path):
            os.makedirs(self.dataset_path)

        if not os.path.exists(self.dataset_path + self.class_name):
            os.makedirs(self.dataset_path + '/' + self.class_name)

        while True:
            _, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                if self.color_mode:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    roi_color = img[y:y + h, x:x + w]
                else:
                    cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]

                if self.eye_detect:
                    if self.color_mode:
                        eyes = eye_cascade.detectMultiScale(roi_color)
                    else:
                        eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        if self.color_mode:
                            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                        else:
                            cv2.rectangle(roi_gray, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                if self.save_face_only and self.color_mode:
                    count = self.save_and_show(count, roi_color)
                if self.save_face_only and not self.color_mode:
                    count = self.save_and_show(count, roi_gray)
                if not self.save_face_only and self.color_mode:
                    count = self.save_and_show(count, img)
                if not self.save_face_only and not self.color_mode:
                    count = self.save_and_show(count, gray)

            if count == self.no_of_samples:
                break
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
    obj = DatasetCreate(save_face_only=True, color_mode=False, class_name='Dipesh')
    obj.create()
