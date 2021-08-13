from Conversor import Conversor
from Path import Path

class App:
    def __init__(self, args):
        self.args = args
        self.keys = []
        self.paths = {}
        self.pathController = Path()
        self.conversor = None
        
        self.setKeys()
        self.config(args)
        
    def config(self, path):
        self.pathController.set(path[1:], self.keys)
        if self.pathController.checkPaths():
            self.paths = self.pathController.toDictionary()
            self.conversor = Conversor(self.paths)
        
    def setKeys(self, keys = ["origin", "destiny", "filename"]):
        self.keys = keys
        
        