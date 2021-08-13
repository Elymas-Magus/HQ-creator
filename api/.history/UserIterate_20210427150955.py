from unidecode import unidecode
import tkinter as tk
import PySimpleGUI as sg
import json

class userInput:
    def __init__(self):
        self.title = "Conversor de RAR para CBR"
        self.inputContent = {}
        self.layout = None
        self.window = None
        
    def menu(self):
        menu
            
        
    def getFileNames(self):
        filename = filedialog.askopenfilenames()
        
        return filename if len(filename) else -1
            
    
    def getPathName(self):
        dirpath = filedialog.askdirectory()
        
        return dirpath if len(dirpath) else -1