from RarToCbr import ConversorCbr0
import Path

class App:
    def __init__(self, path_list):
        self.path_list = path_list
        self.paths = {}
        self.args = {}
        
        self.config()
        
    def config(self):
        self.args = Path.Path(self.path_list).parseString()

    def setOriginPaths(self):
        return self.path_list[1]

    def setDestinationPath(self):
        return self.path_list[2]

    def setFilename(self):
        return self.path_list[3]
        
        