import os

def getFile(path):
    with open(path) as f:
        contents = f.read()
        return contents

def getVersion():
    return getFile('version')
def createFileWrite(path, content):
    with open(path, "w") as f:
        f.write(content)

def createReportFile(path, content):
    try:
        with open(f'reports/{path}', "w+") as f:
            f.write(content)
    except FileNotFoundError:
        os.system('mkdir reports')
        with open(f'reports/{path}', "w+") as f:
            f.write(content)
            
    # Print confirmation
    print(f"Wrote report to reports/{path}")