import patoolib
import shutil
import os

constants = {"extension": ".rar"}

class Compressor:
    def __init__(self, paths):
        self.paths = paths
        
        self.goToFolder(origin)
        self.compress(filename + ".rar")
        
        self.setDestinationPath(self.getPath(detination, filename))
        self.setOriginPath(self.getPath(origin, filename))
        
        self.moveToDestinationFolder()
        
    def getPath(self, folder, filename):
        if not folder.endswith("/"):
            folder = folder + "/"

        if not filename.endswith("/"):
            filename = filename + constants["extension"]    
            
        return r"" + folder + filename  
        
    def goToFolder(self, folder):
        os.chdir(folder)
        
    def compress(self, filename):
        patoolib.create_archive(filename, tuple(os.listdir('.')))
        
    def moveToDestinationFolder(self):
        shutil.move(self.opath, self.dpath)
        
    def setOriginPath(self, path):
        self.opath = path
        
    def setDestinationPath(self, path):
        self.dpath = path

    def findAndDelete(self):
        os.chdir(folder)
        