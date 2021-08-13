import patoolib
import os
import os

class Compressor:
    def __init__(self, folder, filename):
        self.goToFolder(folder)
        self.compress(filename)
        
    def goToFolder(self, folder):
        os.chdir(folder)
        
    def compress(self, filename):
        patoolib.create_archive(filename, tuple(os.listdir('.')))
        
    def moveToDestinationFolder(self, desti)
        