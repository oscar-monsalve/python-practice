import tkinter as tk
# from tkinter import *

window = tk.Tk()


def write() -> None:
    print(f"Este es el texto de entrada {text_in}")

# TODO: make an array of button from 0 to 9 as in a calculator.
# lbl = tk.Label(window, text="Ingrese los parámetros")
# lbl.grid(column=0, row=0)
# for i in range(3):
#     btn = tk.Button(window, text=str(i))
#     btn.grid(column=i, row=0)
#     for k in range(3):
#         btn = tk.Button(window, text=str(k))
#         btn.grid(column=k, row=i)


text_in = tk.StringVar()
text_out = tk.StringVar()

window.title("Calculador de tiro parabólico")
lbl = tk.Label(window, text="Ingrese los parámetros")
lbl.grid(column=0, row=0)

btn = tk.Button(window, text="Calcular", command=write)
btn.grid(column=1, row=0)

texto_entrada = tk.Entry(window)
texto_entrada.grid(column=2, row=0)
texto_entrada.config(textvariable=text_in)

# lbl1 = tk.Label(window, text="Defecto")
# lbl1.grid(column=1, row=2)
# lbl1.config(textvariable=text_out)

window.geometry("350x200")
window.mainloop()
