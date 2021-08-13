from RarToCbr import ConversorCbr
from Path import Path

class App:
    def __init__(self, path_list):
        self.path_list = path_list
        self.paths = {}
        
        self.config(path_list)
        
    def config(self, path):
        self.args = Path(path[1:]).toDictionary()
        
        