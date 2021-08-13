from unidecode import unidecode
import PySimpleGUI as sg

class userInput:
    def __init__(self):
        self.layout = [
            [sg.Text(values=self.content, size=(940, 15))],
            [sg.Button('Remover', size=(200, 2), key='ok')]
        ]

        self.window = sg.Window(title, size=(950, 320)).layout(self.layout)
        
        # print("Escolha uma das opções")
        # input("Digite o caminho do(s) arquivo(s)")