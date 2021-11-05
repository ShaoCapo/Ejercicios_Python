import cv2
from matplotlib import pyplot as plt

img = cv2.imread('formas.png',cv2.IMREAD_COLOR)

# quitar una vez comprobado el problema de formato BGR / RBG
#cv2.imshow('original',img) Muestra lo mismo que en el subplot(221) quitado

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# plt.subplot(nfil ncol pos)
# pos como máximo será nfil * ncol
# pos es la posición donde se colocará de la matriz.
plt.subplot(221), plt.title('original'), plt.axis("off")
plt.imshow(img)
# OpenCV usa BRG y matplotlib usa RGB
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

plt.subplot(223), plt.title('gris'), plt.axis("off")
plt.imshow(gray, 'gray')

plt.subplot(224), plt.title('hsv'), plt.axis("off")
plt.imshow(hsv, 'hsv')

plt.show()
