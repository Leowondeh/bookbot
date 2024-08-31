def getFile(path):
    with open(path) as f:
        contents = f.read()
        return contents