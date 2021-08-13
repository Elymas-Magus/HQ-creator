class Path:
    def __init__ (self, content, keys):
        self.args = ""
        self.content = content
        self.keys = keys
        
    def toDictionary (self):
        self.args = {}

        for key in range(len(self.keys)):
            self.args[]
        
        return self.args
        
    def each (self, fn):
        temp = []
        newDict = {} 
        for item in self.args:
            temp = fn(item)
            newDict[temp[0]] = temp[1] 
            
        self.args = newDict

    def setOriginPaths(self):
        self.paths["origin"] = self.path_list[1]

    def setDestinationPath(self):
        self.paths["destination"] = self.path_list[2]

    def setFilename(self):
        self.paths["filename"] = self.path_list[3]