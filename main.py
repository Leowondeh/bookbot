import os, platform, tkinter as tk

# input optimizer (only linux)
if platform.system() == 'Linux':
    import readline

import uuid

from func.send_greeting import *
from func.converts import *
from func.file_management import *
from func.read_options import *
from func.count_chars import *
from func.count_words import *
from options_main_menu import *

version = '1.2.1'

# Generate report
def generate_report(file_path, window_mode = False):
    # Permission and existence check
    try:
        get_file(file_path)
    except PermissionError:
        if window_mode:
            return "Error when accessing file: no permission!"
        print("Error when accessing file: no permission!")

    current_options = read_options() # Import options
    try:
        text_to_print = f'======== REPORT for {file_path[file_path.rindex("/") + 1:]} ========\n'
    except ValueError:
        text_to_print = f'======== REPORT for {file_path} ========\n'
    text_to_print += '\n'
    text_to_print += f'    * Word count: {count_words(get_file(file_path))}\n'
    text_to_print += '\n'
    text_to_print += '    * Character counts:\n'

    # Charcount and check for options
    if bool(int(current_options[5])):
        for dict in convert_to_sorted_list(count_chars(get_file(file_path))):
            if dict['char'] == '\n':
                pass
            elif dict['char'] == ' ':
                text_to_print += (f'       > [space] was found {dict["count"]} times\n')
            else:
                text_to_print += (f'       > {dict["char"]} was found {dict["count"]} times\n')
    else:
        for dict in convert_to_sorted_list(count_chars(get_file(file_path))):
            if dict['char'].isalpha():
                text_to_print += (f'       > {dict["char"]} was found {dict["count"]} times\n')
            elif dict['char'] == ' ':
                pass # Exclude spaces

    text_to_print += '\n'
    text_to_print += f'    * Vowel count: {count_vowels_and_consonants(get_file(file_path))[0]}\n'
    text_to_print += f'    * Consonant count: {count_vowels_and_consonants(get_file(file_path))[1]}'
    text_to_print += '\n'
    text_to_print += '=================================='

    # Check save first to optimize time
    if bool(int(current_options[3])):
        create_report_file(f'{uuid.uuid4()}-{file_path[file_path.rindex("/") + 1:]}', text_to_print)
        # File format: (random uuid)-(filename).txt

    if bool(int(current_options[1])):
        send_greeting('quickexit')
        quit()
    
    if window_mode:
        return text_to_print
    else:
        print(text_to_print)
        sleep(3)
        send_greeting('start')

# Console run mode
def console_mode():
    while True:
        try:
            inp = input('    ║ File path: ')

            if inp == 'exit' or inp == 'quit' or inp == 'x' or inp == 'q':
                send_greeting('quickexit')
                quit()

            elif inp == 'help' or inp == 'h':
                send_greeting('help')

            elif inp == 'options' or inp == 'opt':
                options_main_menu()

            else:
                try:
                    generate_report(inp)
                except FileNotFoundError:
                    print('    ║ File not found! Example usage: file.txt or folder/file.txt')

        except KeyboardInterrupt:
            send_greeting('quickexit')
            quit()

def window_mode():
    main_window = tk.Tk()

    main_window.title('Bookbot')

    def open_file_dialog(): 
        from tkinter import filedialog
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            report_output.delete(1.0, tk.END)
            report_output.insert(1.0, generate_report(file_path, True))

    open_button = tk.Button(main_window, text="Open File", command=open_file_dialog)
    open_button.pack(pady=10)

    report_output = tk.Text(main_window)
    report_output.insert(1.0, 'Waiting for file...')
    report_output.pack()

    tk.Button(main_window, text = 'Quit', command = quit).pack(pady=10)

    tk.Label(text = f'Bookbot version {version}').pack(pady=10)

    main_window.mainloop()
# Main
def main():
    send_greeting("select-modal")
    while True:
        try:
            try:
                option = get_file('default_run_mode')
                if option == '1':
                    send_greeting('start')
                    console_mode()
                elif option == '2':
                    send_greeting('window-running') 
                    window_mode()
                    quit()
            except FileNotFoundError:
                create_file_write('default_run_mode')

            inp = input('    ║ ')
            if inp == '1':
                send_greeting('start')
                console_mode()
            elif inp == '2':
                send_greeting('window-running') 
                window_mode()
                quit()
            elif inp == 'exit' or inp == 'quit' or inp == 'x' or inp == 'q':
                send_greeting('quickexit')
                quit()
        except KeyboardInterrupt:
            send_greeting('quickexit')
            quit()
    
if __name__ == '__main__':
    main()