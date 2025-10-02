import tkinter as tk
import GUI
import config
import re

mouseX, mouseY = None, None
creature = None

def lines(canvas): # Отрисовка поля
    canvas.delete("all")
    for w in config.objects: # Удаление всех надписей
        if re.match(r".!frame.!canvas.!label\d+", str(w[5])) or re.match(r".!frame.!canvas.!label", str(w[5])):
            print("Label detect")
            w[5].place_forget()
        else:
            print(f"w5: '{str(w[5])}'")
    config.objects.clear() # Очистка поля полностью
    
    rate = 40
    x1 = 35
    x2 = 35
    y1 = 0
    y2 = 577
    for line_y in range(20):
        canvas.create_line(x1, y1, x2, y2)
        x1 += rate
        x2 += rate
    
    y1 = 35
    y2 = 35
    x1 = 0
    x2 = 747
    
    for line_x in range(15):
        canvas.create_line(x1, y1, x2, y2)
        y1 += rate
        y2 += rate

def create_figure_ON(event): # Зажатие клавиши при создании фигуры
    global mouseX, mouseY, current_figureG, creature
    mouseX, mouseY = event.x, event.y
    if config.current_figure == "rect":
        creature = GUI.canvas.create_rectangle(mouseX, mouseY, mouseX, mouseY, outline=config.figure_color, width=3)
    elif config.current_figure == "oval":
        creature = GUI.canvas.create_oval(mouseX, mouseY, mouseX, mouseY, outline=config.figure_color, width=3)
    elif config.current_figure == "line":
        creature = GUI.canvas.create_line(mouseX, mouseY, mouseX, mouseY, fill=config.figure_color, width=3)
    elif config.current_figure == "dot":
        creature = GUI.canvas.create_oval(mouseX - 7, mouseY - 7, mouseX + 7, mouseY + 7, fill=config.figure_color, width=3)
    elif config.current_figure == "signature":
        print(config.current_figure)
        GUI.field_input.place(x=event.x, y=event.y)
        GUI.field_button.place(x=event.x+90, y=event.y)

def create_figure_OFF(event): # Масштабирование фигуры
    global mouseX, mouseY, current_figure, creature
    if config.current_figure in config.scaling:
        GUI.canvas.coords(creature, mouseX, mouseY, event.x, event.y)
    
    
def save_figure(event):# Дополнительное сохранение фигуры
    global mouseX, mouseY, current_figure, creature
    
    if config.figure_color == "gray" and config.lock_color == False:
        config.figure_color = "red"
    elif config.figure_color == "red" and config.lock_color == False:
        config.figure_color = "green"
    elif config.figure_color == "green" and config.lock_color == False:
        config.figure_color = "blue"
    elif config.figure_color == "blue":
        config.figure_color = "gray"
        
    config.objects.append([mouseX, mouseY, event.x, event.y, config.current_figure, creature])
    print(config.objects)
    
def del_last(event=None):
    try:
        obj = config.objects[-1]
        GUI.canvas.delete(obj[5])
        config.objects.remove(obj)
        print("last object removed")
    except IndexError:
        print("Warn: No figures on the field!")
    except Exception as e:
       print(f"Error: {e}")
       obj = config.objects[-1]
       obj[5].place_forget()
       config.objects.remove(obj)
       print("last object removed")
    
def create_sign():
    global mouseX, mouseY
    GUI.field_input.place_forget()
    GUI.field_button.place_forget()
    text = GUI.field_input.get()
    label = tk.Label(GUI.canvas, text=text, width=4, font=("Arial", 12))
    config.objects[-1][5] = label
    label.place(x=mouseX, y=mouseY)
    print(config.objects)
    
    
    

        
        