from tkinter import *

class Menu:
    def __init__(self):
        self.menu = Tk()
        self.menu.title(self.config.title)
        
        self.menu_config(self.menu)
        
        btn = Button(self.menu, text = "Executar")
        btn.pack()
        
        self.menu.mainloop()