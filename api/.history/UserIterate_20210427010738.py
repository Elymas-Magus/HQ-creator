from unidecode import unidecode
import PySimpleGUI as sg

class userInput:
    def __init__(self):
        title = "Conversor de RAR para CBR"
        
        self.layout = [
            [sg.Text(
                "Bem-vindo ao Conversor de RAR/CBR",
                size=(50, 2),
                font = ['Arial', 18],
                text_color = '#01091f',
                justification = 'center'
            )],
            [sg.Button("Converter 1 arquivo", size=(60, 2), key="one_file")],
            [sg.Button("Selecionar arquivos para converter", size=(60, 2), key="multi_files")],
            [sg.Button("Converter arquivos por pasta", size=(60, 2), key="all_files")]
        ]

        self.window = sg.Window(title, size=(500, 225)).layout(self.layout)
        
        while True:
            self.button, self.values = self.window.Read()

            if self.button == 'one_file':
                self.getFileName()
            
            elif self.button == 'multi_files':
                self.getMultiFileName()
            
            elif self.button == 'all_files':
                print('3')

            elif self.button in (sg.WIN_CLOSED, 'close'):
                close = True
                break

        self.window.close()
        
        # print("Escolha uma das opções")
        # input("Digite o caminho do(s) arquivo(s)")