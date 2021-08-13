from RarToCbr import *

class App:
    def __init__(self, path_destino, path_origem):
        self.paths = {
            "origem": path_origem,
            "destino": path_destino,
        }

    def getDestinationPath(self):
        return sys.argv[1]

    def getOriginPaths(self):
        return sys.argv[2:]
        
        