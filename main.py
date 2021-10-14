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


def main():

    prompt = "pd> "
    i = input(prompt)

    if i == "help" or i == "?":
        print(" ")
        print("Commands")
        print("=============")
        print("\"help\" or \"?\" ---- prints this help menu")
        print(" ")
        main()

    if i == "exit":
        exit()

main()
