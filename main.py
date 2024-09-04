import os
import readline # input optimizer

import uuid

from func.sendGreeting import *
from func.converts import *
from func.fileManagement import *
from func.readOptions import *
from func.countChars import *
from func.countWords import *
from optionsMainMenu import *

def generateReport(path):

    getFile(path) # file-exists check

    currentOptions = readOptions() # Import options

    textToPrint = '\n'
    textToPrint += f'======== REPORT for {path[path.rindex("/") + 1:]} ========\n'
    textToPrint += '\n'
    textToPrint += f'    * Word count: {countWords(getFile(path))}\n'
    textToPrint += '\n'
    textToPrint += '    * Character counts:\n'

    # Charcount (+ check for reportAllCharacters option)
    if bool(int(currentOptions[5])):
        for dict in convertToSortedList(countChars(getFile(path))):
            if dict['char'] == '\n':
                pass
            elif dict['char'] == ' ':
                textToPrint += (f'       > [space] was found {dict["count"]} times\n')
            else:
                textToPrint += (f'       > {dict["char"]} was found {dict["count"]} times\n')
    else:
        for dict in convertToSortedList(countChars(getFile(path))):
            if dict['char'].isalpha():
                textToPrint += (f'       > {dict["char"]} was found {dict["count"]} times\n')
            elif dict['char'] == ' ':
                pass

    textToPrint += '\n'
    textToPrint += '=================================='

    print(textToPrint)

    # Check save first to optimize time
    if bool(int(currentOptions[3])):
        createReportFile(f'{uuid.uuid4()}-{path[path.rindex("/") + 1:]}', textToPrint)

    if bool(int(currentOptions[1])):
        sendGreeting('quickexit')
        quit()
    
    # Refresh main menu
    sleep(3)
    sendGreeting("start")
        
# Main
def main():
    os.system('clear')
    sendGreeting("start")

    while True:
        try:
            inp = input('    ║ File path: ')

            if inp == 'exit' or inp == 'quit' or inp == 'x' or inp == 'q':
                os.system('clear')
                sendGreeting('quickexit')
                quit()

            elif inp == 'help' or inp == 'h':
                sendGreeting('help')

            elif inp == 'options' or inp == 'opt':
                optionsMainMenu()

            else:
                try:
                    generateReport(inp)
                except FileNotFoundError:
                    print("")
                    print("File not found! Example usage: file.txt or folder/file.txt")

        except KeyboardInterrupt:
            os.system('clear')
            sendGreeting('quickexit')
            quit()
    
main()