import packageManager  # makes sure all necessary packages are installed

import art

art.tprint("Phishing-Detective")


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
