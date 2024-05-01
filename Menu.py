import cv2
import speech_recognition as sr
import time

# Cargamos el clasificador de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializamos el reconocedor de voz
recognizer = sr.Recognizer()

# Función para escuchar la respuesta del usuario
def listen_response():
    with sr.Microphone() as source:
        print("Di algo...")
        try:
            audio = recognizer.listen(source, phrase_time_limit=5)
            response = recognizer.recognize_google(audio, language='es-ES')
            print("Usuario dijo:", response)
            return response
        except sr.WaitTimeoutError:
            print("No se detectó ningún habla.")
            return None

# Función para detectar rostros
def detect_face():
    cap = cv2.VideoCapture(0)  # Inicializamos la captura de video

    start_time = time.time()  # Guardamos el tiempo de inicio
    while True:
        ret, img = cap.read()  # Leemos un frame del video
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convertimos a escala de grises
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detectamos rostros

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Dibujamos un rectángulo alrededor del rostro

        cv2.imshow('img', img)  # Mostramos la imagen

        if time.time() - start_time > 5:  # Si han pasado más de 5 segundos, salimos del bucle
            break

    cap.release()  # Liberamos la captura de video
    cv2.destroyAllWindows()  # Cerramos todas las ventanas de OpenCV

# Función principal
def main():
    detect_face()  # Detectamos rostros

    response = listen_response()  # Escuchamos la respuesta del usuario

    # Desplegamos el menú según la respuesta del usuario
    if response is not None:
        if 'posgrados' in response.lower():
            print("Has seleccionado Posgrados.")
        elif 'salones' in response.lower():
            print("Has seleccionado Salones.")
        elif 'titulación' in response.lower():
            print("Has seleccionado Titulación.")
        elif 'servicio social' in response.lower():
            print("Has seleccionado Servicio Social.")
        elif 'recidencias' in response.lower():
            print("Has seleccionado Recidencias.")
        elif 'bebedero' in response.lower():
            print("Has seleccionado Bebedero.")
        elif 'baños' in response.lower():
            print("Has seleccionado Baños.")
        else:
            print("No se reconoció la opción.")

if __name__ == "__main__":
    main()