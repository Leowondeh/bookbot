def read_options():
    with open('options') as f:
        current_options = f.readline()
        current_options = current_options.split(", ")
    return current_options