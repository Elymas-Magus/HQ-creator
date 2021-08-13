from RarToCbr import *

class App:
    def __init__(self, path_list):
        self.path_list = path_list
        self.paths = {
            "origem": self.getOriginPaths(),
            "destino": self.getDestinationPath(),
        }

    def getDestinationPath(self):
        return self.path_list[1]

    def getOriginPaths(self):
        return self.path_list[2:]
        
        