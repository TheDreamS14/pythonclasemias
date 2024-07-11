#importacion de librerias y modelos
import tkinter as tk 
from tkinter import messagebox

#codigo de bruto
def mensaje(): 
    messagebox.showinfo("nombre de la caja de texto", "mensaje")

root = tk.Tk()
root.title("interfaz simple")
root.geometry("300x200") #alto x ancho


#crear boton
boton = tk.Button(root, text = "CP aqui", command=mensaje)
boton.pack(pady=20)

root.mainloop()