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
    engine.say("Bienvenido al sistema de asistencia de Posgrado")
    print("Bienvenido al sistema de asistencia de Posgrado")
    engine.say("¿En que puedo ayudarte?")
    print("¿En que puedo ayudarte?")
    engine.say("Selecciona una de las siguientes opciones:")
    print("Selecciona una de las siguientes opciones:")
    engine.say("1: Mapa de posgrado")
    print("1: Mapa de posgrado")
    engine.say("2: Posgrado")
    print("2: Posgrado")
    engine.say("3: Titulacion")
    print("3: Titulacion")
    engine.say("4: Servicio")
    print("4: Servicio")
    engine.say("5: Residencias")
    print("5: Residencias")
    engine.say("6: Salir")
    print("6: Salir\n")
    engine.runAndWait()

#def say_bye():
#    engine.say("¿Te gustaria salir del sistema?")
#    engine.say("Selecciona una de las siguientes opciones:")
#    engine.say("1: Salir")
#    print("1: Salir")
#    engine.say("2: Volver a menu")
#    print("2: Volver a menu")

def mostrar_img(imga):
    img = cv2.imread(imga)  # Leemos el archivo almacenado en la carpeta local con el nombre indicado
    cv2.imshow("Foto", img)  # Mostramos una ventana con el nombre de Foto y lo almacenado en img
    cv2.waitKey(1)

# Función para escuchar la respuesta del usuario
def listen_response():
    with sr.Microphone() as source:
        print("Di algo...")
        try:
            audio = recognizer.listen(source, phrase_time_limit=5)
            response = recognizer.recognize_google(audio, language='es-ES')
            print("Usuario dijo:", response)
            response_lower = response.lower()
            return response
        except sr.WaitTimeoutError:
            return "No se detectó nada"
        except sr.UnknownValueError:
            return "No se detectó nada"

# Función para elegir una respuesta aleatoria según la opción seleccionada

 # def choose_response(option):
 #   if any(keyword in option for keyword in ['hola', 'rogelio', 'saludo']):
 #       return random.choice(["Qué bien!", "Genial!", "Me alegro!"])
 #   elif 'servicio' in option:
 #       return "Mostrando QR del servicio social."
 #   else:
 #       return "Lo siento, no entendí. Por favor, elige una opción válida."

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
                response = listen_response()
                if response:
                    if 'mapa de posgrado' in response.lower():
                        engine.say("Has seleccionado Mapa de Posgrado")
                        engine.say("Se mostrará el mapa de posgrado en la pantalla")
                        engine.runAndWait()
                        print("Has seleccionado Mapa de Posgrado.\n")
                        mostrar_img("Croquis.png")
                        said_hello = False
                    elif 'posgrado' in response.lower():
                        engine.say("Has seleccionado posgrado")
                        engine.say("Se mostrará un QR en la pantalla")
                        engine.runAndWait()
                        print("Has seleccionado Posgrado.\n")
                        mostrar_img("Posgrado.jpeg")
                        said_hello = False
                    elif 'titulación' in response.lower():
                        engine.say("Has seleccionado titulación")
                        engine.say("Se mostrará un QR en la pantalla")
                        engine.runAndWait()
                        print("Has seleccionado Titulación.\n")
                        mostrar_img("Titulacion.jpeg")
                        said_hello = False
                    elif 'servicio' in response.lower():
                        engine.say("Has seleccionado servicio")
                        engine.say("Se mostrará un QR en la pantalla")
                        engine.runAndWait()
                        print("Has seleccionado Servicio Social.\n")
                        mostrar_img("Servicio.jpeg")
                        said_hello = False
                    elif 'residencias' in response.lower():
                        engine.say("Has seleccionado residencias")
                        engine.say("Se mostrará un QR en la pantalla")
                        engine.runAndWait()
                        print("Has seleccionado Residencias.\n")
                        mostrar_img("Residencias.jpeg")
                        said_hello = False
                    elif 'salir' in response.lower():
                        engine.say("Has seleccionado salir")
                        engine.runAndWait()
                        print("Has seleccionado salir.\n")
                        break
                    else:
                        print("No se reconoció la opción.\n")
                        engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                        engine.runAndWait()
                        said_hello = False
                        #response_lower = response.lower()
                        #if 'hola' in response_lower or 'rogelio' in response_lower or 'saludo' in response_lower:
                            #chosen_response = choose_response(response_lower)
                            #engine.say(chosen_response)
                            #engine.runAndWait()
                    # Resetear la variable said_hello para que el programa pueda decir "Hola" de nuevo
            
                #say_bye()
                #last_response_time = time.time()  # Registrar el tiempo de respuesta

                # Esperar respuesta del usuario
                #response = listen_response()
                #if response:
                #   if 'salir' in response[0].lower():
                #       print("Has seleccionado salir.")
        #                break
                #   elif 'volver al menu' in response.lower():
                #       print("Has seleccionado volver al menu.")
                        # Resetear la variable said_hello para que el programa pueda decir "Hola" de nuevo
                #       said_hello = False
                #   else:
                #       print("No se reconoció la opción.")
                #       engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                #       engine.runAndWait()
                        
    else:
        # Verificar si ha pasado el tiempo de espera (5 segundos)
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
    
engine.say("Gracias por su visita")
engine.runAndWait()
print("Bye")
# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
