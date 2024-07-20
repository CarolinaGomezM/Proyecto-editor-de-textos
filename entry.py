from tkinter import *

root = Tk()

#Al usar marcos (frames) nos ayuda a organizar los widgets de una manera más ordenada

#Pero al usar grid nos ayuda a tener los widgets en una cuadrícula, haciendolos simetricos

label = Label(root, text="Nombre muy largo")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5) #sticky = alineación (n, s, e, w, ne, se, sw, nw

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5) #padx = padding en x, pady = padding en y
entry.config(justify="right", state="normal") #justify = alineación del texto (left, right, center
#state = estado del widget (normal, disabled, readonly)


label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*") #show = caracter que se muestra en lugar del texto (útil para contraseñas)






root.mainloop()