from time import sleep
import os

def sendGreeting(type):
    # START
    if type == "start":
        print("""
    ╔═══════════════════════╗
    ║        Bookbot!       ║
    ║                       ║
    ║ Please provide a path ║
    ║ or use 'exit' to exit ║
    ╚═══════════════════════╝
          """)
    # EXIT
    elif type == "exit":
        for i in range(3, 0, -1):
            print(f"""
    ╔═══════════════════════╗
    ║        Bookbot        ║
    ║     is exiting...     ║
    ║           {i}           ║
    ╚═══════════════════════╝
          """)
            sleep(1)
            os.system('clear')
    
    elif type == "options":
            print(f"""
    ╔═════════════════════════════════════════════════════╗
    ║                       Options                       ║
    ║                                                     ║
    ║ Type option name (the one in parantheses) to toggle ║
    ║                                                     ║
    ╚═════════════════════════════════════════════════════╝
          """)
    # ERROR handle
    else:
        print("Error, invalid greeting type!")