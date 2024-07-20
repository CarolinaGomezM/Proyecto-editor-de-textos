from tkinter import *

def Sumar():
    resultado.set( float(n1.get()) + float(n2.get()) )
    borrar()

def Resta():
    resultado.set( float(n1.get()) - float(n2.get()) )
    borrar()

def Prod():
    resultado.set( float(n1.get()) * float(n2.get()) )
    borrar()


def borrar():
    n1.set("")
    n2.set("")


root = Tk()
root.config(bd=15) #bd = border

n1 = StringVar()
n2 = StringVar()   
resultado = StringVar()


Label(root, text="Primer número").pack()
Entry(root, justify="center", textvariable=n1).pack() #primer numero
Label(root, text="Segundo número").pack()
Entry(root, justify="center", textvariable=n2).pack() #segundo numero

Label(root, text="\nResultado").pack()
Label(root, justify="center", textvariable=resultado).pack() #resultado

Button(root, text="Sumar", command=Sumar).pack(side="left")
Button(root, text="Resta", command=Resta).pack(side="left")
Button(root, text="Producto", command=Prod).pack(side="left")




root.mainloop()