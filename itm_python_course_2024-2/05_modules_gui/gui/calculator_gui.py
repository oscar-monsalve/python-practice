import tkinter as tk

window = tk.Tk()
window.title("Basic calculator")

buttons = [
    ["7", 0, 1], ["8", 1, 1], ["9", 2, 1],
    ["4", 0, 2], ["5", 1, 2], ["6", 2, 2],
    ["1", 0, 3], ["2", 1, 3], ["3", 2, 3],
    ["0", 0, 4], [".", 1, 4], ["%", 2, 4],
]

entry = tk.Entry(window).grid(columnspan=3)

for k, col, row in buttons:
    btn_col = tk.Button(window, text=k, bd=1, width=2, height=2, font="10")
    btn_col.grid(column=col, row=row)

exit_btn = tk.Button(window, text="Exit", font="10", command=window.destroy)
exit_btn.grid(column=3, row=0)

window.mainloop()
