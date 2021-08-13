from unidecode import unidecode
from tkinter import filedialog
import PySimpleGUI as sg
import json

class userInput:
    def __init__(self):
        self.title = "Conversor de RAR para CBR"
        self.inputContent = {}
        self.layout = None
        self.window = None
        
    def menu(self):
        self.layout = self.getLayout()

        self.window = sg.Window(self.title, size=(500, 200)).layout(self.layout)
        
        while True:
            self.button, self.values = self.window.Read()
            
            if self.button == 'multi_files':
                filename = self.getMultiFileName()
                inputContent = {'type': 'multi', 'path': filename}
                break
            
            elif self.button == 'all_files':
                dirpath = self.getPathName()
                inputContent = {'type': 'all', 'path': dirpath}
                break

            elif self.button in (sg.WIN_CLOSED, 'close'):
                close = True
                inputContent = {'type': 'exit', 'path': ''}
                break

        self.window.close()
        
        print(json.dumps(self.inputContent))
        return inputContent
        
    def getLayout(self):
        layout = [
            [sg.Text(
                "Bem-vindo ao Conversor de RAR/CBR",
                size=(50, 2),
                font = ['Arial', 18],
                text_color = '#01091f',
                justification = 'center'
            )],
            [sg.Button("Selecionar arquivos para converter", size=(60, 2), key="multi_files")],
            [sg.Button("Converter arquivos por pasta", size=(60, 2), key="all_files")]
        ]
        
    @staticmethod
    def getMultiFileName():
        return filedialog.askopenfilenames()
        
    @staticmethod
    def getPathName():
        return filedialog.askdirectory()