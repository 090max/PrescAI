import speech_recognition as sr
import data_manipulation.data_processor as processor
import time
from speech_text.google_rec import speech_to_text
from tkinter import *

# create window object
app = Tk()

app.title('Prescription')
app.geometry('1000x760')
c = 0

mapper = {
    "name": 0,
    "prescription": 0,
    "symptoms": 0,
    "advice": 0,
    "diagnosis": 0
}
res_tag = ""
res = ""


def name(a, b, d):
    global c
       
    part_text1 = StringVar(app, value=a)
    part_text2 = StringVar(app, value=b)
    part_text3 = StringVar(app, value=d)

    if (mapper["name"] == 0):
        mapper["name"] = 1 - mapper["name"]
        part_name = Label(app, text='Name', font=('bold', 28), pady=20)
        part_name.grid(row=c * 4, column=0)

        part_age = Label(app, text="Age", font=('bold', 28), pady=20)
        part_age.grid(row=c * 4, column=2)

        part_gender = Label(app, text="Gender", font=('bold', 28), pady=20)
        part_gender.grid(row=c * 4, column=4)

    part_entry1 = Entry(app, textvariable=part_text1, font=28)
    part_entry1.grid(row=c * 4 + 2, column=0)

    part_entry2 = Entry(app, textvariable=part_text2, font=28)
    part_entry2.grid(row=c * 4 + 2, column=2)

    part_entry3 = Entry(app, textvariable=part_text3, font=28)
    part_entry3.grid(row=c * 4 + 2, column=4)
    c = c + 1


def symptoms(sym, duration):
    # c = c + 1
    global c
       
    part_text1 = StringVar(app, value=sym)
    part_text2 = StringVar(app, value=duration)

    if (mapper["symptoms"] == 0):
        mapper["symptoms"] = 1-mapper["symptoms"]
        part_name = Label(app, text='Symptom', font=('bold', 28), pady=20)
        part_name.grid(row=c * 4, column=0)

        part_dur = Label(app, text='Duration', font=('bold', 28), pady=20)
        part_dur.grid(row=c * 4, column=2)

    part_entry1 = Entry(app, textvariable=part_text1, font=28)
    part_entry1.grid(row=c * 4 + 2, column=0)

    part_entry2 = Entry(app, textvariable=part_text2, font=28)
    part_entry2.grid(row=c * 4 + 2, column=2)
    c = c + 1


def diagnosis(tagged):
    # c = c + 1
    global c
       
    part_text1 = StringVar(app, value=tagged)
    if (mapper["diagnosis"] == 0):
        mapper["diagnosis"] = 1-mapper["diagnosis"]
        part_name = Label(app, text='Diagnosis', font=('bold', 28), pady=20)
        part_name.grid(row=c * 4, column=0)
    part_entry1 = Entry(app, textvariable=part_text1, font=28)
    part_entry1.grid(row=c * 4 + 2, column=0)
    c = c + 1


def prescription(pres, quan, dosage, nod):
    # c = c + 1
    global c
       

    part_text1 = StringVar(app, value=pres)
    part_text2 = StringVar(app, value=quan)
    part_text3 = StringVar(app, value=dosage)
    part_text4 = StringVar(app, value=nod)
    global res_tag
    print("mapper tag is ", mapper["prescription"], res_tag)
    if (mapper["prescription"] == 0):
        mapper["prescription"] = 1 - mapper["prescription"]
        part_pres = Label(app, text='Presciption', font=('bold', 28), pady=20)
        part_pres.grid(row=c * 4, column=0)

        part_quan = Label(app, text='Quantity', font=('bold', 28), pady=20)
        part_quan.grid(row=c * 4, column=2)

        part_dosage = Label(app, text='Dosage', font=('bold', 28), pady=20)
        part_dosage.grid(row=c * 4, column=4)

        part_nod = Label(app, text='No of Days', font=('bold', 28), pady=20)
        part_nod.grid(row=c * 4, column=6)
    part_entry1 = Entry(app, textvariable=part_text1, font=28)
    part_entry1.grid(row=c * 4 + 2, column=0)

    part_entry2 = Entry(app, textvariable=part_text2, font=28)
    part_entry2.grid(row=c * 4 + 2, column=2)

    part_entry3 = Entry(app, textvariable=part_text3, font=28)
    part_entry3.grid(row=c * 4 + 2, column=4)

    part_entry4 = Entry(app, textvariable=part_text4, font=28)
    part_entry4.grid(row=c * 4 + 2, column=6)

    c = c + 1


def moreSame(tagged):
    global c
       
    part_text1 = StringVar(app, value=tagged)
    part_entry1 = Entry(app, textvariable=part_text1, font=28)
    part_entry1.grid(row=c * 4, column=0)
    c = c + 1


def process_res(text):
    keys = ["name", "symptoms", "prescription", "diagnosis"]
    for i in keys:
        if (i in text):
            global res_tag
            if (len(res_tag) != 0):
                mapper[res_tag] = 1 - mapper[res_tag]
            res_tag = i
            return True
            break
    return False


def record_audio():
    try:
        res = speech_to_text(res_tag)
        if (process_res(res) == False):
            # res_tag = extract(res)
            if (res_tag == "name"):
                name1, age, gender = processor.name(res)
                print(name1, age, gender)
                name(name1, age, gender)
                # c=c+1
            elif (res_tag == "symptoms"):
                sym, duration = processor.symptom(res)
                symptoms(sym, duration)
                # c=c+1
            elif (res_tag == "diagnosis"):
                diag = processor.diagnosis(res)
                diagnosis(diag)
                # c=c+1
            elif (res_tag == "prescription"):
                pres, quan, dosage, nod = processor.prescription(res)
                print("SS", pres, quan, dosage, nod)
                prescription(pres, quan, dosage, nod)
                # c=c+1
            else:
                moreSame(res)
        else:
            record_audio()
    except Exception as ex:
        print(ex)
    except ValueError as val:
        print(val)


def init_tkinter():
    add_btn = Button(app, text="Record Prescription", width=40, bd=4, bg="green", command=record_audio)
    add_btn.grid(row=100, column=4)
    app.mainloop()
