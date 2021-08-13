from unidecode import unidecode
import PySimpleGUI as sg

class userInput:
    def __init__(self):
        self.layout = [
            [sg.Button("Converter 1 arquivo", size=(40, 2), key="one_file")],
            [sg.Button("Selecionar arquivos para converter", size=(40, 2), key="multi_files")],
            [sg.Button("Converter arquivos por pasta", size=(40, 2), key="all_files")]
        ]

        self.window = sg.Window(title, size=(950, 320)).layout(self.layout)
        
        # print("Escolha uma das opções")
        # input("Digite o caminho do(s) arquivo(s)")