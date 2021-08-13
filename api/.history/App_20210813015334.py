from RarToCbr import ConversorCbr
from Path import Path

class App:
    def __init__(self, path_list):
        self.path_list = path_list
        self.paths = {}
        self.args = {}
        
        self.config()
        
    def config(self):
        self.args = Path.Path(self.path_list).toDictionary()

    def setOriginPaths(self):
        self.paths["origin"] = self.path_list[1]

    def setDestinationPath(self):
        self.paths["destination"] = self.path_list[2]

    def setFilename(self):
        self.paths["filename"] = self.path_list[3]
        
        