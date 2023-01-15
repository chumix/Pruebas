import cv2

# Cargar una imagen
img = cv2.imread("image.jpg")

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Leer un marco de la cámara
    ret, frame = cap.read()

    # Girar la imagen de la cámara para que sea espejo
    frame = cv2.flip(frame, 1)

    # Añadir el marco de la cámara a la imagen
    img[0:frame.shape[0], 0:frame.shape[1]] = frame

    # Mostrar la imagen resultante
    cv2.imshow("Image with webcam", img)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
