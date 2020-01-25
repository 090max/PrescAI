
# libraries used in voice recognition and web 

import speech_recognition as sr
import webbrowser as wb

# libraries used for delay

import time
import sys
 
# Making instances for recognizing the voice 

r = sr.Recognizer()

# Making sure that from where the Input came from

def name():
    with sr.Microphone() as source:
        print("enter the name\n")
        sym = r.listen(source, phrase_time_limit = 5)
        print(sym)
    result = r.recognize_google(sym)
    print(result)
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
            sym = r.listen(source, phrase_time_limit = 5)
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
            sym = r.listen(source, phrase_time_limit = 5)
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
            sym = r.listen(source, phrase_time_limit = 5)
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
            sym = r.listen(source, phrase_time_limit = 5)
        result = r.recognize_google(sym)
        check = result.lower()
                
        if 'exit' in check:
            mainfunction()
            break
        else:
            data['advice'].append(result)
            print(data)

    
def mainfunction():
    print("What do you want to Enter:\n" + "Name\n" + "Symptoms\n" + "Diagnosis\n" + "Prescription\n" + "Advice\n" + "Stop : To Stop the program\n")
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit = 3, timeout = 3)
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
    
    elif 'stop' in key:
        sys.exit()
    
data = {'name': [],
        'symptoms': [],
        'diagnosis': [],
        'prescription': [],
        'advice': []
        }

mainfunction()

