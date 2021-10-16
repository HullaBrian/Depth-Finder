import packageManager  # makes sure all necessary packages are installed
import socket
import urllib3.exceptions
from command import command
import art

global hostname
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


class setHost(command):
    def __init__(self):
        super().__init__("set host", ["set", "host"], True, hlp="Sets the hostname to a given url")
        self.hlp = "Sets the hostname to a given url"

    def execute(self, name):
        global hostname
        hostname = name
        print(" ")
        print("hostname ==> " + hostname)
        print(" ")


class setUrl(command):
    def __init__(self):
        super(setUrl, self).__init__("set url", ["set", "url"], True, hlp="sets the url to a given url")
        self.hlp = "sets the url to a given url"

    def execute(self, data):
        global url
        url = data
        print(" ")
        print("url ==>" + url)
        print(" ")


class getInfo(command):
    def __init__(self):
        super().__init__("get info", ["get", "info"], hlp="gets the relevant information on a given hostname")
        self.hlp = "give the relevant information on a given hostname"

    def execute(self, filler):
        info = []
        import whois
        try:
            whois_info = whois.whois(hostname)
        except Exception:
            print("Invalid domain")
            return
        info.append(bool(whois_info.domain_name))
        info.append(whois_info.registrar)
        info.append(whois_info.whois_server)
        info.append(whois_info.creation_date)
        info.append(whois_info)

        print("Registered: " + str(info[0]))
        print("Registrar: " + str(info[1]))
        print("Server: " + str(info[2]))
        print("Creation date: " + str(info[3]))
        print("Other info: " + str(info[4]))


class sslverify(command):
    def __init__(self):
        super().__init__("get sslverify", ["get", "sslverify"], hlp="verifies the SSL certificate of the hostname")
        self.hlp = "verifies the SSL certificate of the hostname"

    def execute(self, filler):
        import requests
        try:
            response = str(requests.get(url))
            if "SSL: CERTIFICATE_VERIFY_FAILED" in response:
                print("url \"" + url + "\" has an invalid SSL certificate")
            else:
                print("url \"" + url + "\" has a valid SSL certificate")
        except requests.exceptions.InvalidURL:
            print("Invalid url \"" + url + "\"")
        except (socket.gaierror, urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError):
            print("Could not resolve url \"" + url + "\" to host")


def main():
    art.tprint("Phishing-Detective")  # we can discuss fonts later, I say we get some of the primary code done before
    # To add a command, simply add a command(command title, required titles) object to commands
    global commands
    commands = []
    commands.append(setHost())
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
            if params[0] == "hostname":
                try:
                    print("Current host name is \"" + hostname + "\"")
                except NameError:
                    print("No host name is set")
                executedCommand = True
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
