from Compressor import Compressor

class Conversor:
    def __init__(self, paths):
        self.initOperation(paths)
    
    def initOperation(self, paths):
        try:
            self.setPaths(paths)
            self.compress()
        except:
            self.rollback()
        
    def setPaths(self, paths):
        self.paths = paths
        
    def compress(self):
        self.compressor = Compressor(self.paths["origin"], self.paths["filename"])
        
    def convertToCbr(self):
        self.compressor = Compressor(self.paths["origin"], self.paths["filename"])
        
    def rollback()