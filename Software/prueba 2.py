from tkinter import *
import tkinter.messagebox as mb
import pyttsx3
import pyautogui
from data import Sensor1
from data import Sensor2
from data import Sensor3
from data import Sensor4


class App(Tk):
    def __init__(self):
        super().__init__()
        mi_menu = Menu(self)
        self.geometry("200x150")
        self.cadena = StringVar();
        self.mayus = 0
        frame0 = Frame(self, width=100, height=100)
        frame0.pack(fill=X, padx=20, pady=1)
        self.e1 = Entry(frame0, width=24, textvariable=self.cadena)
        self.e1.grid(row=0, column=1)
        frame1 = Frame(self, width=100, height=100)
        frame1.pack(fill=X, padx=1, pady=1)
        self.buttonq = Button(frame1, text='Q', command=lambda: self.dialog("q"))
        self.buttonq.grid(row=1, column=0)
        self.buttonw = Button(frame1, text='W', command=lambda: self.dialog("w"))
        self.buttonw.grid(row=1, column=1)
        self.buttone = Button(frame1, text='E', command=lambda: self.dialog("e"))
        self.buttone.grid(row=1, column=2)
        self.buttonr = Button(frame1, text='R', command=lambda: self.dialog("r"))
        self.buttonr.grid(row=1, column=3)
        self.buttont = Button(frame1, text='T', command=lambda: self.dialog("t"))
        self.buttont.grid(row=1, column=4)
        self.buttony = Button(frame1, text='Y', command=lambda: self.dialog("y"))
        self.buttony.grid(row=1, column=5)
        self.buttonu = Button(frame1, text='U', command=lambda: self.dialog("u"))
        self.buttonu.grid(row=1, column=6)
        self.buttoni = Button(frame1, text='I', command=lambda: self.dialog("i"))
        self.buttoni.grid(row=1, column=7)
        self.buttono = Button(frame1, text='O', command=lambda: self.dialog("o"))
        self.buttono.grid(row=1, column=8)
        self.buttonp = Button(frame1, text='P', command=lambda: self.dialog("p"))
        self.buttonp.grid(row=1, column=9)
        frame2 = Frame(self, width=100, height=100)
        frame2.pack(fill=X, padx=12, pady=1)
        self.buttona = Button(frame2, text='A', command=lambda: self.dialog("a"))
        self.buttona.grid(row=0, column=0)
        self.buttons = Button(frame2, text='S', command=lambda: self.dialog("s"))
        self.buttons.grid(row=0, column=1)
        self.buttond = Button(frame2, text='D', command=lambda: self.dialog("d"))
        self.buttond.grid(row=0, column=2)
        self.buttonf = Button(frame2, text='F', command=lambda: self.dialog("f"))
        self.buttonf.grid(row=0, column=3)
        self.buttong = Button(frame2, text='G', command=lambda: self.dialog("g"))
        self.buttong.grid(row=0, column=4)
        self.buttonh = Button(frame2, text='H', command=lambda: self.dialog("h"))
        self.buttonh.grid(row=0, column=5)
        self.buttonj = Button(frame2, text='J', command=lambda: self.dialog("j"))
        self.buttonj.grid(row=0, column=6)
        self.buttonk = Button(frame2, text='K', command=lambda: self.dialog("k"))
        self.buttonk.grid(row=0, column=7)
        self.buttonl = Button(frame2, text='L', command=lambda: self.dialog("l"))
        self.buttonl.grid(row=0, column=8)
        frame3 = Frame(self, width=100, height=100)
        frame3.pack(fill=X, padx=1, pady=1)
        self.button1 = Button(frame3, text='↑', command=self.mayusc)
        self.button1.grid(row=0, column=0)
        self.buttonz = Button(frame3, text='Z', command=lambda: self.dialog("z"))
        self.buttonz.grid(row=0, column=1)
        self.buttonx = Button(frame3, text='X', command=lambda: self.dialog("x"))
        self.buttonx.grid(row=0, column=2)
        self.buttonc = Button(frame3, text='C', command=lambda: self.dialog("c"))
        self.buttonc.grid(row=0, column=3)
        self.buttonv = Button(frame3, text='V', command=lambda: self.dialog("v"))
        self.buttonv.grid(row=0, column=4)
        self.buttonb = Button(frame3, text='B', command=lambda: self.dialog("b"))
        self.buttonb.grid(row=0, column=5)
        self.buttonn = Button(frame3, text='N', command=lambda: self.dialog("n"))
        self.buttonn.grid(row=0, column=6)
        self.buttonm = Button(frame3, text='M', command=lambda: self.dialog("m"))
        self.buttonm.grid(row=0, column=7)
        self.buttonñ = Button(frame3, text='Ñ', command=lambda: self.dialog("ñ"))
        self.buttonñ.grid(row=0, column=8)
        self.button2 = Button(frame3, text='←', command=lambda: self.dialog("*"))
        self.button2.grid(row=0, column=9)
        frame4 = Frame(self, width=100, height=100)
        frame4.pack(fill=X, padx=1, pady=1)
        self.button4 = Button(frame4, text='123')
        self.button4.grid(row=0, column=0)
        self.button5 = Button(frame4, text='@')
        self.button5.grid(row=0, column=1)
        self.button6 = Button(frame4, text='$')
        self.button6.grid(row=0, column=2)
        self.buttonesp = Button(frame4, text='    Espacio    ', command=lambda: self.dialog(" "))
        self.buttonesp.grid(row=0, column=3)

        def enviar_voz():
            engine = pyttsx3.init()
            voice_id = 'spanish-latin-am'
            engine.setProperty('voice', voice_id)
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say(self.cadena.get())
            engine.runAndWait()

        self.buttonret = Button(frame4, text='Return', command=enviar_voz)
        self.buttonret.grid(row=0, column=8)


    def dialog(self):
        cad = self.cadena.get()

            #inicioderecho

            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonw.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                   pyautogui.press(self.buttonw)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonw.configure(bg="gray94")
                self.buttone.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                   pyautogui.press(self.buttone)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttone.configure(bg="gray94")
                self.buttonr.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                   pyautogui.press(self.buttonr)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonr.configure(bg="gray94")
                self.buttont.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                   pyautogui.press(self.buttont)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttont.configure(bg="gray94")
                self.buttony.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttony)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttony.configure(bg="gray94")
                self.buttonu.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonu)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonu.configure(bg="gray94")
                self.buttoni.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttoni)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttoni.configure(bg="gray94")
                self.buttono.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttono)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttono.configure(bg="gray94")
                self.buttonp.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonp)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonp.configure(bg="gray94")
                self.buttona.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttona)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttona.configure(bg="gray94")
                self.buttons.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttons)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttons.configure(bg="gray94")
                self.buttond.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttond)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttond.configure(bg="gray94")
                self.buttonf.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonf)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonf.configure(bg="gray94")
                self.buttong.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttong)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttong.configure(bg="gray94")
                self.buttonh.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonh)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonh.configure(bg="gray94")
                self.buttonj.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonj)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonj.configure(bg="gray94")
                self.buttonk.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonk)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonk.configure(bg="gray94")
                self.buttonl.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonl)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonl.configure(bg="gray94")
                self.button1.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button1)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.button1.configure(bg="gray94")
                self.buttonz.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonz)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonz.configure(bg="gray94")
                self.buttonx.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonx)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonx.configure(bg="gray94")
                self.buttonc.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonc)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonc.configure(bg="gray94")
                self.buttonv.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonv)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonv.configure(bg="gray94")
                self.buttonb.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonb)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonb.configure(bg="gray94")
                self.buttonn.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonn)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonn.configure(bg="gray94")
                self.buttonm.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonm)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonm.configure(bg="gray94")
                self.buttonñ.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonñ)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonñ.configure(bg="gray94")
                self.button2.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button2)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.button2.configure(bg="gray94")
                self.button4.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button4)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.button4.configure(bg="gray94")
                self.button5.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button5)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.button5.configure(bg="gray94")
                self.button6.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button6)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.button6.configure(bg="gray94")
                self.buttonesp.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonesp)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonesp.configure(bg="gray94")
                self.buttonret.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonret)
            if Sensor1 > 500 and Sensor2 > 1000:
                self.buttonret.configure(bg="gray94")
                self.buttonq.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonq)
            #fin de derecha
            #inicio abajo
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttona.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttona)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttona.configure(bg="gray94")
                self.buttonz.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonz)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonz.configure(bg="gray94")
                self.button5.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button5)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonw.configure(bg="gray94")
                self.buttons.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttons)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttons.configure(bg="gray94")
                self.buttonx.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonx)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonx.configure(bg="gray94")
                self.button6.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button6)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttone.configure(bg="gray94")
                self.buttond.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttond)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttond.configure(bg="gray94")
                self.buttonc.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonr)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonc.configure(bg="gray94")
                self.buttonesp.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonesp)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonr.configure(bg="gray94")
                self.buttonf.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonf)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonf.configure(bg="gray94")
                self.buttonv.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonv)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonv.configure(bg="gray94")
                self.buttonesp.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonesp)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttont.configure(bg="gray94")
                self.buttong.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttong)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttong.configure(bg="gray94")
                self.buttonb.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonb)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonb.configure(bg="gray94")
                self.buttony.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttony)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttony.configure(bg="gray94")
                self.buttonh.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonh)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonh.configure(bg="gray94")
                self.buttonn.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonn)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonn.configure(bg="gray94")
                self.buttonesp.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonesp)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonu.configure(bg="gray94")
                self.buttonj.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonj)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonj.configure(bg="gray94")
                self.buttonm.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonm)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonm.configure(bg="gray94")
                self.buttonret.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonret)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttoni.configure(bg="gray94")
                self.buttonk.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonk)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonk.configure(bg="gray94")
                self.buttonñ.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonñ)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonñ.configure(bg="gray94")
                self.buttonret.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonret)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttono.configure(bg="gray94")
                self.buttonl.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonl)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonl.configure(bg="gray94")
                self.button2.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button2)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.button2.configure(bg="gray94")
                self.buttonret.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonret)
            if Sensor3 > 500 and Sensor4 > 1000:
                self.buttonp.configure(bg="gray94")
                self.buttonl.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonl)
            #fin de abajo
            #inicio de arriba
            if Sensor3 > 1000 and Sensor4 > 500:
                self.button4.configure(bg="gray94")
                self.buttonz.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonz)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonz.configure(bg="gray94")
                self.buttona.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttona)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttona.configure(bg="gray94")
                self.buttonq.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonq)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonq.configure(bg="gray94")
            if Sensor3 > 1000 and Sensor4 > 500:
                self.button5.configure(bg="gray94")
                self.buttonx.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonx)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonx.configure(bg="gray94")
                self.buttons.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttons)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttons.configure(bg="gray94")
                self.buttonw.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonw)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonw.configure(bg="gray94")
            if Sensor3 > 1000 and Sensor4 > 500:
                self.button6.configure(bg="gray94")
                self.buttonc.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonc)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonc.configure(bg="gray94")
                self.buttond.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttond)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttond.configure(bg="gray94")
                self.buttone.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttone)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttone.configure(bg="gray94")
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonesp.configure(bg="gray94")
                self.buttonv.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonv)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonv.configure(bg="gray94")
                self.buttonf.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonf)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonf.configure(bg="gray94")
                self.buttonr.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonr)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonr.configure(bg="gray94")
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonesp.configure(bg="gray94")
                self.buttonb.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonb)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonb.configure(bg="gray94")
                self.buttong.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttong)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttong.configure(bg="gray94")
                self.buttont.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttont)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttont.configure(bg="gray94")
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonesp.configure(bg="gray94")
                self.buttonn.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonn)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonn.configure(bg="gray94")
                self.buttonh.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonh)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonh.configure(bg="gray94")
                self.buttony.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttony)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttony.configure(bg="gray94")
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonesp.configure(bg="gray94")
                self.buttonm.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonm)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonm.configure(bg="gray94")
                self.buttonj.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonj)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonj.configure(bg="gray94")
                self.buttonu.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonu)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonu.configure(bg="gray94")
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonret.configure(bg="gray94")
                self.buttonñ.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonñ)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonñ.configure(bg="gray94")
                self.buttonk.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonk)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonk.configure(bg="gray94")
                self.buttoni.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttoni)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttoni.configure(bg="gray94")
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonret.configure(bg="gray94")
                self.button2.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button2)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.button2.configure(bg="gray94")
                self.buttonl.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonl)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttonl.configure(bg="gray94")
                self.buttono.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttono)
            if Sensor3 > 1000 and Sensor4 > 500:
                self.buttono.configure(bg="gray94")
            #fin arriba
            #inicio izquierda
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttono.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttono)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttono.configure(bg="gray94")
                self.buttoni.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttoni)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttoni.configure(bg="gray94")
                self.buttonu.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonu)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonu.configure(bg="gray94")
                self.buttony.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttony)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttony.configure(bg="gray94")
                self.buttont.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttont)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttont.configure(bg="gray94")
                self.buttonr.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonr)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonr.configure(bg="gray94")
                self.buttone.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttone)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttone.configure(bg="gray94")
                self.buttonw.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonw)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonw.configure(bg="gray94")
                self.buttonq.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonq)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonq.configure(bg="gray94")
                self.buttonl.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonl)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonl.configure(bg="gray94")
                self.buttonk.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonk)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonk.configure(bg="gray94")
                self.buttonj.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonj)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonj.configure(bg="gray94")
                self.buttonh.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonh)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonh.configure(bg="gray94")
                self.buttong.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonr)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttong.configure(bg="gray94")
                self.buttonf.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonf)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonf.configure(bg="gray94")
                self.buttond.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttond)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttond.configure(bg="gray94")
                self.buttons.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttons)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttons.configure(bg="gray94")
                self.buttona.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttona)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttona.configure(bg="gray94")
                self.button2.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.button2)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.button2.configure(bg="gray94")
                self.buttonñ.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonñ)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonñ.configure(bg="gray94")
                self.buttonm.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonm)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonm.configure(bg="gray94")
                self.buttonn.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonn)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonn.configure(bg="gray94")
                self.buttonb.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonb)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonb.configure(bg="gray94")
                self.buttonv.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonv)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonv.configure(bg="gray94")
                self.buttonc.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonc)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonc.configure(bg="gray94")
                self.buttonx.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonx)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonx.configure(bg="gray94")
                self.buttonz.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500:
                    pyautogui.press(self.buttonz)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonz.configure(bg="gray94")
                self.button1.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500
                    pyautogui.press(self.button1)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.button1.configure(bg="gray94")
                self.buttonret.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500
                    pyautogui.press(self.buttonret)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonret.configure(bg="gray94")
                self.buttonesp.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500
                    pyautogui.press(self.buttonesp)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.buttonesp.configure(bg="gray94")
                self.button6.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500
                    pyautogui.press(self.button6)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.button6.configure(bg="gray94")
                self.button5.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500
                    pyautogui.press(self.button5)
            if Sensor1 > 1000 and Sensor2 > 500:
                self.button5.configure(bg="gray94")
                self.buttonq.configure(bg="pale turquoise")
                if Sensor1 and Sensor2 > 500
                    pyautogui.press(self.buttonq)
                #fin izquierda

    def mayusc(self):

        if (self.mayus == 1):
            self.mayus = self.mayus - 1
        else:
            self.mayus = self.mayus + 1


if __name__ == "__main__":
    app = App()
    app.mainloop()
