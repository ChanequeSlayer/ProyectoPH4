# Descripción: Este programa permite la interacción con el usuario mediante comandos de voz y la detección de rostros.
# Se muestra un menú con opciones que el usuario puede seleccionar mediante comandos de voz.
# Se muestra una imagen en pantalla según la opción seleccionada.
# Se permite al usuario seleccionar si desea salir o volver al menú principal.
# Autor: José Pablo Aguirre Rivera
#        Alexia Sarahí Mireles Maldonado
#        Omar Quiñonez Esparza
#        Alan Jesús Montes Silva
#        Victor Andres Garduño Ramos
# Fecha: 03 de mayo de 2024

''
# Se importan las librerías necesarias para el funcionamiento del programa
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

# Función para dar la binvenida al usuario y mostrar las opciones
def say_hello():
    engine.say("Bienvenido al sistema de asistencia de Posgrado")
    print("Bienvenido al sistema de asistencia de Posgrado")
    engine.say("¿En que puedo ayudarte?")
    print("¿En que puedo ayudarte?")
    engine.say("Selecciona una de las siguientes opciones:")
    print("Selecciona una de las siguientes opciones:")
    engine.say("1: Mapa del edificio")
    print("1: Mapa del edificio")
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

# Función para dar la binvenida al usuario y mostrar las opciones
def say_bye():
    engine.say("¿Te sirvio la información?")
    print("¿Te sirvio la información?")
    engine.say("Selecciona una de las siguientes opciones:")
    print("Selecciona una de las siguientes opciones:")
    engine.say("1: Salir")
    print("1: Salir")
    engine.say("2: Volver al menu")
    print("2: Volver al menu\n")
    engine.runAndWait()

