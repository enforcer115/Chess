import board
import square
import tkinter as tk


"""def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    btn_decrease["bg"] = "blue"


window = tk.Tk()

window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=100, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=100, weight=1)

btn_decrease = tk.Button(master=window, command=decrease, bg="black", highlightbackground="grey", text="Q")
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window)
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()

"""
"""
check = board.Board()
check.play_turn(1, 0, 0, 3)
check.play_turn(-1, 1, 1, 2)"""
