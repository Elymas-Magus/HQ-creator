from unidecode import unidecode
import PySimpleGUI as sg

class userInput:
    def __init__(self):
        title = "Conversor de RAR para CBR"
        
        self.layout = [
            [sg.Text(
                "Bem-vindo ao Conversor de RAR/CBR",
                size=(50, 2), auto_size_text = None,
                font = None,
                text_color = None,
                justification = None
            )],
            [sg.Text("\n", size=(50, 2))],
            [sg.Button("Converter 1 arquivo", size=(50, 2), key="one_file")],
            [sg.Button("Selecionar arquivos para converter", size=(50, 2), key="multi_files")],
            [sg.Button("Converter arquivos por pasta", size=(50, 2), key="all_files")]
        ]

        self.window = sg.Window(title, size=(450, 320)).layout(self.layout)
        
        while True:
            self.button, self.values = self.window.Read()

            if self.button == 'one_file':
                print('1')
            
            elif self.button == 'multi_files':
                print('2')
            
            elif self.button == 'all_files':
                print('3')

            elif self.button in (sg.WIN_CLOSED, 'close'):
                close = True
                break

        self.window.close()
        
        # print("Escolha uma das opções")
        # input("Digite o caminho do(s) arquivo(s)")