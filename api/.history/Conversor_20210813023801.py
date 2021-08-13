class Conversor:
    def __init__(self, paths):
        self.initOperation(paths)
    
    def initOperation(self, paths):
        self.setPaths(paths)
        
    def setPaths(self, paths):
        self.paths = paths