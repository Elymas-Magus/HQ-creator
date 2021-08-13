class ExtensionChange:
    def __init__(self, filename, newExtension):
        filename = filename[:len(filename) - 4] + newExtension