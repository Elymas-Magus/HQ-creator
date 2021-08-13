from RarToCbr import ConversorCbr
from Path import Path

class App:
    def __init__(self, args):
        self.args = args
        self.keys = []
        self.paths = {}
        self.pathController = Path(path[1:], self.keys)
        
        self.setKeys()
        self.config(args)
        
    def config(self, path):
        self.pathController = Path(path[1:], self.keys)
        self.paths = self.pathController.toDictionary()
        
    def setKeys(self, keys = ["origin", "destiny", "filename"]):
        self.keys = keys
        
    def 
        
        
        