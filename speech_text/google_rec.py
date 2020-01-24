
# libraries used in voice recognition and web 

import speech_recognition as sr
import webbrowser as wb


# libraries for removing stopwards and apply part of speech tagging used in extrat function

import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer


# libraries used for delay

import time
 
# Making instances for recognizing the voice 

r = sr.Recognizer()

# Making sure that from where the Input came from

def name(res_tag):
    name = ""
    age = ""
    gender = ""
    name   = [word for word, tag in tagged if tag == 'NNP']
    age    = [integer for word, tag in tagged if tag == 'CD']
    gender = [gen for word, tag in tagged if tag == 'NN']
    
'''def symptoms(res_tag):
    

def diagnosis(res_tag):
    
    
def prescription(res_tag):
    

def advice(res_tag):'''

    

def extract(res):
    
    stop_words = set(stopwords.words('english')) 
    
    tokenized = sent_tokenize(res)       
    
    wordsList = nltk.word_tokenize(res) 
  
    # removing stop words from wordList 
    wordsList = [w for w in wordsList if not w in stop_words]  
  
    #  Using a Tagger. Which is part-of-speech  
    # tagger or POS-tagger.  
    tagged = nltk.pos_tag(wordsList) 
  
    print(tagged) 
    return tagged
    
def mainfunction(source):
    
    time.sleep(3)
    print("Speak Now...")
    
    audio = r.listen(source)
    
    res = ""
    res = r.recognize_google(audio)
    
    res_tag = extract(res)
    
    if 'name' in res or 'Name' in res:
        name(res_tag)
    
    elif 'symptom' in res or 'symptoms' in res:
        symptoms(res_tag)
    
    elif 'diagnosis' in res or 'Diagnosis' in res:
        diagnosis(res_tag)
    
    elif 'prescription' in res or 'Prescription' in res:
        prescription(res_tag)
    
    elif 'advice' in res or 'Advice' in res:
        advice(res_tag)
    

with sr.Microphone() as source:
    
    while 1:
        mainfunction(source)

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
