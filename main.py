import tkinter as tk
import config as c
import GUI
import utils

#    Copyright (c) 2025 ITDenik

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the Licens


# GUI.background.place(x=0, y=0)

# Размещение объектов на экране
GUI.barline.place(x=765, y=0, relheight=1, relwidth=1)
GUI.sidebar.place(x=10, y=0, relheight=1, relwidth=1)
GUI.border_for_zone.place(x=0, y=100)

GUI.base_logo.place(x=150, y=300)
GUI.base_text.place(x=70, y=20)

GUI.sett_btn.place(x=0, y=0)
GUI.rect_btn.place(x=78, y=0)
GUI.oval_btn.place(x=78*2, y=0)
GUI.line_btn.place(x=78*3,y=0)
GUI.dot_btn.place(x=78*4, y=0)
GUI.signature_btn.place(x=78*5, y=0)
GUI.canvas.place(x=5, y=5)
GUI.clear_btn.place(x=0, y=55)
GUI.del_last_btn.place(x=78, y=55)


# Вызов функций
utils.lines(GUI.canvas)

# Логика
GUI.canvas.bind("<Button-1>", utils.create_figure_ON)
GUI.canvas.bind("<B1-Motion>", utils.create_figure_OFF)
GUI.canvas.bind("<ButtonRelease-1>", utils.save_figure)
c.win.bind("<Control-z>", utils.del_last)

c.win.mainloop()
