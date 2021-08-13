from unidecode import unidecode
import PySimpleGUI as sg

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
            [sg.Button("Converter 1 arquivo", size=(60, 2), key="one_file")],
            [sg.Button("Selecionar arquivos para converter", size=(60, 2), key="multi_files")],
            [sg.Button("Converter arquivos por pasta", size=(60, 2), key="all_files")]
        ]

        self.window = sg.Window(title, size=(500, 225)).layout(layout)
        
        while True:
            self.button, self.values = self.window.Read()

            if self.button == 'one_file':
                inputContent = self.getFileName()
                break
            
            elif self.button == 'multi_files':
                inputContent = self.getMultiFileName()
                break
            
            elif self.button == 'all_files':
                inputContent = self.getPathName()
                break

            elif self.button in (sg.WIN_CLOSED, 'close'):
                close = True
                break

        self.window.close()
        
    def getFileName(self):
        title = "Get File Name"
    
        of_layout = [
            [sg.Text(
                "Insira o nome do arquivo",
                size=(50, 2),
                font = ['Arial', 14],
                text_color = '#01091f',
                justification = 'center'
            )],
            [sg.Text('Nome do Arquivo'), sg.Input(key="file_name"), sg.Button('Ok', key='ok')],
        ]

        of_window = sg.Window(title, size=(500, 150)).layout(of_layout)
        
    
        while True:
            button, values = of_window.Read()

            if button == 'ok':
                print(values)
                break
            
            elif button in (sg.WIN_CLOSED, 'close'):
                close = True
                break

        of_window.close()
        
    def getMultiFileName(self):
        print('d')
        
    def getPathName(self):
        print('d')
        # print("Escolha uma das opções")
        # input("Digite o caminho do(s) arquivo(s)")