def mostrar_fondo():
    img = cv2.imread("lastBack.jpeg")  # Leemos el archivo almacenado en la carpeta local con el nombre indicado

    # Creamos una ventana con el nombre "Foto" y configuramos para que sea pantalla completa
    cv2.namedWindow("fondo", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("fondo", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Mostramos la imagen centrada en la ventana
    cv2.imshow("fondo", img)



# Función para mostrar una imagen en pantalla
def mostrar_img(imga,tipo):
    img = cv2.imread(imga)  # Leemos el archivo almacenado en la carpeta local con el nombre indicado
    if tipo == 1:
        print("Paso por aqui")
        # Creamos una ventana con el nombre "Foto" y configuramos para que sea pantalla completa
        cv2.namedWindow("Foto", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Foto", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Mostramos la imagen centrada en la ventana
        cv2.imshow("Foto", img)

        cv2.waitKey(20000)  # Esperamos 1 minuto (60,000 milisegundos)
        cv2.destroyWindow("Foto")  # Cerramos la ventana del codigo QR y del mapa en si.
    elif tipo == 2:
        print("Paso por aca.")
        img = cv2.imread(imga)

        # Obtener las dimensiones de la imagen
        height, width, _ = img.shape

        # Crear una ventana con el nombre "Imagen con QR"
        cv2.namedWindow("qr", cv2.WINDOW_NORMAL)

        # Redimensionar la ventana para que coincida con el tamaño de la imagen
        cv2.resizeWindow("qr", width, height)

        # Mostramos la imagen centrada en la ventana
        cv2.imshow("qr", img)

        cv2.waitKey(20000)  # Esperamos 1 minuto (60,000 milisegundos)
        cv2.destroyWindow("qr")  # Cerramos la ventana del codigo QR y del mapa en si.
    elif tipo == 3:
        img = cv2.imread(imga)

        # Obtener las dimensiones de la imagen
        height, width, _ = img.shape

        # Crear una ventana con el nombre "Imagen con QR"
        cv2.namedWindow("estado", cv2.WINDOW_NORMAL)

        # Redimensionar la ventana para que coincida con el tamaño de la imagen
        cv2.resizeWindow("estado", width, height)

        cv2.moveWindow("estado", 0, 0)

        # Mostramos la imagen centrada en la ventana
        cv2.imshow("estado", img)
    else:
        print("Paso por aca.")
        img = cv2.imread(imga)

        # Obtener las dimensiones de la imagen
        height, width, _ = img.shape

        # Crear una ventana con el nombre "Imagen con QR"
        cv2.namedWindow("menu", cv2.WINDOW_NORMAL)

        # Redimensionar la ventana para que coincida con el tamaño de la imagen
        cv2.resizeWindow("menu", width, height)

        cv2.moveWindow("estado", 50, 50)

        # Mostramos la imagen centrada en la ventana
        cv2.imshow("menu", img)









# Función para escuchar la respuesta del usuario
def listen_response():
    # Escucha la respuesta del usuario
    with sr.Microphone() as source:
        print("Di algo...")
        engine.say("Te escucho...")
        try:
            # Escuchar la respuesta del usuario durante 5 segundos
            audio = recognizer.listen(source, phrase_time_limit=5)
            # Convierte la respuesta a texto 
            response = recognizer.recognize_google(audio, language='es-ES')
            # Imprimir la respuesta del usuario
            print("Usuario dijo:", response)
            # Actualizar el tiempo de la última respuesta
            response_lower = response.lower()
            # Actualizar el tiempo de la última respuesta
            return response
        # Manejo de errores    
        except sr.WaitTimeoutError:
            return "No se detectó nada"
        except sr.UnknownValueError:
            return "No se detectó nada"

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)
start_time = None

mostrar_fondo()


#PRIMERA PARTE, ESTO LO PUEDO DECIR YO, O TU, COMO QUIERAS.


while True:
    mostrar_img("analizandoD.jpeg", 3)
    # Leer el fotograma
    ret, frame = cap.read()
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if detect_faces:
        # Detectar rostros solo si detect_faces es True
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            # Si es la primera vez que se detecta un rostro, registrar el tiempo
            if start_time is None:
                start_time = time.time()
            else:
                # Calcular la duración desde que se detectó el rostro
                duration = time.time() - start_time
                # Mostrar el mensaje después de 5 segundos
                if duration >= 5:
                    # Dar la binevenida si se detecta un rostro
                    respuesta = True
                    if not said_hello:
                        cv2.destroyWindow("estado")  # Cerramos la ventana del codigo QR y del mapa en si.z
                        mostrar_img("buscandoD.jpeg", 3)
                        mostrar_img("menusD.jpeg", 4)
                        say_hello()  # Dar la bienvenida y mostrar las opciones
                        salir = False  # Variable para controlar si se selecciona salir
                        said_hello = True  # Actualizar la variable para no volver a dar la bienvenida
                        detect_faces = False  # Detener la detección de rostros
                        # Esperar respuesta del usuario
                        response = listen_response()
                        # Verificar si se detectó una respuesta
                        if response:
                            cv2.destroyWindow("estado")  # Cerramos la ventana del codigo QR y del mapa en si.z
                            mostrar_img("esperandoD.jpeg", 3)
                            # Verificar la respuesta del usuario
                            if 'mapa del edificio' in response.lower():
                                # Mostrar el mapa del edificio
                                engine.say("Has seleccionado Mapa del edificio")
                                engine.say("Se mostrará el mapa del edificio en la pantalla")
                                engine.runAndWait()
                                print("Has seleccionado Mapa del edificio.\n")
                                # Mostrar la imagen del mapa del edificio
                                mostrar_img("lastCroquis.jpeg", 1)
                                # Actualizar la variable para no volver a dar la bienvenida
                                time.sleep(5)
                                cv2.destroyWindow("estado")  # Cerramos la ventana del codigo QR y del mapa en si.z

                                while respuesta:
                                    # Preguntar si se desea salir o volver al menú
                                    say_bye()
                                    response = listen_response()
                                    if response:
                                        cv2.destroyWindow("menu")  # Cerramos la ventana del codigo QR y del mapa en si.
                                        if "salir" in response.lower():
                                            engine.say("Has seleccionado salir")
                                            engine.runAndWait()
                                            print("Has seleccionado salir.\n")
                                            respuesta = False
                                            salir = True
                                            break
                                        elif "volver al menú" in response.lower():
                                            engine.say("Has seleccionado volver al menu")
                                            engine.runAndWait()
                                            print("Has seleccionado volver al menu.\n")
                                            said_hello = False
                                            start_time = None
                                            break
                                        else:
                                            print("No se reconoció la opción.\n")
                                            engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                                            engine.runAndWait()
                            elif 'posgrado' in response.lower():
                                engine.say("Has seleccionado posgrado")
                                engine.say("Se mostrará un QR en la pantalla")
                                engine.runAndWait()
                                print("Has seleccionado Posgrado.\n")
                                mostrar_img("Posgrado.jpeg", 2)
                                said_hello = False
                                time.sleep(5)
                                cv2.destroyWindow("estado")  # Cerramos la ventana del codigo QR y del mapa en si.z

                                while respuesta:
                                    say_bye()
                                    response = listen_response()
                                    if response:

                                        if "salir" in response.lower():
                                            engine.say("Has seleccionado salir")
                                            engine.runAndWait()
                                            print("Has seleccionado salir.\n")
                                            respuesta = False
                                            salir = True
                                            break
                                        elif "volver al menú" in response.lower():
                                            engine.say("Has seleccionado volver al menu")
                                            engine.runAndWait()
                                            print("Has seleccionado volver al menu.\n")
                                            said_hello = False
                                            start_time = None
                                            break
                                        else:
                                            print("No se reconoció la opción.\n")
                                            engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                                            engine.runAndWait()
                            elif 'titulación' in response.lower():
                                engine.say("Has seleccionado titulación")
                                engine.say("Se mostrará un QR en la pantalla")
                                engine.runAndWait()
                                print("Has seleccionado Titulación.\n")
                                mostrar_img("Titulacion.jpeg", 2)
                                said_hello = False
                                time.sleep(5)
                                cv2.destroyWindow("estado")  # Cerramos la ventana del codigo QR y del mapa en si.z

                                while respuesta:
                                    say_bye()
                                    response = listen_response()
                                    if response:
                                        cv2.destroyWindow("menu")  # Cerramos la ventana del codigo QR y del mapa en si.
                                        if "salir" in response.lower():
                                            engine.say("Has seleccionado salir")
                                            engine.runAndWait()
                                            print("Has seleccionado salir.\n")
                                            respuesta = False
                                            salir = True
                                            break
                                        elif "volver al menú" in response.lower():
                                            engine.say("Has seleccionado volver al menu")
                                            engine.runAndWait()
                                            print("Has seleccionado volver al menu.\n")
                                            said_hello = False
                                            start_time = None
                                            break
                                        else:
                                            print("No se reconoció la opción.\n")
                                            engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                                            engine.runAndWait()
                            elif 'servicio' in response.lower():
                                engine.say("Has seleccionado servicio")
                                engine.say("Se mostrará un QR en la pantalla")
                                engine.runAndWait()
                                print("Has seleccionado Servicio Social.\n")
                                mostrar_img("Servicio.jpeg", 2)
                                said_hello = False
                                time.sleep(5)
                                cv2.destroyWindow("estado")  # Cerramos la ventana del codigo QR y del mapa en si.z

                                while respuesta:

                                    say_bye()
                                    response = listen_response()
                                    if response:
                                        cv2.destroyWindow("menu")  # Cerramos la ventana del codigo QR y del mapa en si.
                                        if "salir" in response.lower():
                                            engine.say("Has seleccionado salir")
                                            engine.runAndWait()
                                            print("Has seleccionado salir.\n")
                                            respuesta = False
                                            salir = True
                                            break
                                        elif "volver al menú" in response.lower():
                                            engine.say("Has seleccionado volver al menu")
                                            engine.runAndWait()
                                            print("Has seleccionado volver al menu.\n")
                                            said_hello = False
                                            start_time = None
                                            break
                                        else:
                                            print("No se reconoció la opción.\n")
                                            engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                                            engine.runAndWait()
                            elif 'residencias' in response.lower():
                                engine.say("Has seleccionado residencias")
                                engine.say("Se mostrará un QR en la pantalla")
                                engine.runAndWait()
                                print("Has seleccionado Residencias.\n")
                                mostrar_img("Residencias.jpeg", 2)
                                said_hello = False
                                time.sleep(5)
                                cv2.destroyWindow("estado")  # Cerramos la ventana del codigo QR y del mapa en si.z

                                while respuesta:
                                    say_bye()
                                    response = listen_response()
                                    if response:
                                        cv2.destroyWindow("menu")  # Cerramos la ventana del codigo QR y del mapa en si.
                                        if "salir" in response.lower():
                                            engine.say("Has seleccionado salir")
                                            engine.runAndWait()
                                            print("Has seleccionado salir.\n")
                                            respuesta = False
                                            salir = True
                                            break
                                        elif "volver al menú" in response.lower():
                                            engine.say("Has seleccionado volver al menu")
                                            engine.runAndWait()
                                            print("Has seleccionado volver al menu.\n")
                                            said_hello = False
                                            start_time = None
                                            break
                                        else:
                                            print("No se reconoció la opción.\n")
                                            engine.say("Lo siento, no entendí. Por favor, elige una opción válida.")
                                            engine.runAndWait()
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
                                time.sleep(5)
                                cv2.destroyWindow("estado")  # Cerramos la ventana del codigo QR y del mapa en si.
                    # Salir si se ha seleccionado salir
                    if salir:
                        break


    # Actualizar el tiempo de la última respuesta
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
# Despedirse del usuario
engine.say("Gracias por su visita")
engine.runAndWait()
print("Bye")
# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()