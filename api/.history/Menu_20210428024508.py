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
        
        self.page_title = StringVar()
        self.page_title.set("HQ Generator")
        
        label_page = Label(self.menu, textvariable=self.page_title)
        label_page.pack()
        
        self.root_page = Button(self.menu, text="Voltar", command=lambda: self.open_page('root'))
        
        btn = Button(self.menu, text = "Converter", command=lambda: self.open_page('Converter'))
        btn.pack()
        
        btn = Button(self.menu, text = "Criar", command=lambda: self.open_page('Criar'))
        btn.pack()
        
        self.menu.mainloop()
        
    def config_menu(self):
        pos_x = int((self.config.screen['size']['width'] - self.config.window['size']['width'])/2)
        pos_y = int((self.config.screen['size']['height'] - self.config.window['size']['height'])/2)
        
        self.menu.geometry("{}x{}+{}+{}".format(self.config.window['size']['width'], self.config.window['size']['height'], pos_x, pos_y))
        self.menu.iconbitmap(self.config.iconpath)     
        self.menu['bg'] = '#e9eaff'   
        
    def open_page(self, page):
        self.page_title.set(page)
        print(page)