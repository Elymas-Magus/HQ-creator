from RarToCbr import ConversorCbr
import Path

class App:
    def __init__(self, path_list):
        self.path_list = path_list
        self.paths = {}
        self.args = {}
        
        self.config()
        
    def config(self):
        self.args = Path.Path(self.path_list).parseString()

    def getDestinationPath(self):
        return self.path_list[1]

    def getFilename(self):
        return self.path_list[2]

    def getOriginPaths(self):
        return self.path_list[3:]
        
        