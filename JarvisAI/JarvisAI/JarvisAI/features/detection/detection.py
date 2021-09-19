import cvzone
import cv2


class Detections:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detectionCon = 0.5
        self.maxHands = 2
        self.cam_display = True
        self.detector = cvzone.HandDetector(detectionCon=self.detectionCon, maxHands=self.maxHands)

    def configure_hand_detector(self, camera=0, detectionCon=0.7, maxHands=2, cam_display=True, cam_height=480, cam_width=888):
        self.cap = cv2.VideoCapture(camera)
        self.cap.set(3, cam_width)
        self.cap.set(4, cam_height)
        self.detectionCon = detectionCon
        self.maxHands = maxHands
        self.cam_display = cam_display
        self.detector = cvzone.HandDetector(detectionCon=self.detectionCon, maxHands=self.maxHands)
        # self.detector_face = cvzone.FaceMeshDetector(maxFaces=2)

    def detect_hands(self, message=""):
        success, img = self.cap.read()
        # img, faces = self.detector_face.findFaceMesh(img)
        img = self.detector.findHands(img)
        lmlist, bbox = self.detector.findPosition(img)
        fingers = None
        myHandType = None
        img = cv2.flip(img, 1)
        if lmlist:
            fingers = self.detector.fingersUp()
            totalFingers = fingers.count(1)
            myHandType = self.detector.handType()
            cv2.putText(img, f'Hand:{myHandType} | Fingers:{totalFingers}', (50, 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cv2.putText(img, f'{message}', (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        if self.cam_display:
            cv2.imshow('img', img)
            cv2.waitKey(1)
        return fingers, myHandType, cv2, img, self.cap


if __name__ == '__main__':
    obj = Detections()
    obj.configure_hand_detector(maxHands=2)

    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            future = executor.submit(obj.detect_hands)
            fingers, hand_type, cv2, img = future.result()
            print(fingers, hand_type)

        # fingers, hand_type, cv2, img = obj.detect_hands()
        # print(fingers, hand_type)
        # cv2.putText(img, f'{"message"}', (50, 200),
        #                 cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        # cv2.imshow("img", img)
        # cv2.waitKey(1)
