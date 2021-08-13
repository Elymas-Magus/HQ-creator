import os

class FileOrganizer:
    def __init__(self, path):
        self.path = path
        
        self.createFolder()
        
    def createFolder(self):
        