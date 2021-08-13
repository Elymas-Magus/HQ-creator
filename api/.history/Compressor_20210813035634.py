import patoolib
import shutil
import os

class Compressor:
    def __init__(self, origin, detination, filename):
        self.goToFolder(origin)
        self.compress(filename)
        
    def goToFolder(self, folder):
        os.chdir(folder)
        
    def compress(self, filename):
        patoolib.create_archive(filename, tuple(os.listdir('.')))
        
    def moveToDestinationFolder(self, origin, detination)
        shutil.move(origin,detination)
