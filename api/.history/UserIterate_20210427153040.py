from unidecode import unidecode
import tkinter as tk
import PySimpleGUI as sg
import json
import ctypes

class userInput:
    def __init__(self):
        self.title = "HQ generator"
        self.inputContent = {}
        self.layout = None
        self.window = None
        user32 = ctypes.windll.user32
        self.screensize = {
            'width': user32.GetSystemMetrics(0),
            'height': user32.GetSystemMetrics(1)
        }
        
    def menu(self):
        menu = tk.Tk()
        menu.title(self.title)
        menu.geometry(f"500x250+{self.screensize(0)}+{self.screensize(1)}")
        menu.mainloop()
            
        
    def getFileNames(self):
        filename = tk.filedialog.askopenfilenames()
        
        return filename if len(filename) else -1
            
    
    def getPathName(self):
        dirpath = tk.filedialog.askdirectory()
        
        return dirpath if len(dirpath) else -1