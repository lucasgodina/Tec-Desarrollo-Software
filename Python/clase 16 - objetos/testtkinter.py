import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.config(width=800, height=600)

boton1 = tk.Button(ventana, text="Hola mundo")
boton1.place(x=100, y=100, width=100, height=50)

ventana.mainloop()