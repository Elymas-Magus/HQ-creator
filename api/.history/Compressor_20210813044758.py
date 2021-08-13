import patoolib
import shutil
import os

constants = {"extension": ".rar"}

class Compressor:
    def __init__(self, paths):
        self.paths = paths
        
        self.goToFolder(self.paths["origin"])
        self.compress(self.paths["filename"] + constants["extension"])
        
        self.setDestinationPath(self.getPath(self.paths["detination"], self.paths["filename"]))
        self.setOriginPath(self.getPath(self.paths["origin"], self.paths["filename"]))
        
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
        os.chdir(self.paths["origin"])
        
        if os.path.exists(self.paths["filename"] + constants["extension"]) and os.path.isfile(self.paths["filename"] + constants["extension"]):
            os.remove(self.paths["filename"] + constants["extension"])
            
        os.chdir(self.paths["destiny"])
        
        if os.path.exists(self.paths["filename"] + constants["extension"]) and os.path.isfile(self.paths["filename"] + constants["extension"]):
            os.remove(self.paths["filename"] + constants["extension"])
            
        