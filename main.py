import os
import platform

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

# Generate report
def generate_report(path):
    get_file(path) # file-exists check

    current_options = read_options() # Import options
    try:
        text_to_print = f'======== REPORT for {path[path.rindex("/") + 1:]} ========\n'
    except ValueError:
        text_to_print = f'======== REPORT for {path} ========\n'
    text_to_print += '\n'
    text_to_print += f'    * Word count: {count_words(get_file(path))}\n'
    text_to_print += '\n'
    text_to_print += '    * Character counts:\n'

    # Charcount and check for options
    if bool(int(current_options[5])):
        for dict in convert_to_sorted_list(count_chars(get_file(path))):
            if dict['char'] == '\n':
                pass
            elif dict['char'] == ' ':
                text_to_print += (f'       > [space] was found {dict["count"]} times\n')
            else:
                text_to_print += (f'       > {dict["char"]} was found {dict["count"]} times\n')
    else:
        for dict in convert_to_sorted_list(count_chars(get_file(path))):
            if dict['char'].isalpha():
                text_to_print += (f'       > {dict["char"]} was found {dict["count"]} times\n')
            elif dict['char'] == ' ':
                pass # Exclude spaces

    text_to_print += '\n'
    text_to_print += f'    * Vowel count: {count_vowels_and_consonants(get_file(path))[0]}\n'
    text_to_print += f'    * Consonant count: {count_vowels_and_consonants(get_file(path))[1]}'
    text_to_print += '\n'
    text_to_print += '=================================='

    print(text_to_print)

    # Check save first to optimize time
    if bool(int(current_options[3])):
        create_report_file(f'{uuid.uuid4()}-{path[path.rindex("/") + 1:]}', text_to_print)
        # File format: (random uuid)-(filename).txt

    if bool(int(current_options[1])):
        send_greeting('quickexit')
        quit()
    
    # Refresh main menu
    sleep(3)
    send_greeting("start")
        
# Main
def main():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    send_greeting("start")

    while True:
        try:
            inp = input('    ║ File path: ')

            if inp == 'exit' or inp == 'quit' or inp == 'x' or inp == 'q':
                os.system('cls' if platform.system() == 'Windows' else 'clear')
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
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            send_greeting('quickexit')
            quit()
    
if __name__ == '__main__':
    main()