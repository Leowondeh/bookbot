import os
from func.sendGreeting import *
from func.fileManagement import *
from func.debugPrint import *

def saveSettings(currentOptions):
    settingsExport = ""
    for i in range(0, len(currentOptions)):
        settingsExport += currentOptions[i]['option'] + ", " + str(currentOptions[i]['value']) + ", "
    with open('options', 'w') as f:
        f.write(settingsExport[:-2])

def optionsMainMenu():
    os.system('clear')
    sendGreeting('options')

    # Read options file & print options
    try:
        open('options') # Exist-check to jump into except
    except FileNotFoundError:
        createFile('options', 
"exitAfterReport, 0, saveToFile, 0") # Hardcoded options list
        
    with open('options') as f:
        currentOptions = f.readline()
        currentOptions = currentOptions.split(", ")
        tempOptions = []
        for i in range(0, len(currentOptions), 2):
            tempOptions.append({'option': currentOptions[i], 'value': int(currentOptions[i+1])})
        currentOptions = tempOptions
    
    for item in currentOptions:
        print(f"    ║ {item['option']} = {item['value']}")
    
    saveSettings(currentOptions)
    while True:
        inp = input()
        
        # Return to main
        if inp == 'return' or inp == 'rt' or inp == 'quit' or inp == 'exit':
            saveSettings(currentOptions)
            os.system('clear')
            sendGreeting('start')
            break
        
        # Otherwise scan for value
        else:
            found = False
            for item in currentOptions:
                   if inp == item['option']:
                    item['value'] = int(not bool(item['value']))
                    found = True
                    print(f'Value of {item["option"]} changed to {item["value"]}')
            if not found:
                print("Option not found, try again!")