from time import sleep

def sendGreeting(type):
    # START
    if type == "start":
        print("""
    ╔═══════════════════════╗
    ║        Bookbot!       ║
    ║                       ║
    ║ Please provide a path ║
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
    # ERROR handle
    else:
        print("Error, invalid greeting type!")