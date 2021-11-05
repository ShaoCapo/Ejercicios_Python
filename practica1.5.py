import cv2
import numpy as np

img = cv2.imread('reloj.png',0)

# ecualizamos la imagen
equ = cv2.equalizeHist(img)

# concatenamos la imagen y su histograma
# np.hstack() : se utiliza para apilar la secuencia de matrices de
#               entrada horizontalmente (es decir, por columnas) para formar
#               una única matriz.
res = np.hstack((img,equ))

cv2.imshow('img',res)
cv2.waitKey()
cv2.destroyAllWindows()
