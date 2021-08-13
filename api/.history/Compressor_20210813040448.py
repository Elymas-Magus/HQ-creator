import patoolib
import shutil
import os

constants = (".rar")

class Compressor:
    def __init__(self, origin, detination, filename):
        self.goToFolder(origin)
        self.compress(filename)
        self.setDestinationPath(r"" + detination + "/" + filename + ".rar")
        self.setOriginPath(r"" + origin + "/" + filename + ".rar")
        self.moveToDestinationFolder(origin, detination, filename)
        
    def goToFolder(self, folder):
        os.chdir(folder)
        
    def compress(self, filename):
        patoolib.create_archive(filename + ".rar", tuple(os.listdir('.')))
        
    def moveToDestinationFolder(self, origin, detination, filename):
        shutil.move(, r"" + detination + ".rar")
        
    def setOriginPath(self, path):
        self.opath = path
        
    def setDestinationPath(self, path):
        self.dpath = path
