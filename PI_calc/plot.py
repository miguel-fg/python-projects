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

window: tk.CTkFrame
side: tk.CTkFrame
canvas: FigureCanvasTkAgg

fig = Figure(figsize = (8,5), dpi=100)
plot_pi = fig.add_subplot()

def get_al(p, state):
    graph = []

    if(state == 'l'):
        for i in range(1, p + 1):
            graph.append(l(i))
    elif(state == 'b'):
        for i in range(1, p + 1):
            graph.append(b(i))
    elif(state == 'c'):
        for i in range(1, p + 1):
            graph.append(c(i))
    else:
        raise Exception("Unkown algorithm state parameter: " + state)
    
    return graph

def plot(f):
    global canvas

    plot_pi.axhline(y=math.pi, color="r", linestyle="-")

    p = int(precision.get())

    if(l_check._check_state):
        pi_leibniz = get_al(p, 'l')
        plot_pi.plot(pi_leibniz)
    if(b_check._check_state):
        pi_bbp = get_al(p, 'b')
        plot_pi.plot(pi_bbp)
    if(c_check._check_state):
        pi_chudnovsky = get_al(p, 'c')
        plot_pi.plot(pi_chudnovsky)

    canvas = FigureCanvasTkAgg(fig, master=f)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

def refresh():
    canvas.get_tk_widget().destroy()
    plot_pi.clear()
    plot(window)


def main_build(f):
    label = tk.CTkLabel(f, text="PI Algorithm visualizer", text_color="white", font=("Roboto", 24))
    label.pack()
    
    plot(f)

def side_build(f):
    global precision, l_check, b_check, c_check, window

    precision_label = tk.CTkLabel(f, text="Algorithm precision")
    precision_label.pack()
    precision = tk.CTkEntry(f)
    precision.insert(0, "100")
    precision.pack(pady=(0, 50))

    l_check = tk.CTkCheckBox(f, text="Leibniz")
    l_check.pack(pady= 10)
    b_check = tk.CTkCheckBox(f, text="BBP")
    b_check.pack(pady=10)
    c_check = tk.CTkCheckBox(f, text="Chudnovsky")
    c_check.pack(pady=10)

    run_button = tk.CTkButton(f, text="Run", width=100, command=refresh)
    run_button.pack(pady=(50, 5))
    exit_button = tk.CTkButton(f, text="Exit", width=100, command=m.destroy)
    exit_button.pack(pady=5)

def app_build():
    global window, side

    m.title("PI visualization")
    m.geometry("1000x700")
    m.minsize(1000, 700)

    window = tk.CTkFrame(frame, width=750, height=650)
    window.grid(row=0, column=0, padx=10, pady=5)

    side = tk.CTkFrame(frame, width=200, height=650)
    side.grid(row=0, column=1, pady=5)

    side_build(side)
    main_build(window)

    m.mainloop()

def main():
    app_build()

if __name__ == "__main__":
    main()