class ExtensionChange:
    def __init__(self, filename, newExtension):
        self.checkFilename()
        self.setFilename(filename, newExtension)
        
    def setFilename(self, filename, newExtension):
        self.newFilename = filename[:len(filename) - 4] + newExtension