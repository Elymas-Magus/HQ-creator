from Compressor import Compressor
import os

class Conversor:
    def __init__(self, paths):
        self.initOperation(paths)
    
    def initOperation(self, paths):
        self.setPaths(paths)
        self.compress()
        
    def setPaths(self, paths):
        self.paths = paths
        
    def compress(self):
        self.compressor = Compressor(self.paths["origin"], self.paths["filename"])