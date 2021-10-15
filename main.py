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
from commands import *

art.tprint("Phishing-Detective") #we can discuss fonts later, I say we get some of the primary code done before


def main():
    # To add a command, simply add a command(command title, required titles) object to commands
    commandlst = []
    commandlst.append(setHost())
    commandlst.append(hlp(commandlst))  # Put the help addition at the end of adding commands to properly generate the help command

    while True:  # Loops until exits
        prompt = "pd> "
        print(prompt, end="")

        command = input().split(" ")
        if len(command) >= 3:
            cmd = command[0]
            subcmd = command[1]
            arg = command[2]
            params = [cmd, subcmd, arg]
        elif len(command) >= 2:
            cmd = command[0]
            subcmd = command[1]
            params = [cmd, subcmd]
        elif len(command) >= 1:
            cmd = command[0]
            params = [cmd]

        if cmd == "exit":
            exit()
            break
        executedCommand = False
        for command in commandlst:
            if command.matchesParams(params):
                command.execute(params[-1])
                executedCommand = True
        if not executedCommand:
            print("Invalid command")


main()
