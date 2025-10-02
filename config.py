import tkinter as tk
#C:/Users/Наташа/Desktop/Проекты Дениса/проекты Java и Python/Python/Geometry/main.py

win = tk.Tk()
width, height = 1000, 650
win.geometry(f"{width}x{height}+100+30")
win.title("Апофема2D")
win.iconbitmap("img/Logo.ico")

lock_color = False
current_figure = "rect"
figure_color = "gray"
scaling = ["rect", "oval", "line"]

objects = [] # Список фигур на поле