import cv2
import pyttsx3
import speech_recognition as sr
import random

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()
# Configurar el reconocedor de voz
recognizer = sr.Recognizer()
# Configurar el clasificador de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Variable para controlar si ya se ha dicho "Hola" o no
said_hello = False


# Función para decir "Hola"
def say_hello():
    engine.say("Hola, ¿cómo estás?")
    engine.runAndWait()


# Función para escuchar la respuesta del usuario
def listen_response():
    with sr.Microphone() as source:
        print("Di algo...")
        try:
            audio = recognizer.listen(source, timeout=5)
            response = recognizer.recognize_google(audio, language='es-ES')
            return response
        except sr.WaitTimeoutError:
            print("No se detectó ningún habla.")
            return None
        except sr.UnknownValueError:
            print("No se pudo entender el habla.")
            return None


# Función para elegir una respuesta aleatoria según la opción seleccionada
def choose_response(option):
    if option == 'hola':
        return random.choice(["Qué bien!", "Genial!", "Me alegro!"])
    elif option == 'rogelio':
        return random.choice(["Qué lástima!", "Oh no!", "Es una pena!"])
    elif option == 'saludo':
        return random.choice(["Interesante!", "Vaya!", "Qué curioso!"])
    else:
        return "Lo siento, no entendí. Por favor, elige una opción válida."


# Capturar video desde la cámara
cap = cv2.VideoCapture(1)
while True:
    # Leer el fotograma
    ret, frame = cap.read()
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detectar rostros
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        # Decir "Hola" si se detecta un rostro
        if not said_hello:
            say_hello()
            said_hello = True
            # Esperar respuesta del usuario
            response = listen_response()
            if response:
                print("Usuario dijo:", response)
                response_lower = response.lower()
                if 'hola' in response_lower or 'rogelio' in response_lower or 'saludo' in response_lower:
                    chosen_response = choose_response(response_lower)
                    engine.say(chosen_response)
                    engine.runAndWait()
                else:
                    engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                    engine.runAndWait()
    else:
        # Reiniciar la variable said_hello si no se detectan rostros
        said_hello = False

    # Dibujar un rectángulo alrededor de cada rostro detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Mostrar el fotograma con los rectángulos de detección de rostros
    cv2.imshow('Face Detection', frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
# CHECAR ACERCAMIENTO Y CHECAR ENCUADRE DE LA PERSONA, PERSONALIZADO AL USUARIO QUE ESTE ENFRENTE.
# PONER VARIOS PARAMETROS DE INICIO.
# IDENTIFICAR TAMBIEN QUE HABLE, VER IS ESTA HBALANDO TAMBIEN PARA PODER INICIAR LA INTERACCION.
# USADO EN UNA OFICINA, O EN EL R(POSGRADO) EN OFICNAS DE PROFESORES
# O TAMBIEN EN ADMINISTRACION, PARA VISUALIZAR QUE SE HACE EN CADA UNO DE LOS APARTADOS.


# QUIERO PAGAR UNA CONSTANCIA --> EL PAGO LO PUEDES REALIZAR AQUI Y TIENE UN COSTO DE CIERTO CASO.

# TENER UNA BARAJA DE OPCIONES.

# CONSIDEARAR EL AMBIENTE DEL R, SERVICIOS DE SERVICIO SOCIAL O POSGRADO EN SI O BUSCANDO UN PROFESOR COMO UN MAPA TAMBIEN
# UN SISTEMA CONECTADO Y FUNCIONANDO CON EXTERNOS.

# INTERACCION SENCILLA DEPENDIENDO DE LA INFORMACION.
