import datetime

import packageManager  # makes sure all necessary packages are installed
import socket
import urllib3.exceptions
from command import command
import art

global url
global commands


class hlp(command):
    def __init__(self):
        super().__init__("help", ["help"])

    def execute(self, filler):
        print("\nhelp   Displays this menu")
        print("\"Set\" Commands")
        for x in range(len("\"Set\" Commands")):
            print("-", end="")
        print()

        print("\tCommand", end="")
        maxCommandNameLength = 0
        for command in commands:
            if len(command.title) > maxCommandNameLength:
                maxCommandNameLength = len(command.title)
        if maxCommandNameLength >= len("Command"):
            for x in range(maxCommandNameLength - len("Command") + 3):
                print(" ", end="")
        else:
            for x in range(len("Command") + 3):
                print(" ", end="")

        print("Description")

        print("\t", end="")
        for x in range(len("Command")):
            print("-", end="")
        if maxCommandNameLength >= len("Command"):
            for x in range(maxCommandNameLength - len("Command") + 3):
                print(" ", end="")
        else:
            for x in range(len("Command") + 3):
                print(" ", end="")
        for x in range(len("Description")):
            print("-", end="")
        print()

        setCommands = []
        for command in commands:
            if command.requiredCommands[0] == "set":
                setCommands.append(command)
        for command in setCommands:
            print("\t" + str(command.title), end="")
            for x in range(max(maxCommandNameLength, len("Command")) - len(command.title) + 3):
                print(" ", end="")
            print(str(command.hlp))

        # Section seperator

        print("\n\"Get\" Commands")
        for x in range(len("\"Get\" Commands")):
            print("-", end="")
        print()

        print("\tCommand", end="")
        maxCommandNameLength = 0
        for command in commands:
            if len(command.title) > maxCommandNameLength:
                maxCommandNameLength = len(command.title)
        if maxCommandNameLength >= len("Command"):
            for x in range(maxCommandNameLength - len("Command") + 3):
                print(" ", end="")
        else:
            for x in range(len("Command") + 3):
                print(" ", end="")

        print("Description")

        print("\t", end="")
        for x in range(len("Command")):
            print("-", end="")
        if maxCommandNameLength >= len("Command"):
            for x in range(maxCommandNameLength - len("Command") + 3):
                print(" ", end="")
        else:
            for x in range(len("Command") + 3):
                print(" ", end="")
        for x in range(len("Description")):
            print("-", end="")
        print()

        setCommands = []
        for command in commands:
            if command.requiredCommands[0] == "get":
                setCommands.append(command)
        for command in setCommands:
            print("\t" + str(command.title), end="")
            for x in range(max(maxCommandNameLength, len("Command")) - len(command.title) + 3):
                print(" ", end="")
            print(str(command.hlp))


class setUrl(command):
    def __init__(self):
        super(setUrl, self).__init__("set url", ["set", "url"], True, hlp="sets the url to a given url")
        self.hlp = "sets the url to a given url"

    def execute(self, data):
        global url
        url = data
        print(" ")
        print("url ==> " + url)
        print(" ")


class getInfo(command):
    def __init__(self):
        super().__init__("get info", ["get", "info"], hlp="gets the relevant information on a given url")
        self.hlp = "give the relevant information on a given url"
        self.info = []
        self.expirationDate = 0

    def execute(self, filler):
        import whois
        try:
            whois_info = whois.whois(url)
        except Exception:
            print("Invalid url")
            return
        self.info.append(bool(whois_info.domain_name))
        self.info.append(whois_info.registrar)
        self.info.append(whois_info.whois_server)
        self.info.append(whois_info.creation_date)
        self.info.append(whois_info)

        print("Registered: " + str(self.info[0]))
        print("Registrar: " + str(self.info[1]))
        print("Server: " + str(self.info[2]))
        print("Creation date: " + str(self.info[3]))
        print("Other info: " + str(self.info[4]))

        self.expirationDate = whois_info.expiration_date


class sslverify(command):
    def __init__(self):
        super().__init__("get sslverify", ["get", "sslverify"], hlp="verifies the SSL certificate of the url")
        self.hlp = "verifies the SSL certificate of the url"

    def execute(self, filler):
        import socket
        import ssl
        try:
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname=url) as s:
                s.connect((url, 443))
            print(url + " has a VALID SSL certificate")
        except Exception as e:
            print(url + " has an INVALID SSL certificate, error:", e)


def main():
    art.tprint("Phishing-Detective")  # we can discuss fonts later, I say we get some of the primary code done before
    # To add a command, simply add a command(command title, required titles) object to commands
    global commands
    commands = []
    commands.append(setUrl())
    commands.append(getInfo())
    commands.append(sslverify())
    commands.append(hlp())  # Put the help addition at the end of adding commands to properly generate the help command

    while True:  # Loops until exits
        prompt = "pd> "
        print(prompt, end="")

        command = input().lower().split(" ")
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
        if len(params) == 1:
            if params[0] == "url":
                try:
                    print("Current url is \"" + url + "\"")
                except NameError:
                    print("No url is set")
                executedCommand = True
        for command in commands:
            if command.matchesParams(params):
                command.execute(params[-1])
                executedCommand = True
        if not executedCommand:
            print("Invalid command")


main()
