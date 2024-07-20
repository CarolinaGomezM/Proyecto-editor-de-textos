from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
 #   MessageBox.showinfo("Hola!", "Hola mundo!") #Titulo, mensaje, showinfo: mensaje de información
 #   MessageBox.showwarning("Alerta", "Sección solo para administradores.") #showwarning: mensaje de advertencia
 #   MessageBox.showerror("Error", "Ha ocurrido un error inesperado.") #showerror: mensaje de error

 #   resultado = MessageBox.askquestion("Salir", "Estas seguro que quieres salir?") #askquestion: mensaje de pregunta
 #   if resultado == "yes": # 'no' si se presiona el botón de cancelar
 #       root.destroy() #destroy: cerrar la ventana
    
 #  resultado = MessageBox.askokcancel("Salir", "Sobreescribir el archivo actual?") #askokcancel: mensaje de pregunta con botones de aceptar y cancelar
 #  if resultado: # 'False' si se presiona el botón de cancelar
 #      root.destroy()

 #   resultado = MessageBox.askyesno("Salir", "Estas seguro que quieres salir?") #askyesno: mensaje de pregunta con botones de si y no
 #   if resultado: # 'False' si se presiona el botón de no
 #       root.destroy()

 #   resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar") #askretrycancel: mensaje de pregunta con botones de reintentar y cancelar
 #   if resultado: # 'False' si se presiona el botón de cancelar
 #       root.destroy()

 # POPUPS AVANZADOS: ------------------------------------------------------------------------------...

 #   color = ColorChooser.askcolor(title="Elige un color")  #askcolor: abrir un selector de color
 #   print(color)

 #   ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", 
                                     # filetypes=(("Ficheros de texto", "*.txt"),
                                                # ("Ficheros de texto avanzado", "*.txt2"),
                                                # ("Todos los ficheros", "*.*")))
    #askopenfilename: abrir un cuadro de diálogo para abrir un archivo
    # Para que funcione tiene que dejarse minimo una coma en filetypes es decir: filetypes=(("Ficheros de texto", "*.txt"),)
    #print(ruta)

                 #Equivale a open('ruta','w')
                 #Asksaveasfile: abrir un cuadro de diálogo para guardar un archivo
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        fichero.write("Hola mundo!")
        fichero.close()

        
Button(root, text="Clícame",command=test).pack()


root.mainloop()