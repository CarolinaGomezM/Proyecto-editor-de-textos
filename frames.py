from tkinter import *

root = Tk()
root.title("Hola mundo")
root.iconbitmap("hola.ico")
root.resizable(1,1) # Si se quiere que no se pueda cambiar el tamaño de la ventana poner False, False

frame = Frame(root, width=480, height=320)
frame.pack(fill="both", expand=1) # Alinear el frame en el centro de la ventana, fill = x, y, both, si se pasa únicamente fill="y" el frame
# no se expande como debería, por lo que se debe pasar expand=1
# frame.pack(side="bottom", anchor="w") # Alinear el frame en el centro y abajo de la ventana, anchor = w, e, n, s, ne, nw, se, sw
frame.config(cursor="pirate") #Cambiar el cursor del ratón dentro del frame
frame.config(bg="lightblue") #Cambiar el color de fondo del frame
frame.config(bd=25) #Cambiar el tamaño del borde del frame
frame.config(relief="sunken") #Cambiar el tipo de borde del frame



root.config(cursor="arrow") #Cambiar el cursor del ratón dentro del frame
root.config(bg="blue") #Cambiar el color de fondo del frame
root.config(bd=15) #Cambiar el tamaño del borde del frame
root.config(relief="ridge") #Cambiar el tipo de borde del frame
root.mainloop()

