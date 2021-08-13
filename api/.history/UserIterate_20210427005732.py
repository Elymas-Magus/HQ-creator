from unidecode import unidecode
import PySimpleGUI as sg

class userInput:
    def __init__(self):
        title = "Conversor de RAR para CBR"
        
        self.layout = [
            [sg.Button("Converter 1 arquivo", size=(40, 2), key="one_file")],
            [sg.Button("Selecionar arquivos para converter", size=(40, 2), key="multi_files")],
            [sg.Button("Converter arquivos por pasta", size=(40, 2), key="all_files")]
        ]

        self.window = sg.Window(title, size=(950, 320)).layout(self.layout)
        
        while True:
            self.button, self.values = self.window.Read()

            if self.button == 'start':
                self.iniciar ()
            
            elif self.button == 'open':
                self.abrir ()

            elif self.button in (sg.WIN_CLOSED, 'close'):
                close = True
                break

            elif self.live.inscritos == None or self.live.siex == None or self.live.error:
                close = True
                break

        self.window.close()
        
        # print("Escolha uma das opções")
        # input("Digite o caminho do(s) arquivo(s)")