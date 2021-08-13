from tkinter import *
from Config import *

class Menu:
    def __init__(self):
        self.config = Config()
        self.getMenu()    
        
    def config_menu(self):
        pos_x = int((self.config.screen['size']['width'] - self.config.window['size']['width'])/2)
        pos_y = int((self.config.screen['size']['height'] - self.config.window['size']['height'])/2)
        
        self.menu.geometry("{}x{}+{}+{}".format(self.config.window['size']['width'], self.config.window['size']['height'], pos_x, pos_y))
        self.menu.iconbitmap(self.config.iconpath)     
        self.menu['bg'] = self.config.page_color  
        
        self.menu_lateral_width = 20
        self.menu_lateral_font = "Verdana 12"
        
    def getMenu(self):
        self.menu = Tk()
        self.menu.title(self.config.title)
        
        self.config_menu()
        
        self.page_title = StringVar()
        self.page_title.set("HQ Generator")
        
        label_page = Label(self.menu, textvariable=self.page_title)
        label_page.pack()
        
        self.root_page = Button(self.menu, text="Voltar", command=lambda: self.open_page('root'))
        
        label_convert = Label(
            self.menu,
            text="Converter",
            width=self.menu_lateral_width,
            font=self.menu_lateral_font,
            bg=self.config.page_color,
        )
        
        btn_convert = Button(
            self.menu,
            text="Converter",
            width=self.menu_lateral_width,
            font=self.menu_lateral_font,
            command=lambda: self.open_page('Converter')
        )
        
        label_convert.pack()
        btn_convert.pack()
        
        label_create = Label(
            self.menu,
            text="Criar",
            width=self.menu_lateral_width,
            font=self.menu_lateral_font,
            bg=self.config.page_color
        )
        
        btn_create = Button(
            self.menu, 
            text = "Criar", 
            width=self.menu_lateral_width,
            font=self.menu_lateral_font,
            command=lambda: self.open_page('Criar')
        )
        
        label_create.pack()
        btn_create.pack()
        
        self.menu.mainloop()
        
    def open_page(self, page):
        if page is not 'root':
            self.root_page.pack()
        else:
            self.root_page.clipboard_clear()
            
        self.page_title.set(page)
        print(page)