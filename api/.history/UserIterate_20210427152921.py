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
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        
        print(screensize)
        
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