from RarToCbr import *

class App:
    def __init__(self, path_list):
        self.path_list = path_list
        self.paths = {
            "origem": self.getDestinationPath(),
            "destino": self.getDestinationPath(),
        }

    def getDestinationPath(self):
        return sys.argv[1]

    def getOriginPaths(self):
        return sys.argv[2:]
        
        