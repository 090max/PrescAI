import nltk
import sys

sys.path.append('..')
import spacy

spacy_nlp_sci = spacy.load('en_core_sci_md')
spacy_nlp_en = spacy.load('en_core_web_sm')


def Remove_stopwords(string):
    # tokenizing
    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer("[a-zA-Z@0-9]+")
    word_list = tokenizer.tokenize(string)

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

def chinking_list(list, entity_list, pos_tags):
    unused_words = []
    final_list = []
    final_entity_list = []
    for i in range(len(list)):
        if (list[i][1] not in pos_tags):
            final_list.append(list[i])
        else:
            unused_words.append(list[i][0])

    for i in range(len(entity_list)):
        if (entity_list[i][0] not in unused_words):
            final_entity_list.append(entity_list[i])

    return final_list, final_entity_list



def get_pos_tags_en(text, rem_stopwords=1):
    final_text = text
    if (rem_stopwords == 1):
        processed_text = Remove_stopwords(text)
        final_text = " ".join(processed_text)
    words = spacy_nlp_sci(final_text)
    arr = [(w.text, w.tag_) for w in words]
    named_entity = [(w.text, w.label_) for w in words.ents]
    return arr, named_entity


def get_pos_tags_sci(text, rem_stopwords=1):
    final_text = text
    if (rem_stopwords == 1):
        processed_text = Remove_stopwords(text)
        final_text = " ".join(processed_text)
    words = spacy_nlp_sci(final_text)
    arr = [(w.text, w.tag_) for w in words]
    named_entity = [(w.text, w.label_) for w in words.ents]
    return arr, named_entity


def name(text):
    arr, named_entity = get_pos_tags_sci(text)
    not_require = ["name", "patients", "patient", "age", "gender", "sex", "years", "old"]
    pname=[]
    age=""
    gender=""
    for i in range(len(arr)):
        if arr[i][1] == "CD":
            age = arr[i][0]
        elif arr[i][0] == "male" or arr[i][0] == "female" or arr[i][0] == "others":
            gender = arr[i][0]
        else:
            if(arr[i][1] == "NNP" and arr[i][0] not in not_require):
                pname.append(arr[i][0])

    fname=" ".join(pname)

    print(fname, age, gender)
    return fname, age, gender

#TODO --- dataset se value uthani h
def symptom(text):

    arr,named_entity=get_pos_tags_sci(text)
    print(arr,named_entity)
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

    sym = " ".join(sym)
    duration = " ".join(duration)
    print(sym, duration)
    return sym, duration

def diagnosis(text):
    init_arr, init_named_entity = get_pos_tags_sci(text)
    arr,named_entity=chinking_list(init_arr,init_named_entity,["VBG","VB"])
    print(arr,named_entity)
    diag=[]
    not_require = ["name", "patients", "patient", "age", "gender", "sex", "years", "old"]
    for i in range(len(named_entity)):
        if named_entity[i][0] not in not_require:
            diag.append(named_entity[i][0])

    diag = " ".join(diag)
    print(diag)
    return diag

#TODO add advice to the prescription
def prescription(text):
    init_arr, init_named_entity = get_pos_tags_sci(text, 0)
    arr, named_entity = chinking_list(init_arr, init_named_entity, ["PRP", "VBP", "VB", "TO"])
    print(arr, named_entity)
    time_list = ['day', 'days', 'week', 'weeks', 'month', 'months', 'year', 'years']
    quantity = ['ml', 'liter', 'liters', 'mg', 'milli gram', 'milligram', 'milligrams', 'milli grams', 'kilo grams',
                'kilo gram', 'kilogram', 'kilograms']
    drug_quantity = ["spoon", "tablet", "spoons", "tablets"]
    frequency_notifiers = ["times", "time"]
    food_details = ["before", "after"]
    time_details = ["hour", "hours", "minutes", "minute", "seconds", "seconds"]
    fixed_freq=["daily","monthly","weekly","yearly"]
    data = {
        "drug_name": "",  # Name of the drug
        "quantity": "",  # The quantity of the prescribed drug
        "unit": "",  # the unit of drug ..mg ,ml
        "drug_quantity": "",  # quantity of tablets or spoons
        "frequency": "",  # How many times a day
        "duration": ""  # For how many days
    }
    for i in range(len(named_entity)):
        if (named_entity[i][1] == 'ENTITY' and named_entity[i][0] not in drug_quantity and named_entity[i][0] not in time_list and named_entity[i][0] not in quantity):
            if (len(data["drug_name"]) == 0):
                data["drug_name"] = str(named_entity[i][0])
    i = 0
    while i < (len(arr)):
        if (arr[i][1] == 'NN' or arr[i][1] == 'NNS'):
            if (arr[i][0] in quantity):
                if (len(data["unit"]) == 0):
                    data["unit"] = str(arr[i][0])
                if (arr[i - 1][1] == "CD"):
                    if (len(data["quantity"]) == 0):
                        data["quantity"] = arr[i - 1][0]
            elif (arr[i][0] in drug_quantity):
                if (len(data["drug_quantity"]) == 0):
                    type = ""
                    quant = ""
                    type = str(arr[i][0])
                    if (arr[i - 1][1] == "CD"):
                        quant = arr[i - 1][0]
                    data["drug_quantity"] = str(quant) + " " + str(type)

            elif (arr[i][0] in frequency_notifiers):
                if (len(data["frequency"]) == 0):
                    freq = ""
                    freq_type = ""
                    freq_time = ""
                    freq_type = arr[i][0]
                    # Now searching for a CD
                    idx = i - 1
                    while (idx > 0 and arr[idx][1] != "NN" or arr[idx][1] != "NNS"):
                        if (arr[idx][1] == "CD"):
                            freq = arr[idx][0]
                            break
                        idx = idx - 1
                    # now finding time
                    idx = i + 1
                    while (idx < len(arr) and arr[idx][1] != "IN" or arr[idx][1] != "CD"):
                        print("hello..")
                        if (arr[idx][0] in time_list):
                            freq_time = arr[idx][0]
                            i = idx
                            break
                        idx = idx + 1

                    data["frequency"] = freq + " " + freq_type + " " + freq_time
            elif (arr[i][0] in time_list):
                if (len(data["duration"]) == 0):
                    # Now finding the duration
                    if (arr[i - 1][1] == "CD"):
                        data["duration"] = str(arr[i - 1][0]) + " " + str(arr[i][0])
                    elif (arr[i - 1][1] == "DT"):
                        data["duration"] = str("1") + " " + str(arr[i][0])

        elif (arr[i][1] == "RB" or arr[i][1] == "VBD" and arr[i][0] not in drug_quantity):
            if (len(data["frequency"]) == 0):
                freq = arr[i][0]
                freq_time = ""
                if(arr[i][0] not in fixed_freq):
                    # now finding time
                    idx = i + 1
                    while (idx < len(arr) and arr[idx][1] != "IN" or arr[idx][1] != "CD"):
                        if (arr[idx][0] in time_list):
                            freq_time = arr[idx][0]
                            i = idx
                            break
                        idx = idx + 1

                data["frequency"] = freq + " " + freq_time
        i = i + 1
    print(data)



name_text = "patient name is Nikhil Sharma he is a male and his age is 30"
name(name_text)

symptom_text = "patient is suffering from fever"
symptom(symptom_text)

diagnosis_text = "patient is suffering from acute bronchitis"
diagnosis(diagnosis_text)

prescription_text="paracetamol 250 mg twice a day daily for a week"
prescription(prescription_text)
