import os

def get_file(path):
    with open(path) as f:
        contents = f.read()
        return contents

def create_file_write(path, content = ''):
    with open(path, "w") as f:
        f.write(content)

def create_report_file(path, content):
    try:
        with open(f'reports/{path}', "w+") as f:
            f.write(content)
    except FileNotFoundError:
        os.system('mkdir reports')
        with open(f'reports/{path}', "w+") as f:
            f.write(content)
            
    # Print confirmation
    print(f"Wrote report to reports/{path}")