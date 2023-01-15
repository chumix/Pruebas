import cv2
import facemesh

# Cargar una imagen de fondo
img = cv2.imread("image.jpg")

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Obtener el tamaño de la imagen de fondo
img_height, img_width, _ = img.shape

# Define el tamaño y posición de la ventana de video
video_height = int(img_height * 0.3)
video_width = int(img_width * 0.3)
video_x = int(img_width * 0.35)
video_y = int(img_height * 0.65)

# Inicializar FaceMesh
model = facemesh.load_model()

while True:
    # Leer un marco de la cámara
    ret, frame = cap.read()

    # Redimensionar el marco de video
    frame = cv2.resize(frame, (video_width, video_height))

    # Añadir el marco de video a la imagen de fondo
    img[video_y:video_y + video_height, video_x:video_x + video_width] = frame
    
    # Convertir la imagen a formato RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar rostros en el marco
    predictions = model.predict(frame)
    if predictions:
        # Dibujar los puntos clave del rostro en el marco
        facemesh.visualize_points(frame, predictions)
        # Añadir los puntos clave al marco de video
        img[video_y:video_y + video_height, video_x:video_x + video_width] = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Mostrar la imagen en una ventana
    cv2.imshow("Image", img)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
