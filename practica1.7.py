import cv2

face_cascade = cv2.CascadeClassifier('./opencv/data/haarcascades/haarcascade_frontalface_default.xml')
ete_cascade = cv2.CascadeClassifier('./opencv/data/haarcascades/haarcascade_eye.xml')

img = cv2.imread('24Lena.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    img = cv2.rectagule(img, (x,y),(x+w, y+h),(255,0,0),2)
    roi_gray = gray[y:t+h, x:x+w]
    roi_color = img[y:t+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey,ew,eh) in eyes:
        cv2.rectangule(roi_color,(ex,ey), (ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
