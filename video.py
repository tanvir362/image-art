import cv2
import time
from image_art import ImageArt
from outline import outline

camera = cv2.VideoCapture(0)

art = ImageArt('images/t.png')


while True:
    ret, frame = camera.read()
    art.set_orginal_image(frame)

    cv2.imshow(f"video", art.prepare_image())

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()