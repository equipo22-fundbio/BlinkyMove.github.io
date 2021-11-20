from tkinter import *
import tkinter.messagebox as mb
import math
class App(Tk):
    def __init__(self):
        super().__init__()
        mi_menu=Menu(self)
        self.geometry("250x350")
        self.config(menu=mi_menu)
        op_menu=Menu(mi_menu,tearoff=0)
        mi_menu.add_cascade(label='Atrás')

        self.l=Label(self,text="Registrate")
        self.l.pack(side=TOP)
        
        frame1 = Frame(self,width=100, height=100)
        frame1.pack(fill= X, padx=1, pady = 1)
        self.l1=Label(frame1,text="Nombre Completo")
        self.l1.pack(side=LEFT)
        frame2 = Frame(self,width=100, height=100)
        frame2.pack(fill= X, padx=1, pady = 1)
        self.e1=Entry(frame2, width=35)
        self.e1.pack(side=LEFT,padx= 1, pady = 2)
        frame3 = Frame(self,width=100, height=100)

        frame3.pack(fill= X, padx=1, pady = 1)
        
        self.l2=Label(frame3,text="Correo electrónico")
        self.l2.pack(side=LEFT)
        frame4 = Frame(self,width=100, height=100)
        frame4.pack(fill= X, padx=1, pady = 1)
        self.e2=Entry(frame4, width=35)
        self.e2.pack(side=LEFT,padx= 1, pady = 2)
        frame5 = Frame(self,width=100, height=100)
        frame5.pack(fill= X, padx=1, pady = 1)

        self.l3=Label(frame5,text="Contraseña")
        self.l3.pack(side=LEFT)
        frame6 = Frame(self,width=100, height=100)
        frame6.pack(fill= X, padx=1, pady = 1)
        self.e3=Entry(frame6,width=35)
        self.e3.pack(side=LEFT,padx= 1, pady = 2)
        frame7 = Frame(self,width=100, height=100)
        frame7.pack(fill= X, padx=1, pady = 1)
        
        self.l4=Label(frame7,text="Confirmar contraseña")
        self.l4.pack(side=LEFT)
        frame8 = Frame(self,width=100, height=100)
        frame8.pack(fill= X, padx=1, pady = 1)
        self.e4=Entry(frame8,width=35)
        self.e4.pack(side=LEFT,padx= 1, pady = 2)
 
        self.b=Button(self, text="Log in", width=10,command=self.calculate)
        self.b.pack(side=BOTTOM)
    def calculate(self):
        ia=int(self.v1.get())
        years=int(self.v2.get())
        mir=float(self.v3.get())/1200
        fr=ia*pow((1+mir),years*12)
        cad="$"+str(round(fr,2))
        self.v4.set(cad)
    def about(self):
        msg = "This is a program"
        mb.showwarning("About", msg)
if __name__ == "__main__":
    app= App()
    app.mainloop()
