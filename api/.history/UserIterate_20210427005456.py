from unidecode import unidecode
import PySimpleGUI as sg

class userInput:
    def __init__(self):
        self.layout = [
            [sg.Button("Converter 1 arquivo", size=(40, 2), key="start")],
            [sg.Button("Selecionar arquivos para converter", size=(40, 2), key="open")],
            [sg.Button("Fechar", size=(26, 2), key="close")]
        ]

        self.window = sg.Window(title, size=(950, 320)).layout(self.layout)
        
        # print("Escolha uma das opções")
        # input("Digite o caminho do(s) arquivo(s)")