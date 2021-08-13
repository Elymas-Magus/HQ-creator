class Path:
    def __init__(self, content):
        self.content = content
        
    def parseString(self):
        args = self.path_list.split("&")