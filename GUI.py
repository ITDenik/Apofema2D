import tkinter as tk
import config as c
import text as txt
import image
import  utils
from tkinter import font

#print(font.families())
button_color = "#2E34A6"
Btext_color = "#FFFFFF"
active_button_color = "#3498DB"
sidebar_color = "#303848"
barline_color = "#111E36"

app_logo = tk.PhotoImage(file="img/Logo.png")
app_logo = app_logo.subsample(15, 15)

# bg_img = tk.PhotoImage(file="img/bg1.png", width=1700, height=1000).zoom(2, 2)
# background = tk.Label(c.win, image=bg_img)
c.win.configure(bg="#1C2237")

def BaseFont(size):
    ft = font.Font(family="Comic Sans MS", size=size)
    return ft

def choose_rect():
    c.current_figure = "rect"
    rect_btn.configure(bg=active_button_color)
    oval_btn.configure(bg=button_color)
    line_btn.configure(bg=button_color)
    dot_btn.configure(bg=button_color)
    signature_btn.configure(bg=button_color)
    
def choose_oval():
    c.current_figure = "oval"
    oval_btn.configure(bg=active_button_color)
    rect_btn.configure(bg=button_color)
    line_btn.configure(bg=button_color)
    dot_btn.configure(bg=button_color)
    signature_btn.configure(bg=button_color)
    
def choose_line():
    c.current_figure = "line"
    line_btn.configure(bg=active_button_color)
    rect_btn.configure(bg=button_color)
    oval_btn.configure(bg=button_color)
    dot_btn.configure(bg=button_color)
    signature_btn.configure(bg=button_color)

def choose_dot():
    c.current_figure = "dot"
    dot_btn.configure(bg=active_button_color)
    line_btn.configure(bg=button_color)
    rect_btn.configure(bg=button_color)
    oval_btn.configure(bg=button_color)
    signature_btn.configure(bg=button_color)
    
def choose_sign():
    c.current_figure = "signature"
    signature_btn.configure(bg=active_button_color)
    dot_btn.configure(bg=button_color)
    line_btn.configure(bg=button_color)
    rect_btn.configure(bg=button_color)
    oval_btn.configure(bg=button_color)       
    
    
border_for_zone = tk.Frame(c.win, bg="#3C465A", width=765, height=595)
canvas = tk.Canvas(border_for_zone, width=750, height=580, bg="#F8F9FA")
#canvas.create_rectangle(4, 4, 750, 580, outline="blue", width=5)

sett_btn = tk.Button(c.win, text=txt.settings, width=10, height=3, bg=button_color, fg=Btext_color)
clear_btn = tk.Button(c.win, text=txt.clear, width=10, height=2, command=lambda: utils.lines(canvas), bg="#062D68", activebackground="#E92E2E", fg=Btext_color)
del_last_btn = tk.Button(c.win, text=txt.last, width=18, height=2, command=lambda: utils.del_last(), bg="#062D68", activebackground="#E92E2E", fg=Btext_color)
rect_btn = tk.Button(c.win, text=txt.rect, width=10, height=3, command=choose_rect, bg=button_color, fg=Btext_color)
oval_btn = tk.Button(c.win, text=txt.oval, width=10, height=3, command=choose_oval, bg=button_color, fg=Btext_color)
line_btn = tk.Button(c.win, text=txt.line, width=10, height=3, command=choose_line, bg=button_color, fg=Btext_color)
dot_btn = tk.Button(c.win, text=txt.dot, width=10, height=3, command=choose_dot, bg=button_color, fg=Btext_color)
signature_btn = tk.Button(c.win, text=txt.signature, width=10, height=3, command=choose_sign, bg=button_color, fg=Btext_color)

barline = tk.Frame(c.win, bg=barline_color, width=50)
sidebar = tk.Frame(barline, bg=sidebar_color, width=50)

field_input = tk.Entry(canvas, width=7, font=("Arial", 16), highlightcolor="#000000")
field_button = tk.Button(canvas, text=txt.enter, height=1, bg="#B4F7F4", command=utils.create_sign)

base_logo = tk.Label(sidebar, image=app_logo, bg=sidebar_color)

base_text = tk.Label(sidebar, bg=sidebar_color, text=txt.welcome, font=BaseFont(20), fg=Btext_color, anchor="center")
