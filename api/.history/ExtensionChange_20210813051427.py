class ExtensionChange:
    def __init__(self, filename, newExtension):
        self.newFilename = filename[:len(filename) - 4] + newExtension
        
    def setFilename