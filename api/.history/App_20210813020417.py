from RarToCbr import ConversorCbr
from Path import Path

class App:
    def __init__(self, args):
        self.args = args
        self.paths = {}
        
        self.setKeys()
        self.config(args)
        
    def config(self, path):
        self.paths = Path(path[1:], self.keys).toDictionary()
        
    def setKeys(self, keys = ["origin", "destiny", "filename"]):
        self.keys = keys
        
        
        