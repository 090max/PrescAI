import nltk
import sys
sys.path.append('..')
from speech_text.google_rec import GoogleRecognizer

def preprocess(string):
    
    #tokenizing
    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer("[a-zA-Z@0-9]+")
    word_list=tokenizer.tokenize(string.lower())

    #stopword removal
    from nltk.corpus import stopwords
    sw  = set(stopwords.words('english'))
    useful_words = [w for w in word_list if w not in sw]

    #stemming
    important_words=[]
    from nltk.stem.snowball import PorterStemmer
    ps = PorterStemmer()
    for i in range(len(useful_words)):
        important_words.append(ps.stem(useful_words[i]))
        
    ## Lemmatization
    final_words=[]
    from nltk.stem import WordNetLemmatizer
    wn = WordNetLemmatizer()
    for i in range(len(important_words)):
            final_words.append(wn.lemmatize(important_words[i]))    
            
    return final_words


converter=GoogleRecognizer()
resp=converter.get_response()
if(resp is not None):
    print(resp)
    output=preprocess(resp)
    print(output)
else:
    print("error occured")


