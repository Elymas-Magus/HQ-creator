class ExtensionChange:
    def __init__(self, filename, newExtension):
        newFilename = filename[:len(filename) - 4] + newExtension