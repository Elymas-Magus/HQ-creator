from unidecode import unidecode
from RarToCbr import *

class App:
    def __init__(self):
        
    def getFileNames(self):
        filename = filedialog.askopenfilenames()
        
        return filename if len(filename) else -1
            
    
    def getPathName(self):
        dirpath = filedialog.askdirectory()
        
        return dirpath if len(dirpath) else -1