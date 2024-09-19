import tkinter as tk


def write(value: str) -> None:
    current_text = display.get()
    display.delete(0, tk.END)  # Clear the display
    display.insert(0, current_text + value)  # Insert the new value


window = tk.Tk()
window.title("Basic calculator")

buttons = [
    ["7", 0, 1], ["8", 1, 1], ["9", 2, 1],
    ["4", 0, 2], ["5", 1, 2], ["6", 2, 2],
    ["1", 0, 3], ["2", 1, 3], ["3", 2, 3],
    ["0", 0, 4], [".", 1, 4], ["%", 2, 4],
]

for k, col, row in buttons:
    btn_col = tk.Button(window, text=k, command=lambda k=k: write(k), bd=1, width=2, height=2, font="10")
    btn_col.grid(column=col, row=row)

display = tk.Entry(window)
display.grid(column=0, row=0, columnspan=3)

exit_btn = tk.Button(window, text="Exit", font="10", command=window.quit)
exit_btn.grid(column=3, row=0)

window.mainloop()
