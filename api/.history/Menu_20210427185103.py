from tkinter import *
from Config import *

class Menu:
    def __init__(self):
        self.config = Config()
        self.init_menu()
        
    def init_menu(self):
        self.menu = Tk()
        self.menu.title(self.config.title)
        
        self.menu_config(self.menu)
        
        btn = Button(self.menu, text = "Executar", command=self.exec_btn_click)
        btn.pack()
        
        self.menu.mainloop()
        
    def menu_config(self, menu):
        p_x = int((self.config.screen['size']['width'] - self.config.window['size']['width'])/2)
        p_y = int((self.config.screen['size']['height'] - self.config.window['size']['height'])/2)
        
        menu.geometry("{}x{}+{}+{}".format(self.config.window['size']['width'], self.config.window['size']['height'], p_x, p_y))
        menu.iconbitmap(self.config.iconpath)     
        menu['bg'] = '#e9eaff'   
        
    def exec_btn_click(self):
        print('hello world\n')