import os
def write_file(file_name, file_content):
    path = f"{file_name}.txt"
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, 'w') as f:
        f.write(file_content) 
        pass

def append_file(file_name, append_content):
    path = f"{file_name}.txt"
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, 'a') as f:
        f.write(append_content)
    pass

def read_file(file_name):
    path = f"{file_name}.txt"
    with open(path, 'r') as f:
        return f.read()
    pass