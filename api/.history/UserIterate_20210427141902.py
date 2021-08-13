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

        self.window = sg.Window(self.title, size=(500, 175)).layout(self.layout)
        
        while True:
            self.button, self.values = self.window.Read()
            
            if self.button == 'multi_files':
                filename = self.getFileNames()
                
                if filename == -1:
                    continue
                
                self.inputContent = {'type': 'multi', 'path': filename, 'closed': False}
                break
            
            elif self.button == 'all_files':
                dirpath = self.getPathName()
                
                if dirpath == -1:
                    continue
                
                self.inputContent = {'type': 'all', 'path': dirpath, 'closed': False}
                break

            elif self.button in (sg.WIN_CLOSED, 'close'):
                self.inputContent = {'type': 'exit', 'path': '', 'closed': True}
                break

        self.window.close()        
        
    def getInput(self):
        print(json.dumps(self.inputContent))
        return self.inputContent
        
    def getLayout(self):
        return [
            [sg.Text(
                "Bem-vindo ao Conversor de RAR/CBR",
                size=(50, 2),
                font = ['Arial', 18],
                text_color = '#01091f',
                justification = 'center'
            )],
            [sg.Button("Selecionar arquivos (.rar) para converter", size=(60, 2), key="multi_files")],
            [sg.Button("Converter arquivos (.rar) por pasta", size=(60, 2), key="all_files")]
        ]
        
    def newOperation(self):
        layout = [
            [sg.Text("Deseja fazer nova conversão?")],
            [sg.Button("OK", size=(30, 2), key="btn_ok"), sg.Button("Cancel", size=(30, 2), key="btn_cancel")]
        ]

        window = sg.Window(self.title, size=(500, 90)).layout(layout)
        
        while True:
            button, values = window.Read()
            
            if button == 'btn_ok':
                window.close()
                return True
                
            elif button == 'btn_cancel' or button in (sg.WIN_CLOSED, 'close'):
                window.close()
                return False
            
        
    def getFileNames(self):
        filename = filedialog.askopenfilenames()
        
        return filename if len(filename) else -1
            
    
    def getPathName(self):
        dirpath = filedialog.askdirectory()
        
        return dirpath if len(dirpath) else -1