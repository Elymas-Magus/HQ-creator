import patoolib

class Compressor:
    def __init__(self):
        patoolib.create_archive("teste.rar", tuple(os.listdir('.')))
        
    def goToFolder(self, folder):
        os.chdir(folder)