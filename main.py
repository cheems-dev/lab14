# importando librerias basicas para el proyecto
import cv2
import face_recognition
import imutils

# lectura del video en este caso, tambien podria usarse la camara web
cap = cv2.VideoCapture('input.mp4' ,0)
# Lista para almacenar los rostros encontrados en la imagen
face_locations = []

while True:
    # Capturando video
    ret, frame = cap.read()
    if not ret:
        # Entrara al if si el video termmina
        print("end of video")
        break

    # Cambiando la resolucion del video para poder correrlo con fluidez
    frame = imutils.resize(frame, width=600)
    
    # obteniendo los canlaes rgb para poder pasarselos al detector de rostros
    rgb_frame = frame[:, :, ::-1]
    # Funcion que se encarga de encontrar todos los rostros en el fotograma
    face_locations = face_recognition.face_locations(rgb_frame)

    # Mostrar los rostros encontradas
    for top, right, bottom, left in face_locations:
        # Dibujando un rectangulo y escribiendo donde se encontro un rostro
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
        cv2.putText(frame, 'Rostro',  (left, top-5), cv2.FONT_HERSHEY_PLAIN, 1.0, (255,0,0), 2, cv2.LINE_AA)
    # Mostrando la imagen con los rostros detectados
    cv2.imshow('Video', frame)
    
    # Tecla para detecter el video
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

# Liberando recursos
cap.release()
cv2.destroyAllWindows()