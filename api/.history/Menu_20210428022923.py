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
        
        label_title = Label(self.menu, text = "HQ Generator")
        label_title.pack()
        
        btn = Button(self.menu, text = "Executar", command=self.exec_btn_click)
        btn.pack()
        
        btn = Button(self.menu, text = "Executar", command=self.exec_btn_click)
        btn.pack()
        
        btn = Button(self.menu, text = "Executar", command=self.exec_btn_click)
        btn.pack()
        
        self.menu.mainloop()
        
    def config_menu(self):
        pos_x = int((self.config.screen['size']['width'] - self.config.window['size']['width'])/2)
        pos_y = int((self.config.screen['size']['height'] - self.config.window['size']['height'])/2)
        
        self.menu.geometry("{}x{}+{}+{}".format(self.config.window['size']['width'], self.config.window['size']['height'], pos_x, pos_y))
        self.menu.iconbitmap(self.config.iconpath)     
        self.menu['bg'] = '#e9eaff'   
        
    def exec_btn_click(self):
        print('hello world')