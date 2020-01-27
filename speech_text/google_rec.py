import speech_recognition as sr
import time


def speech_to_text(tag):
    with sr.Microphone() as source:
        try:
            r = sr.Recognizer()
            time.sleep(2)
            print("Speak Now...",tag)
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=4)
            res = r.recognize_google(audio)
            return res
        except ValueError as err:
            print(err)
        except Exception as ex:
            print(ex)
