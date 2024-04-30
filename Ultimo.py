import cv2
import pyttsx3
import speech_recognition as sr
import random
import time
import threading

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()
# Configurar el reconocedor de voz
recognizer = sr.Recognizer()

# Configurar el clasificador de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Variable para controlar si ya se ha dicho "Hola" o no
said_hello = False
# Variable para controlar la detección de rostros
detect_faces = True
# Temporizador para controlar la detección de rostros después de hablar
last_response_time = time.time()

# Función para decir "Hola"
def say_hello():
    engine.say("Hola, ¿En que puedo ayudarte?")
    engine.runAndWait()

# Función para mostrar imagen
def mostrar_img(imga):
    img = cv2.imread(imga)
    print("Informacion :D")
    cv2.imshow("Foto", img)
    cv2.waitKey(1)

# Función para escuchar la respuesta del usuario
def listen_response():
    with sr.Microphone() as source:
        print("Di algo...")
        try:
            audio = recognizer.listen(source, timeout=5)
            response = recognizer.recognize_google(audio, language='es-ES')
            print("Usuario dijo:", response)
            return response
        except sr.WaitTimeoutError:
            print("No se detectó ningún habla.")
            return None
        except sr.UnknownValueError:
            print("No se pudo entender el habla.")
            return None

# Función para elegir una respuesta aleatoria según la opción seleccionada
def choose_response(option):
    if any(keyword in option for keyword in ['hola', 'rogelio', 'saludo']):
        mostrar_img("qrU.png")
        return random.choice(["Qué bien!", "Genial!", "Me alegro!"])
    elif 'servicio' in option:
        return "Mostrando QR del servicio social."
    else:
        return "Lo siento, no entendí. Por favor, elige una opción válida."

# Función para la detección de rostros
def face_detection():
    global detect_faces, said_hello, last_response_time
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if detect_faces:
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) > 0:
                if not said_hello:
                    say_hello()
                    said_hello = True
                    detect_faces = False
                    last_response_time = time.time()

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Función para el reconocimiento de voz y el asistente de voz
def voice_recognition_and_assistant():
    global detect_faces, last_response_time
    while True:
        if not detect_faces:
            response = listen_response()
            if response:
                response_lower = response.lower()
                if 'hola' in response_lower or 'rogelio' in response_lower or 'saludo' in response_lower:
                    chosen_response = choose_response(response_lower)
                    engine.say(chosen_response)
                    engine.runAndWait()
                elif 'servicio' in response_lower:
                    print("Mostrando QR del servicio social.")
                else:
                    engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                    engine.runAndWait()
                detect_faces = True
                last_response_time = time.time()

# Iniciar hilos
face_thread = threading.Thread(target=face_detection)
voice_thread = threading.Thread(target=voice_recognition_and_assistant)

# Iniciar los hilos
face_thread.start()
voice_thread.start()

# Esperar
#
# ñ
# a que los hilos terminen (esto no será alcanzado en este caso)
face_thread.join()
voice_thread.join()
