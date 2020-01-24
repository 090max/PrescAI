import nltk
import sys

sys.path.append('..')
import spacy

spacy_nlp_sci = spacy.load('en_core_sci_md')
spacy_nlp_en = spacy.load('en')


def Remove_stopwords(string):
    # tokenizing
    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer("[a-zA-Z@0-9]+")
    word_list = tokenizer.tokenize(string.lower())

    # stopword removal
    from nltk.corpus import stopwords
    sw = set(stopwords.words('english'))
    sw.remove("no")
    useful_words = [w for w in word_list if w not in sw]
    return useful_words


def process_cont(tokenized):
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            print("words....", words)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))


def get_pos_tags_en(text, rem_stopwords=1):
    final_text = text.lower()
    if (rem_stopwords == 1):
        processed_text = Remove_stopwords(text)
        final_text = " ".join(processed_text)
    words = spacy_nlp_sci(final_text)
    arr = [(w.text, w.tag_) for w in words]
    named_entity = [(w.text, w.label_) for w in words.ents]
    return arr, named_entity


def get_pos_tags_sci(text, rem_stopwords=1):
    final_text = text.lower()
    if (rem_stopwords == 1):
        processed_text = Remove_stopwords(text)
        final_text = " ".join(processed_text)
    words = spacy_nlp_sci(final_text)
    arr = [(w.text, w.tag_) for w in words]
    named_entity = [(w.text, w.label_) for w in words.ents]
    return arr, named_entity


def sypmptom(text):

    arr,named_entity=get_pos_tags_sci(text)
    print(arr)
    print(named_entity)

    dict = {}
    sym = []
    duration = []
    time_list = ['day', 'days', 'week', 'weeks', 'month', 'months', 'year', 'years']

    for i in range(len(arr)):
        dict[arr[i][0]] = arr[i][1]
        if (arr[i][1] == "CD"):
            duration.append(arr[i][0])
        if (arr[i][0] in time_list):
            duration.append(arr[i][0])
        if (arr[i][0] == 'yesterday'):
            duration.append("1 day")

    for i in range(len(named_entity)):
        if (named_entity[i][0] in dict):
            if (dict[named_entity[i][0]] == "JJ"):
                sym.append(named_entity[i][0])
        else:
            sym.append(named_entity[i][0])

    print(sym, duration)
    return sym, duration


def prescription(text):
    arr,named_entity=get_pos_tags_sci(text,1)
    print(named_entity)


sample_text = "high fever since yesterday"
sypmptom(sample_text)
