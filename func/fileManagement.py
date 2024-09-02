def getFile(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def createFile(path, content):
    with open(path, "w") as f:
        f.write(content)