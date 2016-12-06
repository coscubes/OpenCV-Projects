import math
import cv2
from scipy.stats import linregress


def new_points(x, y, slope):
    if t:
        xnew = x + 50 * math.cos(math.atan(slope))
        ynew = y + 50 * math.sin(math.atan(slope))
    else:
        xnew = x + 50 * math.cos(math.atan(slope))
        ynew = y + 50 * math.sin(math.atan(slope))
    return xnew, ynew
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

t = True
X = []
Y = []
for i in range(10):
    X.append(0)
    Y.append(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        X.pop(0)
        Y.pop(0)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        # m.move(x+ int(w / 2), y + int(h / 2))
        X.append(int(x + w / 2))
        Y.append(int(y + h / 2))
        line = linregress(X, Y)
        xnew, ynew = new_points(X[9], Y[9], line[0])
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2
        cv2.line(img, (X[9], Y[9]), (int(xnew), int(ynew)), (0, 0, 255), 5)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
