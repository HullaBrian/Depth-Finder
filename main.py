'''
note: create a new function for every new functionallity/feature, then tie it in to the main function with an if statement.
make sure you end off every new function with a redirect to the main function

EX:

def new_feature():
    code code code code
    
    main()

def main():

    prompt = "pd> "
    ex = input(prompt)
    if ex == "ex":
        print(" ")
        new_feature()
        
main()
'''


import packageManager  # makes sure all necessary packages are installed
import art

art.tprint("Phishing-Detective") #we can discuss fonts later, I say we get some of the primary code done before


def help():
    print(" ")
    print("Commands")
    print("=============")
    print("\"help\" or \"?\" ---- prints this help menu")
    print("\"set target [URL]\" ---- sets target URL for data gathering")
    print(" ")
    main()


def main():
    prompt = "pd> "
    print(prompt, end="")

    command = input().split(" ")
    if len(command) >= 3:
        cmd = command[0]
        subcmd = command[1]
        arg = command[2]
    elif len(command) >= 2:
        cmd = command[0]
        subcmd = command[1]
    elif len(command) >= 1:
        cmd = command[0]

    if cmd == "set" and subcmd == "target":
        hostname = arg
        print("hostname ===> "+ arg)

    if cmd == "help" or cmd == "?":
        print("EEE")
        help()

    if cmd == "exit":
        exit()


main()
