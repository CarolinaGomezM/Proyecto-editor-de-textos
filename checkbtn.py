from tkinter import *

def seleccionar():
    cadena = ""
    if(leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"
    if(azucar.get()):
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"

    monitor.config(text=cadena)

root = Tk()

root.title("Cafetería")
root.config(bd=15) #bd: border

leche = IntVar() # 1 si, 0 no
azucar = IntVar() # 1 si, 0 no

imagen = PhotoImage(file="imagen.gif")

Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="¿Cómo prefieres el café?").pack(anchor="w") #anchor: alineación

Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w") 
#onvalue es el valor que se le asigna a la variable si está seleccionado, offvalue si no lo está
Checkbutton(frame, text="Con azúcar", variable=azucar,onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()




root.mainloop()