import tkinter as tk

window = tk.Tk()


def write() -> None:
    print(f"Este es el texto de entrada {text_in}")


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
