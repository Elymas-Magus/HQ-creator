class Menu:
    def __init__(self):
        self.menu = Tk()
        menu.title(self.config.title)
        
        self.menu_config(menu)
        
        btn = Button(menu, text = "Executar")
        btn.pack()
        
        menu.mainloop()