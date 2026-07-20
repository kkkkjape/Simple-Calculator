import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]  
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", ]

row_count = len(button_values)#5
column_count = len(button_values[0])#4

color_light_gray = "#D4D4D2"
color_blackboard = "#1C1C1C"
color_heather_gray = "#505050"
color_vivid_gamboge = "#FF9500"
color_white = "#FFFFFF"

window = tk.Tk()
window.title("Simple Calculator")
window.resizable(False, False)

frame = tk.Frame(window, bg=color_blackboard)
label = tk.Label(frame, text="0", anchor=tk.E, bg=color_blackboard, fg=color_white, padx=10, font=("Arial", 45))

label.grid(row=0, column=0, columnspan=column_count, sticky="nsew")

frame.pack(fill=tk.BOTH, expand=True)

window.mainloop()