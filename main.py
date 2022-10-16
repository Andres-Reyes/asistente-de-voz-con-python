import speech_recognition as asistente
import pyttsx3
engine = pyttsx3.init()
engine.say("Bienvenido a embioecol en que puedo ayudarte")
engine.runAndWait()


r = asistente.Recognizer()

with asistente.Microphone() as source:
    print("por favor habla")
    audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language="es")
        print(texto)
        engine.say(texto)
        engine.runAndWait()
    except:
        print("no te pude entender")
