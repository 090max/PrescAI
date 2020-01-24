
# libraries used in voice recognition and web 

import speech_recognition as sr
import webbrowser as wb

# libraries used for delay

import time
 
# Making instances for recognizing the voice 

r = sr.Recognizer()

<<<<<<< HEAD
        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with microphone as source:
            # recognizer.adjust_for_ambient_noise(source)  # #  analyze the audio source for 1 second
            audio = recognizer.listen(source)
=======
# Making sure that from where the Input came from
>>>>>>> 36588693f7817964bc5857f5d0625ff5dc9ba6a0

def name():
    with sr.Microphone() as source:
        print("enter the name\n")
        sym = r.listen(source)
        time.sleep(2)
    result = r.recognize_google(sym)
    data['name'].append(result)
    print(data)
    mainfunction()
    
def symptoms():
    check=""
    while True:
        r = sr.Recognizer()
        if(len(check)==0):
            print("BEGIN...\n")
        
        with sr.Microphone() as source:
            print("enter the symptoms\n")
            sym = r.listen(source)
            time.sleep(2)
        result = r.recognize_google(sym)
        check = result.lower()
                
        if 'exit' in check:
            mainfunction()
            break
        else:
            data['symptoms'].append(result)
            print(data)
            
def diagnosis():
    check=""
    while True:
        r = sr.Recognizer()
        if(len(check)==0):
            print("BEGIN...\n")
        
        with sr.Microphone() as source:
            print("enter the diagnosis\n")
            sym = r.listen(source)
            time.sleep(2)
        result = r.recognize_google(sym)
        check = result.lower()
                
        if 'exit' in check:
            mainfunction()
            break
        else:
            data['diagnosis'].append(result)
            print(data)
    
    
def prescription():
    check=""
    while True:
        r = sr.Recognizer()
        if(len(check)==0):
            print("BEGIN...\n")
        
        with sr.Microphone() as source:
            print("enter the prescription\n")
            sym = r.listen(source)
            time.sleep(2)
        result = r.recognize_google(sym)
        check = result.lower()
                
        if 'exit' in check:
            mainfunction()
            break
        else:
            data['prescription'].append(result)
            print(data)
    

def advice():
    check=""
    while True:
        r = sr.Recognizer()
        if(len(check)==0):
            print("BEGIN...\n")
        
        with sr.Microphone() as source:
            print("enter the advice\n")
            sym = r.listen(source)
            time.sleep(2)
        result = r.recognize_google(sym)
        check = result.lower()
                
        if 'exit' in check:
            mainfunction()
            break
        else:
            data['advice'].append(result)
            print(data)

    
def mainfunction():
    print("What do you want to Enter:\n" + "Name\n" + "Symptoms\n" + "Diagnosis\n" + "Prescription\n" + "Advice\n")
    with sr.Microphone() as source:
        audio = r.listen(source)
    res = r.recognize_google(audio)
    res = res.lower()
    keywords(res)
    
    
def keywords(key):    
    if 'name' in key:
        name()
    
    elif 'symptom' in key:
        key = symptoms()
        
    elif 'diagnosis' in key:
        diagnosis()
    
    elif 'prescription' in key:
        prescription()
    
    elif 'advice' in key:
        advice()
    
data = {'name': [],
        'symptoms': [],
        'diagnosis': [],
        'prescription': [],
        'advice': []
        }

mainfunction()

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
