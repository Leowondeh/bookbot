from time import sleep
import os
from func.fileManagement import getVersion

def sendGreeting(type):
    # start
    if type == "start":
        print(f"""
    ╔═══════════════════════╗
    ║    Bookbot! v{getVersion()}   ║
    ║                       ║
    ║ Please provide a path ║
    ║ or use 'exit' to exit ║
    ╚═══════════════════════╝
          """)

    # exit (unused, use if need to save)
    elif type == "exit5":
        for i in range(5, 0, -1):
            print(f"""
    ╔═══════════════════════╗
    ║        Bookbot        ║
    ║     is exiting...     ║
    ║           {i}           ║
    ╚═══════════════════════╝
          """)
            sleep(1)

    # quick exit
    elif type == 'quickexit':
        print("""
    ╔═══════════════════════╗
    ║        Bookbot!       ║
    ║                       ║
    ║       Exiting...      ║
    ║        Goodbye!       ║
    ╚═══════════════════════╝
          """)
    elif type == 'help':
         os.system('clear')
         print("""    
    ╔══════════════════════════════════╗
    ║                Help              ║
    ║                                  ║
    ║ command(shortcuts) - use         ║
    ║                                  ║
    ║ help(h) - displays this menu     ║
    ║ quit(exit, q, x) - quit Bookbot  ║
    ║ options(opt) - display options   ║
    ║                                  ║
    ║    Use return(rt) to go back     ║
    ╚══════════════════════════════════╝
""")
         while True:
                inp = input()
                if inp == 'return' or inp == 'rt' or inp == 'q' or inp == 'x':
                    os.system('clear')
                    sendGreeting('start')
                    break
                else:
                     os.system('clear')
                     sendGreeting('help')

    # options
    elif type == 'options':
            print(
"""    ║
    ║                       Options                       
    ║
    ║ Changes are saved after exiting! (use rt/return)                                  
    ║ Type option name to toggle:
    ║                                                     """)
    # else it's an error
    else:
        raise TypeError