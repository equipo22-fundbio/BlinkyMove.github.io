from tkinter import *
import tkinter.messagebox as mb
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
        button1 = Button(frame1, text="Vamos a comer\n🍕",width=23, height=8)
        button1.pack( padx=1, pady = 1,side=LEFT)
        button2 = Button(frame1,text="Quiero ir al baño\n🚽",width=23, height=8)
        button2.pack( padx=1, pady = 1,side=RIGHT)
        frame2 = Frame(self,width=100, height=100)
        frame2.pack(fill= X, padx=1, pady = 1)
        button3 = Button(frame2, text="Hola\n🙋",width=23, height=8)
        button3.pack( padx=1, pady = 1,side=LEFT)
        button4 = Button(frame2,text="Tengo sed\n🥤",width=23, height=8)
        button4.pack( padx=1, pady = 1,side=RIGHT)
        frame3 = Frame(self,width=100, height=100)
        frame3.pack(fill= X, padx=1, pady = 1)
        button5= Button(frame3, text="Iré a dormir\n🥱",width=23, height=8)
        button5.pack( padx=1, pady = 1,side=LEFT)
        button6 = Button(frame3,text="Tengo frío\n❄",width=23, height=8)
        button6.pack( padx=1, pady = 1,side=RIGHT)
        frame4 = Frame(self,width=100, height=100)
        frame4.pack(fill= X, padx=1, pady = 1)
        button5= Button(frame4, text="Editar",width=10, height=10)
        button5.pack( padx=1, pady = 1,side=TOP)
if __name__ == "__main__":
    app= App()
    app.mainloop()