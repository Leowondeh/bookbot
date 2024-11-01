import os, platform
from func.sendGreeting import *
from func.fileManagement import *
from func.readOptions import *

def saveSettings(currentOptions):
    settingsExport = ""
    for i in range(0, len(currentOptions)):
        settingsExport += currentOptions[i]['option'] + ", " + str(currentOptions[i]['value']) + ", "
    with open('options', 'w') as f:
        f.write(settingsExport[:-2]) # except last 2 chars for ", "

# Create (or reset) options list
def createOrResetOptions():
    createFileWrite('options', 
"exit after finishing report, 0, save to file, 0, report more characters, 0, display vowel count, 1, display consonant count, 1")

def optionsMainMenu():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    sendGreeting('options')

    # Read options file & print options
    try:
        open('options') # Exist-check to jump into except
    except FileNotFoundError:
        createOrResetOptions()
        
    currentOptions = readOptions()
    tempOptions = []
    for i in range(0, len(currentOptions), 2):
        tempOptions.append({'option': currentOptions[i], 'value': int(currentOptions[i+1])})
    currentOptions = tempOptions
    
    for item in currentOptions:
        print(f"    ║ {item['option']} = {bool(item['value'])}")
    print('    ║')
    
    saveSettings(currentOptions)

    # Input loop
    while True:
        inp = input('    ║ Select option: ')
        
        # Return to main
        if inp == 'return' or inp == 'rt' or inp == 'q' or inp == 'x':
            saveSettings(currentOptions)
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            sendGreeting('start')
            break
        
        # Options reset
        elif inp == 'reset':
            createOrResetOptions()
            print('    ║ Resetting options... please wait.')
            sleep(2)
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            sendGreeting('start')
            break
            
        
        # Otherwise scan for value
        else:
            found = False
            for item in currentOptions:
                   if inp == item['option']:
                    item['value'] = int(not bool(item['value']))
                    found = True
                    print(f'    ║ Value of {item["option"]} changed to {bool(item["value"])}')
            if not found:
                print('    ║Option not found, try again!')