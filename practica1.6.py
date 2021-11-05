import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('yelmo.png',0)

gamma = 0.6
invGamma = 1.0 / gamma

table = np.array([((i / 255.0) ** invGamma) *
                  255 for i in np.arange(0, 256)]).astype("uint8")

res = cv2.LUT(img, table)

plt.subplot(211), plt.title('original'), plt.axis("off")
plt.imshow(img, 'gray')

plt.subplot(212), plt.title('gamma'), plt.axis("off")
plt.imshow(res, 'gray')

plt.show()
