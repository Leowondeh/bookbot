from time import sleep
import platform, os

def send_greeting(type):
    # start
    if type == "start":
        from main import version
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"""
    ╔═══════════════════════╗
    ║    Bookbot! v{version}    ║
    ║                       ║
    ║ Please provide a path ║
    ║ or use 'exit' to exit ║
    ╠═══════════════════════╝
    ║""")

    # exit (unused, use if need to save)
    elif type == "exit5":
        os.system('cls' if platform.system() == 'Windows' else 'clear')
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
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print("""
    ╔═══════════════════════╗
    ║        Bookbot!       ║
    ║                       ║
    ║       Exiting...      ║
    ║        Goodbye!       ║
    ╚═══════════════════════╝""")
    elif type == 'select-modal':
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print("""    
    ╔══════════════════════════════════╗
    ║             Bookbot              ║
    ║      Select operation mode       ║
    ║                                  ║
    ║ The default_run_mode file also   ║
    ║   works to choose this option!   ║
    ║   1 - Console   ║   2 - Window   ║
    ╠══════════════════════════════════╝""")
    elif type == 'window-running':
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print("""    
    ╔══════════════════════════════════╗
    ║             Bookbot              ║
    ║    Is running in window mode     ║
    ║ Swap to the new window to use it ║
    ╚══════════════════════════════════╝""")
    elif type == 'help':
         os.system('cls' if platform.system() == 'Windows' else 'clear')
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
                    send_greeting('start')
                    break
                else:
                     send_greeting('help')

    # options
    elif type == 'options':
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(
"""    ║
    ║                       Options                       
    ║
    ║ Changes are saved after exiting! (use rt/return)
    ║ If options are missing or not working correctly
    ║ try using 'reset' to reset options to default.
    ║
    ║ Type option name to toggle:
    ║                                                     """)
    # else it's an error
    else:
        raise TypeError