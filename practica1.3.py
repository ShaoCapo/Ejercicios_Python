import cv2
from matplotlib import pyplot as plt

img = cv2.imread('yelmo.png', cv2.IMREAD_GRAYSCALE)

# cv2.calcHist(images, [channels], mask, histSize, ranges[, hist[, accumulate]])
# images = imagen de origen de tipo uint8 o float32 representada como "[img]".
# [channels] = es el índice del canal para el que calculamos el histograma.
#              Para la imagen en escala de grises, su valor es [0] y
#
# [mask] = imagen de máscara. Para encontrar el histograma de la imagen completa,
#          se da como "None".
# histSize = representa nuestra cuenta BIN. Para la escala completa, pasamos [256].
# ranges = esto es nuestro RANGO. Normalmente, es [0,256].
hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(211), plt.title('original'), plt.axis("off")
plt.imshow(img, 'gray')

plt.subplot(212), plt.title('histograma')
plt.hist(img.ravel(), 256, [0, 256])

plt.show()
