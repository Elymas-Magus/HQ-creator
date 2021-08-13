class Path:
    def __init__ (self, content = None, keys = None):
        self.args = ""
        self.content = content
        self.keys = keys
        
    def set(self, keys):
        self.keys = keys
        
    def setContent(self, content):
        self.content = content
        
    def setKeys(self, keys):
        self.keys = keys
        
    def toDictionary (self):
        self.args = {}

        for i in range(len(self.keys)):
            self.args[self.keys[i]] = self.content[i]
        
        return self.args