from RarToCbr import ConversorCbr

class App:
    def __init__(self, path_list):
        self.path_list = path_list
        self.filename = self.getFilename()
        self.paths = {}

    def getDestinationPath(self):
        return self.path_list[1]

    def getFilename(self):
        return self.path_list[2]

    def getOriginPaths(self):
        return self.path_list[3:]
        
        