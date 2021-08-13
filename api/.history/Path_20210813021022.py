class Path:
    def __init__ (self, content = None, keys = None):
        self.args = ""
        self.content = content
        self.keys = keys
        
    def setContent(self):
        self.content = content
        
    def toDictionary (self):
        self.args = {}

        for i in range(len(self.keys)):
            self.args[self.keys[i]] = self.content[i]
        
        return self.args