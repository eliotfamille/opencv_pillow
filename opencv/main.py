import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1) # lis le capteur
if not cap.isOpened():
    print("impossible d'acceder a la camera")
    exit()

while True:
    ret, frame = cap.read() # prend chaque frame

    if not ret:
        print("ne recois pas d'image (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)    # renvois l'image et le coleur
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
