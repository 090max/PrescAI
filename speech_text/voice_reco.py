
import speech_recognition as sr

import time

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print('[search Edureka: and search Youtube]')
    print('Speak Now')
    # Using r3 instance to listen the audio signal using microphone
    
    while(True):
        print("in")
        time.sleep(2)

        try:
            print("Speak NOW ...")
            r3 = sr.Recognizer()
            audio = r3.listen(source,timeout=4)
            print(audio)
            hello = r3.recognize_google(audio)
            print(hello)
            if 'name' in hello:
                print("Name entered success")
            if 'symptom' in hello:
                print("Symptom entered sucess")
            if 'stop' in hello or 'Stop' in hello:
                break
        except Exception as ex:
            print(ex)
        except ValueError as err:
            print(err)

# Now converting audio signal recorded into text using API(recognize_google)

'''if 'Youtube' or 'youtube' in hello:
    url = 'https://www.youtube.com/'
    url = url + 'results?search_query=garmi'
    with sr.Microphone() as source:s
        print('Serach Your Query')
        audio = r2.listen(source)
        
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        
        except sr.UnknownValueError:
            print('error')
       
        except sr.RequestError as e:
            print('failed'.format(e))'''