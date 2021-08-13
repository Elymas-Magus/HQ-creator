from RarToCbr import ConversorCbr
from Path import Path

class App:
    def __init__(self, path_list):
        self.path_list = path_list
        self.paths = {}
        
        self.config(path_list)
        
    def config(self, path):
        self.paths = Path(path[1:], self.keys).toDictionary()
        
    def setKeys(keys = ["origin", "destiny", "filename"]):
        self.keys = keys
        
        
        