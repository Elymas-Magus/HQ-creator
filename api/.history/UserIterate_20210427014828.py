from unidecode import unidecode
from tkinter import filedialog
import PySimpleGUI as sg
import json

class userInput:
    def __init__(self):
        title = "Conversor de RAR para CBR"
        
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

        self.window = sg.Window(title, size=(500, 225)).layout(layout)
        
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
                break

        self.window.close()
        
        print(json.dumps(inputContent))
        
    @staticmethod
    def getMultiFileName():
        return filedialog.askopenfilenames()
        
    @staticmethod
    def getPathName():
        return filedialog.askdirectory()