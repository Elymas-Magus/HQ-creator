import patoolib
import os

class Compressor:
    def __init__(self, folder, filename):
        self.goToFolder(folder)
        self.compress()
        
    def goToFolder(self, folder):
        os.chdir(folder)
        
    def compress(self):
        patoolib.create_archive("teste.rar", tuple(os.listdir('.')))
        