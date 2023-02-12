#improved GUI framework
import customtkinter as tk

#plotting modules
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#default math modules
import math
from decimal import Decimal, getcontext

#custom PI algorithm implementations
from leibniz import algorithm as l
from bbp import algorithm as b
from chudnovsky import algorithm as c

#setting global window and appearance
m = tk.CTk()
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
frame = tk.CTkFrame(master=m)
frame.pack(fill="both", expand=True)
plt.style.use("dark_background")

#global input variables
precision: tk.CTkEntry
l_check: tk.CTkCheckBox
b_check: tk.CTkCheckBox
c_check: tk.CTkCheckBox

def get_leibniz(p):
    graph = []

    for i in range(1, p + 1):
        graph.append(l(i))
    
    return graph

def get_bbp(p):
    graph = []

    for i in range(1, p + 1):
        graph.append(b(i))
    
    return graph

def get_chudnovsky(p):
    graph = []

    for i in range(1, p + 1):
        graph.append(c(i))
    
    return graph

def plot(f):
    fig = Figure(figsize = (8,5), dpi=100)

    plot_pi = fig.add_subplot()
    plot_pi.axhline(y=math.pi, color="r", linestyle="-")

    p = int(precision.get())

    if(l_check._check_state):
        pi_leibniz = get_leibniz(p)
        plot_pi.plot(pi_leibniz)
    if(b_check._check_state):
        pi_bbp = get_bbp(p)
        plot_pi.plot(pi_bbp)
    if(c_check._check_state):
        pi_chudnovsky = get_chudnovsky(p)
        plot_pi.plot(pi_chudnovsky)

    canvas = FigureCanvasTkAgg(fig, master=f)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

def main_build(f):

    label = tk.CTkLabel(f, text="PI Algorithm visualizer", text_color="white", font=("Roboto", 24))
    label.pack()

    plot(f)
    
    exitButton = tk.CTkButton(f, text="Exit", width=100, command=m.destroy)
    exitButton.pack(pady=10)

def side_build(f):
    global precision, l_check, b_check, c_check

    precision_label = tk.CTkLabel(f, text="Algorithm precision")
    precision_label.pack()
    precision = tk.CTkEntry(f)
    precision.insert(0, "2")
    precision.pack(pady=(0, 50))

    l_check = tk.CTkCheckBox(f, text="Leibniz")
    l_check.select()
    l_check.pack(pady= 10)
    b_check = tk.CTkCheckBox(f, text="BBP")
    b_check.select()
    b_check.pack(pady=10)
    c_check = tk.CTkCheckBox(f, text="Chudnovsky")
    c_check.select()
    c_check.pack(pady=10)

def app_build():
    m.title("PI visualization")
    m.geometry("1000x700")
    m.minsize(1000, 700)

    main = tk.CTkFrame(frame, width=750, height=650)
    main.grid(row=0, column=0, padx=10, pady=5)

    side = tk.CTkFrame(frame, width=200, height=650)
    side.grid(row=0, column=1, pady=5)

    side_build(side)
    main_build(main)

    m.mainloop()

def main():
    app_build()

if __name__ == "__main__":
    main()