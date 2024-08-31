import os
from func.sendGreeting import *
from func.convertToSortedList import *
from func.getFile import *
from func.countChars import *
from func.countWords import *
from func.options.optionsMainMenu import *

def generateReport(path):

    countWords(getFile(path)) # file-exists check
    print("")
    print(f"======== REPORT for {path} ========")
    print("")
    print(f"    * Word count: {countWords(getFile(path))}")
    print("")
    print("    * Character counts:")

    # Char counts (only alphabet)
    for dict in convertToSortedList(countChars(getFile(path))):
        if dict['char'].isalpha():
          print(f"       > {dict['char']} was found {dict['count']} times")

    print("")
    print("==================================================")
    sleep(3)
    print("")
    sendGreeting("start")
        
# Main (WIP)
def main():
    os.system('clear')
    sendGreeting("start")

    while True:
        inp = input()

        if inp == 'exit':
            os.system('clear')
            sendGreeting('exit')
            quit()
        elif inp == 'options':
            optionsMainMenu()
        else:
            try:
                generateReport(inp)
            except FileNotFoundError:
                print("")
                print("File not found! Example usage: file.txt or folder/file.txt")
                sleep(3)
                os.system('clear')
                sendGreeting("start")
    
main()