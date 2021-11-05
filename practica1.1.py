import cv2

# cv2.imread(path, flag)
# path: imagen a leer
# flag: forma en la cual se leerá la imagen. Hay tres tipos
# cv2.IMREAD_COLOR: imagen a color (por defecto), lo mismo si se pone 1.
# cv2.IMREAD_GRAYSCALE: imagen a escala de grises, lo mismo si se pone 0.
# cv2.IMREAD_COLOR: imagen que incluye un canal alfa, lo mismo si se pone -1.
img = cv2.imread('formas.png', cv2.IMREAD_COLOR)

# cv2.imshow(window_name, image)
# window_name: nombre de la ventana
# image: imagen a mostar
cv2.imshow('original', img)

# cv2.cvtColor(src, code[, dst[, dstCn]])
# imagen a modificar
# código de conversión
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gris', gray)

# HSV (Hue, Saturation, Value) == Matiz, Saturacion, Valor
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# cv2.waitKey: devuelve un valor entero
k = cv2.waitKey(0) & 0xFF
if k == 27:         # ESC para salir
    cv2.destroyAllWindows()
# ord(character): devuelve el valor del carácter de la tabla ASCII
elif k == ord('s'): # s para salvar en JPG y salir
    # cv2.imwrite(filename, image)
    # filename: archivo de imagen
    # image: imagen elegida
    #cv2.imwrite('formas.jpg', img) guardas un duplicado
    cv2.imwrite('formas_hsv.jpg', hsv)
    cv2.imwrite('formas_gris.jpg', gray)
    cv2.destroyAllWindows()
