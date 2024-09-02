from time import sleep
import os

def sendGreeting(type):
    # start
    if type == "start":
        print("""
    ╔═══════════════════════╗
    ║        Bookbot!       ║
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

    # options
    elif type == "options":
            print(
f"""    ║
    ║                       Options                       
    ║
    ║ Changes are saved after exiting! (use rt/return)                                  
    ║ Type option name to toggle:
    ║                                                     """)
    # else it's an error
    else:
        raise TypeError