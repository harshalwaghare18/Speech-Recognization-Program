from tkinter import *
from gtts import gTTS
import speech_recognition as sr
import os
mainwindow = Tk()
mainwindow.title("Converter")
mainwindow.geometry('600x600')
mainwindow.resizable(0,0)
mainwindow.configure(bg='yellow')

def say(text1):
    language = 'en'
    speech = gTTS(text = text1,lang=language,slow=False)
    speech.save('text.mp3')
    os.system('start text.mp3')

def recordvoice():
    while True :
        r = sr.Recognizer()
        with sr.Microphone() as source :
            audio =r.listen(source)
            try:
                text1= r.recognize_google(audio, language='en-IN')

            except :
                pass
            return text1

def TextToSpeech():
    texttospeechwindow=Toplevel(mainwindow)
    texttospeechwindow.title('Text To Speech Converter')
    texttospeechwindow.geometry('600x600')
    texttospeechwindow.configure(bg='blue')

    Label(texttospeechwindow, text ="Text To Speech ", font=('Times new roman',15), bg='blue').place(x=50)
    text = Text(texttospeechwindow, height=5, width =30, font=12)
    text.place(x=7, y=60)
    speakbutton=Button(texttospeechwindow, text='listen',bg='coral',command=lambda:say(str(text.get(1.0,END))))
    speakbutton.place(x=140, y=200)

def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech To Text Converter')
    speechtotextwindow.geometry('600x600')
    speechtotextwindow.configure(bg='pink')
    Label(speechtotextwindow, text='Speech To Text Converter', font = ('Times new roman',15),bg = 'IndianRed').place(x=50)

    text = Text(speechtotextwindow, font =12, height=3, width=30)
    text.place(x=7,y=100)

    recordbutton = Button(speechtotextwindow, text='Record', bg= 'sienna', command=lambda:text.insert(END,recordvoice))
    recordbutton.place(x=140,y=50)

Label(mainwindow, text ="Converter", font=('Times new roman', 16), bg ='red', wrap=True, wraplength =450).place(x=25, y=0)
texttospeechbutton = Button(mainwindow, text = "Text To Speech Conversion", font=('Times new roman', 16), bg='purple', fg='white',command=TextToSpeech)
texttospeechbutton.place(x=100, y=150)

speechtotextbutton = Button(mainwindow, text='SpeechTo Text Conversion', font = ('Times new roman',15), bg= 'purple', fg = 'white', command=SpeechToText)
speechtotextbutton.place(x=100, y=250)

mainwindow.update()
mainwindow.mainloop()
