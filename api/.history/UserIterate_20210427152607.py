from unidecode import unidecode
import tkinter as tk
import PySimpleGUI as sg
import json

class userInput:
    def __init__(self):
        self.title = "HQ generator"
        self.inputContent = {}
        self.layout = None
        self.window = None
        
    def menu(self):
        menu = tk.Tk()
        menu.title(self.title)
        menu.geometry("500x250+200+200")
        menu.mainloop()
            
        
    def getFileNames(self):
        filename = tk.filedialog.askopenfilenames()
        
        return filename if len(filename) else -1
            
    
    def getPathName(self):
        dirpath = tk.filedialog.askdirectory()
        
        return dirpath if len(dirpath) else -1