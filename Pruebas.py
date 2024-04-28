import cv2
import pyttsx3
import speech_recognition as sr
import random
import time

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


# Función para escuchar la respuesta del usuario
def listen_response():
    with sr.Microphone() as source:
        print("Di algo...")
        try:
            audio = recognizer.listen(source, timeout=2)
            response = recognizer.recognize_google(audio, language='es-ES')
            print("Usuario dijo:", response)
            response_lower = response.lower()
            if 'servicio' in response_lower:
                return response, True  # Devolver la respuesta y un indicador de servicio
            else:
                return response, False
        except sr.WaitTimeoutError:
            print("No se detectó ningún habla.")
            return None, False
        except sr.UnknownValueError:
            print("No se pudo entender el habla.")
            return None, False

# Función para elegir una respuesta aleatoria según la opción seleccionada

def choose_response(option):
    if any(keyword in option for keyword in ['hola', 'rogelio', 'saludo']):
        return random.choice(["Qué bien!", "Genial!", "Me alegro!"])
    elif 'servicio' in option:
        return "Mostrando QR del servicio social."
    else:
        return "Lo siento, no entendí. Por favor, elige una opción válida."


# Capturar video desde la cámara
cap = cv2.VideoCapture(0)
while True:
    # Leer el fotograma
    ret, frame = cap.read()
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if detect_faces:
        # Detectar rostros solo si detect_faces es True
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            # Decir "Hola" si se detecta un rostro
            if not said_hello:
                say_hello()
                said_hello = True
                detect_faces = False  # Detener la detección de rostros
                last_response_time = time.time()  # Registrar el tiempo de respuesta

                # Esperar respuesta del usuario
                response, is_service = listen_response()
                if response:
                    if is_service:
                        # Realizar la acción correspondiente al servicio
                        # Aquí puedes agregar el código para la acción que deseas realizar
                        print("Mostrando QR en pantalla.")
                    else:
                        response_lower = response.lower()
                        if 'hola' in response_lower or 'rogelio' in response_lower or 'saludo' in response_lower:
                            chosen_response = choose_response(response_lower)
                            engine.say(chosen_response)
                            engine.runAndWait()
                        else:
                            engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                            engine.runAndWait()
    else:
        # Verificar si ha pasado el tiempo de espera (10 segundos)
        if time.time() - last_response_time >= 2:
            detect_faces = True

    # Dibujar un rectángulo alrededor de cada rostro detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Mostrar el fotograma con los rectángulos de detección de rostros
    cv2.imshow('Face Detection', frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
