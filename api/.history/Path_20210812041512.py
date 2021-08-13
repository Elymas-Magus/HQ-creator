class Path:
    def __init__ (self, content):
        self.args = ""
        self.content = content
        
    def parseString (self):
        self.args = self.content.split("&")
        
        self.each(lambda item : item.split("="))
        
    def each (self, fn):
        temp = []
        newDict = {} 
        for item in self.args:
            temp = fn(item)
            newDict[temp[0]] = temp[1] 