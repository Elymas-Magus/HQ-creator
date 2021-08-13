from unidecode import unidecode
from tkinter import *
import PySimpleGUI as sg
import json
import ctypes

class userInput:
    def __init__(self):
        self.title = "HQ generator"
        self.inputContent = {}
        self.layout = None
        self.window = None
        
        self.configPage()
        
        
    def configPage(self):
        user32 = ctypes.windll.user32
        
        self.screensize = {
            'width': user32.GetSystemMetrics(0),
            'height': user32.GetSystemMetrics(1)
        }
        
        self.windowsize = {
            'width': 768,
            'height': 500
        }
        
        self.iconpath = "images/icon-comics-small.ico"
        
    def menu(self):
        menu = Tk()
        menu.title(self.title)
        
        p_x = int((self.screensize['width'] - self.windowsize['width'])/2)
        p_y = int((self.screensize['height'] - self.windowsize['height'])/2)
        
        menu.geometry("{}x{}+{}+{}".format(self.windowsize['width'], self.windowsize['height'], p_x, p_y))
        menu.iconbitmap(self.iconpath)     
        menu['bg'] = '#e9eaff'  
        
        self.getFileNames() 
        
        menu.mainloop()
            
        
    def getFileNames(self):
        filename = filedialog.askopenfilenames()
        
        return filename if len(filename) else -1
            
    
    def getPathName(self):
        dirpath = filedialog.askdirectory()
        
        return dirpath if len(dirpath) else -1