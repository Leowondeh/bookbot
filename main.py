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
    textToPrint = f'======== REPORT for {path[path.rindex("/") + 1:]} ========\n'
    textToPrint += '\n'
    textToPrint += f'    * Word count: {countWords(getFile(path))}\n'
    textToPrint += '\n'
    textToPrint += '    * Character counts:\n'

    # Charcount 
    for dict in convertToSortedList(countChars(getFile(path))):
        if dict['char'].isalpha():
          textToPrint += (f'       > {dict["char"]} was found {dict["count"]} times\n')

    textToPrint += '\n'
    textToPrint += '==================================================\n'

    print(textToPrint)

    currentOptions = readOptions() # Import options

    # Check save first to optimize time
    if bool(int(currentOptions[3])) == True:
        createReportFile(f'{uuid.uuid4()}-{path[path.rindex("/") + 1:]}', textToPrint)

    if bool(int(currentOptions[1])) == True:
        sendGreeting('quickexit')
        quit()
    
    # Refresh main menu
    sleep(3)
    print("")
    sendGreeting("start")
        
# Main (WIP)
def main():
    os.system('clear')
    sendGreeting("start")

    while True:
        try:
            inp = input()

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