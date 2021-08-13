# Supported archive formats
ArchiveFormats = (
    '7z', 'ace', 'adf', 'alzip', 'ape', 'ar', 'arc', 'arj',
    'bzip2', 'cab', 'chm', 'compress', 'cpio', 'deb', 'dms',
    'flac', 'gzip', 'iso', 'lrzip', 'lzh', 'lzip', 'lzma', 'lzop',
    'rar', 'rpm', 'rzip', 'shar', 'shn', 'tar', 'vhd', 'xz',
    'zip', 'zoo', 'zpaq')


class ExtensionChange:
    def __init__(self, filename, newExtension):
        self.checkFilename()
        self.setFilename(filename, newExtension)
        
    def setFilename(self, filename, newExtension):
        self.newFilename = filename[:len(filename) - 4] + newExtension
        
    def checkFilename(self):
        