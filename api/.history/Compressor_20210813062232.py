import patoolib
import shutil
import os

constants = {"extension": ".rar", "hq_format": ".rar"}

class Compressor:
    def __init__(self, paths):
        self.paths = paths
        self.hasError = False
        self.opath = None
        self.dpath = None
        self.config()
        
    def config(self):
        try:        
            self.goToFolder(self.paths["origin"])
            self.compress(self.paths["filename"] + constants["extension"])
            
            
            self.setDestinationPath(self.getPath(self.paths["destiny"], self.paths["filename"]))
            self.setOriginPath(self.getPath(self.paths["origin"], self.paths["filename"]))
            
            self.moveToDestinationFolder()
        except:
            self.hasError = True
        
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
        
    def toCbr(self):
        os.rename(self.dpath, self.getConvertedName())
        print("cheguei")
        
    def getConvertedName(self):
        if self.dpath.endswith(constants["extension"]):
            return self.dpath[:len(self.dpath) - len(constants["extension"])] + constants["hq_format"]
        
    def rollback(self):
        os.chdir(self.paths["origin"])
        
        if os.path.exists(self.paths["filename"] + constants["extension"]) and os.path.isfile(self.paths["filename"] + constants["extension"]):
            os.remove(self.paths["filename"] + constants["extension"])
            
        os.chdir(self.paths["destiny"])
        
        if os.path.exists(self.paths["filename"] + constants["extension"]) and os.path.isfile(self.paths["filename"] + constants["extension"]):
            os.remove(self.paths["filename"] + constants["extension"])
        
        if os.path.exists(self.paths["filename"] + constants["hq_format"]) and os.path.isfile(self.paths["filename"] + constants["hq_format"]):
            os.remove(self.paths["filename"] + constants["hq_format"])
            
        