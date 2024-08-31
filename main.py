import os
from func.sendGreeting import *
from func.convertToSortedList import *
from func.getFile import *
from func.countChars import *
from func.countWords import *

def generateReport(path):
    print(f"======== REPORT for {path} ========")
    print("")
    print(f"    * Word count: {countWords(getFile(path))}")
    print("")
    print("    * Character counts:")

    for dict in convertToSortedList(countChars(getFile(path))):
        if dict['char'].isalpha():
            print(f"       > {dict['char']} was found {dict['count']} times")
    print("==================================================")
        
# Main (WIP)
def main():
    os.system('clear')
    sendGreeting("start")

    while True:
        inp = input()
        
        try:
            generateReport(inp)
        except FileNotFoundError:
            print("File not found! Example usage: file.txt or folder/file.txt")
            sleep(3)
            os.system('clear')
            sendGreeting("start")
    
main()