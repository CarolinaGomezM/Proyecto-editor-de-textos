from tkinter import *

root = Tk()


"""
# StringVar() es una variable especial que se puede asociar a un widget para que se actualice automáticamente cuando cambie el valor de la variable
texto = StringVar()
texto.set("Un nuevo texto")

# Se usa únicamente side para indicar la posición de la etiqueta, sin embargo no pone las etiquetas en la posición deseada.
# Cuando se usa anchor, se puede indicar la posición de la etiqueta con respecto a la ventana, sin embargo la altura de las etiquetas es dispareja
#.pack(side="left"), .pack(anchor="nw")
Label(root, text="Hola mundo!").pack(anchor="nw")
label = Label(root, text="Otra etiqueta!")
label.pack(anchor="center")
Label(root, text="última etiqueta!").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana", 24)) #bg = background, fg = foreground, font = fuente
label.config(textvariable=texto)

"""

imagen = PhotoImage(file="imagen.gif")

Label(root, image=imagen, bd=0).pack(side="left") #bd = border

root.mainloop()