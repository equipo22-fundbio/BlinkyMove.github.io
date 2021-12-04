from tkinter import *
import tkinter.messagebox as mb
import pyttsx3


def hacer_click1():
    engine = pyttsx3.init()
    voice_id = 'spanish-latin-am'
    engine.setProperty('voice', voice_id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say('Vamos a comer')
    engine.runAndWait()

def hacer_click2():
    engine = pyttsx3.init()
    voice_id = 'spanish-latin-am'
    engine.setProperty('voice', voice_id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say('Quiero ir al baño')
    engine.runAndWait()

def hacer_click3():
    engine = pyttsx3.init()
    voice_id = 'spanish-latin-am'
    engine.setProperty('voice', voice_id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say('Hola')
    engine.runAndWait()

def hacer_click4():
    engine = pyttsx3.init()
    voice_id = 'spanish-latin-am'
    engine.setProperty('voice', voice_id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say('Tengo sed')
    engine.runAndWait()

def hacer_click5():
    engine = pyttsx3.init()
    voice_id = 'spanish-latin-am'
    engine.setProperty('voice', voice_id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say('Iré a dormir')
    engine.runAndWait()

def hacer_click6():
    engine = pyttsx3.init()
    voice_id = 'spanish-latin-am'
    engine.setProperty('voice', voice_id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say('Tengo frío')
    engine.runAndWait()

class App(Tk):
    def __init__(self):
        super().__init__()
        mi_menu=Menu(self)
        self.geometry("350x450")
        self.config(menu=mi_menu)
        op_menu=Menu(mi_menu,tearoff=0)
        mi_menu.add_cascade(label='Atrás')
        self.l=Label(self,text="Selecciona una frase")
        self.l.pack(side=TOP)

        frame1 = Frame(self,width=100, height=100)
        frame1.pack(fill= X, padx=1, pady = 1)
        button1 = Button(frame1, text="Vamos a comer\n🍕",width=23, height=8, command=hacer_click1)
        button1.pack( padx=1, pady = 1,side=LEFT)
        button2 = Button(frame1,text="Quiero ir al baño\n🚽",width=23, height=8, command=hacer_click2)
        button2.pack( padx=1, pady = 1,side=RIGHT)
        frame2 = Frame(self,width=100, height=100)
        frame2.pack(fill= X, padx=1, pady = 1)
        button3 = Button(frame2, text="Hola\n🙋",width=23, height=8, command=hacer_click3)
        button3.pack( padx=1, pady = 1,side=LEFT)
        button4 = Button(frame2,text="Tengo sed\n🥤",width=23, height=8, command=hacer_click4)
        button4.pack( padx=1, pady = 1,side=RIGHT)
        frame3 = Frame(self,width=100, height=100)
        frame3.pack(fill= X, padx=1, pady = 1)
        button5= Button(frame3, text="Iré a dormir\n🥱",width=23, height=8, command=hacer_click5)
        button5.pack( padx=1, pady = 1,side=LEFT)
        button6 = Button(frame3,text="Tengo frío\n❄",width=23, height=8, command=hacer_click6)
        button6.pack( padx=1, pady = 1,side=RIGHT)
        frame4 = Frame(self,width=100, height=100)
        frame4.pack(fill= X, padx=1, pady = 1)



if __name__ == "__main__":
    app= App()
    app.mainloop()
