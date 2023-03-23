import datetime
import cv2
import os


def click_pic(*args, **kwargs):
    try:
        t = datetime.datetime.now()
        #     Taking a video from the webcam
        camera = cv2.VideoCapture(0)
        #     Taking first 20 frames of the video
        for i in range(20):
            return_value, image = camera.read()
        if not os.path.exists("photos"):
            os.mkdir("photos")
        #     Using 20th frame as the picture and now saving the image as the time in seconds,minute,hour,day and month of the year
        # Giving the camera around 20 frames to adjust to the surroundings for better picture quality
        cv2.imwrite(f"photos/{t.second, t.minute, t.hour, t.day, t.month}_photo.png", image)
        #     As soon as the image is saved we will stop recording
        del camera
        print(f"Photo taken: photos/{t.second, t.minute, t.hour, t.day, t.month}_photo.png")
        return "Photo taken"
    except Exception as e:
        return "Error: " + str(e) + "\n Unable to take photo"


# Calling the photo_with_python function
if __name__ == "__main__":
    click_pic()
