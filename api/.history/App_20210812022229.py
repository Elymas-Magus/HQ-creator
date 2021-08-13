from unidecode import unidecode
from RarToCbr import *

class main_app:
    def __init__(self):
        self.menu = None
        
        
    def init_menu(self):
        self.menu = Menu()               
        
    def getFileNames(self):
        filename = filedialog.askopenfilenames()
        
        return filename if len(filename) else -1
            
    
    def getPathName(self):
        dirpath = filedialog.askdirectory()
        
        return dirpath if len(dirpath) else -1