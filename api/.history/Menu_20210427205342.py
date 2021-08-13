from tkinter import *
from Config import *

class Menu:
    def __init__(self):
        self.config = Config()
        self.getMenu()
        
    def getMenu(self):
        self.menu = Tk()
        self.menu.title(self.config.title)
        
        self.config_menu()
        
        btn = Button(self.menu, text = "Executar", command=self.exec_btn_click)
        btn.pack()
        
        self.menu.mainloop()
        
        btn = Button(self.menu, text = "Teste", command=self.exec_btn_click)
        btn.pack()
        
    def config_menu(self):
        pos_x = int((self.config.screen['size']['width'] - self.config.window['size']['width'])/2)
        p_y = int((self.config.screen['size']['height'] - self.config.window['size']['height'])/2)
        
        self.menu.geometry("{}x{}+{}+{}".format(self.config.window['size']['width'], self.config.window['size']['height'], p_x, p_y))
        self.menu.iconbitmap(self.config.iconpath)     
        self.menu['bg'] = '#e9eaff'   
        
    def exec_btn_click(self):
        print('hello world')