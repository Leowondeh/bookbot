import os, platform
from func.send_greeting import *
from func.file_management import *
from func.read_options import *

def save_settings(current_options):
    settings_export = ""
    for i in range(0, len(current_options)):
        settings_export += current_options[i]['option'] + ", " + str(current_options[i]['value']) + ", "
    with open('options', 'w') as f:
        f.write(settings_export[:-2]) # except last 2 chars for ", "

# Create (or reset) options list
def create_or_reset_options():
    create_file_write('options', 
"exit after finishing report, 0, save to file, 0, report more characters, 0, display vowel count, 1, display consonant count, 1")

def options_main_menu():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    send_greeting('options')

    # Read options file & print options
    try:
        open('options') # Exist-check to jump into except
    except FileNotFoundError:
        create_or_reset_options()
        
    current_options = read_options()
    temp_options = []
    for i in range(0, len(current_options), 2):
        temp_options.append({'option': current_options[i], 'value': int(current_options[i+1])})
    current_options = temp_options
    
    for item in current_options:
        print(f"    ║ {item['option']} = {bool(item['value'])}")
    print('    ║')
    
    save_settings(current_options)

    # Input loop
    while True:
        inp = input('    ║ Select option: ')
        
        # Return to main
        if inp == 'return' or inp == 'rt' or inp == 'q' or inp == 'x':
            save_settings(current_options)
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            send_greeting('start')
            break
        
        # Options reset
        elif inp == 'reset':
            create_or_reset_options()
            print('    ║ Resetting options... please wait.')
            sleep(2)
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            send_greeting('start')
            break
            
        
        # Otherwise scan for value
        else:
            found = False
            for item in current_options:
                   if inp == item['option']:
                    item['value'] = int(not bool(item['value']))
                    found = True
                    print(f'    ║ Value of {item["option"]} changed to {bool(item["value"])}')
            if not found:
                print('    ║Option not found, try again!')