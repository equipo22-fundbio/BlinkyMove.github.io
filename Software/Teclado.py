from tkinter import *
import tkinter.messagebox as mb


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
        self.button3 = Button(frame3, text='$')
        self.button3.grid(row=0, column=8)
        self.button2 = Button(frame3, text='←', command=lambda: self.dialog("*"))
        self.button2.grid(row=0, column=9)
        frame4 = Frame(self, width=100, height=100)
        frame4.pack(fill=X, padx=1, pady=1)
        self.button4 = Button(frame4, text='123')
        self.button4.grid(row=0, column=0)
        self.button5 = Button(frame4, text='@')
        self.button5.grid(row=0, column=1)
        self.button6 = Button(frame4, text='¥')
        self.button6.grid(row=0, column=2)
        self.buttonesp = Button(frame4, text='    Espacio    ', command=lambda: self.dialog(" "))
        self.buttonesp.grid(row=0, column=3)
        self.buttonret = Button(frame4, text='Return')
        self.buttonret.grid(row=0, column=8)

    def dialog(self, q):
        cad = self.cadena.get()
        if q == "*":
            cad = cad[:-1]
        else:
            if self.mayus == 1:
                cad = cad + q.upper()
            else:
                cad = cad + q
        self.cadena.set(cad)

    def mayusc(self):

        if (self.mayus == 1):
            self.mayus = self.mayus - 1
        else:
            self.mayus = self.mayus + 1


if __name__ == "__main__":
    app = App()
    app.mainloop()
