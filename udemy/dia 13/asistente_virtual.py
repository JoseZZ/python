import datetime
import webbrowser

import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import yfinance


# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    reconocimiento = sr.Recognizer()
    # Configurar el micrófono
    with sr.Microphone() as fuente:
        # tiempo de espera
        reconocimiento.pause_threshold = 0.7
        # iniciar el reconocimiento
        print("Escuchando...")
        reconocimiento.adjust_for_ambient_noise(fuente, duration=1)
        audio = reconocimiento.listen(fuente)
        try:
            # reconocer el audio y buscar en google
            print("Reconociendo...")
            texto = reconocimiento.recognize_google(audio, language='es-ES')
            # mostrar el texto reconocido
            print(f"Usuario: {texto}")
            # devolver el texto
            return texto
        except sr.UnknownValueError:
            print("No te he entendido")
            return "Sigo esperando"
        except sr.RequestError:
            print("Error de conexión")
            return "Sigo esperando"
        except:
            print("Error desconocido")
            return "Sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(texto):
    # inicializar el motor de texto a voz
    engine = pyttsx3.init()
    # pronuncia el mensaje
    engine.say(texto)
    engine.runAndWait()


# funcion para informar el dia de la semana
def informar_dia_semana():
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    calendario = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"}
    # informar al usuario
    hablar(f"Hoy es {calendario[dia_semana]}")


# funcion para informar la hora actual
def informar_hora():
    hora = datetime.datetime.now()
    hora_actual = hora.strftime("%H:%M")
    # informar al usuario
    hablar(f"Son las {hora_actual}")


# funcion para saludo inicial
def saludo_inicial():
    # obtener la hora actual
    hora = datetime.datetime.now()
    if hora.hour < 12:
        saludo = "Buenos días"
    elif hora.hour < 18:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"

    # informar al usuario
    hablar(f"{saludo}. soy Lola, tu asistente virtual. ¿En qué puedo ayudarte hoy?")
    print("Hola, soy Lola, tu asistente virtual. ¿En qué puedo ayudarte hoy?")  # Para mostrar en consola


# funcion principal del asistente
def asistente_virtual():
    saludo_inicial()
    while True:
        # escuchar al usuario
        texto = transformar_audio_en_texto().lower()
        # procesar la solicitud del usuario
        if "buscar en youtube" in texto:
            hablar("¿Qué quieres buscar en YouTube?")
            busqueda = transformar_audio_en_texto().lower()
            if busqueda != "Sigo esperando":
                webbrowser.open(f"https://www.youtube.com/results?search_query={busqueda}")
        elif "buscar en google" in texto:
            hablar("¿Qué quieres buscar en Google?")
            busqueda = transformar_audio_en_texto().lower()
            if busqueda != "Sigo esperando":
                webbrowser.open(f"https://www.google.com/search?q={busqueda}")
        elif "que día es hoy" in texto:
            informar_dia_semana()
        elif "hora" in texto:
            informar_hora()
        elif "buscar en wikipedia" in texto:
            hablar("Buscando en wikipedia")
            texto = texto.replace('buscar en wikipedia', '')
            wikipedia.set_lang('es')
            busqueda = wikipedia.summary(texto, sentences=1)
            hablar("Wikipedia dice lo siguiente:")
            hablar(busqueda)
        elif "busca en internet" in texto:
            hablar("Estoy buscando")
            texto = texto.replace('busca en internet', '')
            pywhatkit.search(texto)
            hablar("Esto es lo que he encontrado")
        elif "reproduce" in texto:
            hablar("Reproduciendo música")
            texto = texto.replace('reproduce', '')
            pywhatkit.playonyt(texto)
        elif "chiste" in texto:
            hablar(pyjokes.get_joke("es"))
        elif "precio de las acciones" in texto:
            accion = texto.split("de")[-1].strip()
            cartera = {
                "apple": "APPL",
                "google": "GOOGL",
                "amazon": "AMZN",
                "microsoft": "MSFT"
            }
            try:
                accion_buscada = cartera[accion.lower()]
                accion_buscada = yfinance.Ticker(accion_buscada)
                precio = accion_buscada.info["regularMarketPrice"]
                hablar(f"El precio de las acciones de {accion} es {precio} dólares")
            except KeyError:
                hablar("Lo siento, no tengo información sobre esa acción.")

        elif "adiós" in texto or "hasta luego" in texto:
            hablar("Hasta luego, que tengas un buen día")
            break
        else:
            hablar("Lo siento, no he entendido tu solicitud. ¿Puedes repetirlo?")


asistente_virtual()
