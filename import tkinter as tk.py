import tkinter as tk 
from tkinter import messagebox

def Mensaje():
    messagebox.showinfo("Info", "Test1")

    root  = tk.Tk
    root.title("Test 1")
    root.geometry ("600x600")

    label  tk.Label (root, text="esto es un test")
    label.pack (pady= 5)

    button = tk.Button(root, text="Boton", Mensaje)
    button.pack(pady= 5)