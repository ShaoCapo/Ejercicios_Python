import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('numeros.png')
# np.ones(shape, dtype = None, order = 'C'):
        # devuelve un nuevo array de forma y tipo dados, con unos.
kernel = np.ones((5,5),np.float32)/25

# cv2.filter2D(src, dst, ddepth, kernel):
        # convoluciona una imagen con el núcleo.
# src: Un objeto Mat que representa la fuente (imagen de entrada)
#      para esta operación.
# dst: Un objeto Mat que representa el destino (imagen de salida)
#      de esta operación.
# ddepth: Una variable de tipo entero que representa la profundidad
#         de la imagen de salida.
# kernel: Un objeto Mat que representa el kernel de convolución.
dst = cv2.filter2D(img,-1,kernel)
# cv2.blur(img,(5,5)): desenfoca una image
blur = cv2.blur(img,(5,5))

gaussianBlur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,75,75)

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(dst),plt.title('Media')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.subplot(234),plt.imshow(gaussianBlur),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(median),plt.title('Mediana')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(bilateral),plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()
