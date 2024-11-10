import tkinter as tk


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


# Crear la ventana
window = tk.Tk()
window.title("Calculadora")

# Definir la entrada
entry = tk.Entry(window, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Definir los botones
buttons = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    ".",
    "=",
    "+",
]

row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(window, text=button, padx=40, pady=20)
    btn.grid(row=row_val, column=col_val)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
