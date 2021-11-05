import cv2
from matplotlib import pyplot as plt

img = cv2.imread('baboon.jpg',cv2.IMREAD_COLOR)

color = ('b', 'g', 'r')

# enumerate(value): convierte una tupla en un objeto de enumeración
for i,col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0,256])
# plt.plot: recibe un conjunto de valores x e y, los muestra en
#           el plano definido por los ejes como puntos unidos por líneas
    plt.plot(histr,color = col)
#plt.xlim(*args, **kwargs): muestra el histograma entre los valores
#                           especificados
    plt.xlim([0,256])
plt.show()
