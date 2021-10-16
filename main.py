from command import command


global hostname
global commands


class hlp(command):
    def __init__(self):
        super().__init__("help", ["help"])

    def execute(self, filler):
        print(" ")
        print("Commands")
        print("=============")
        print("\"help\" or \"?\" ---- prints help menu")
        for command in commands[0:-1]:
            print(f"\"{command.title} [", end="")
            for param in command.requiredCommands[:-1]:
                print(param + ", ", end="")
            print(command.requiredCommands[-1] + "] ---- " + str(command.hlp))
        print(" ")


class setHost(command):
    def __init__(self):
        super().__init__("set host", ["set", "host"], hlp="Sets the hostname to a given url")
        self.hlp = "Sets the hostname to a given url"

    def execute(self, name):
        global hostname
        hostname = name
        print("Set host name to " + hostname)


class isDomainRegistered(command):
    def __init__(self):
        super().__init__("isDomainRegistered", ["isDomainRegistered"], hlp="Checks if the current domain name set is a valid, registered domain")
        self.hlp = "Checks if the current domain name set is a valid, registered domain"

    def execute(self, filler):
        if hostname == "" or hostname == "isDomainRegistered":
            print("Missing required parameter \"hostname\"")
            return
        import whois
        print("Verifying domain...", end="")
        try:
            if whois.whois(hostname).domain_name:
                print("Done!\nDomain " + hostname + " is registered.")
            else:
                print("Done!\nDomain " + hostname + " is not registered.")
        except Exception:
            print("ERROR! Domain is not valid!")
            return


class getDomainInfo(command):
    def __init__(self):
        super().__init__("getDomainInfo", ["getDomainInfo"], hlp="give the relevant information on a given hostname")
        self.hlp = "give the relevant information on a given hostname"

    def execute(self, hostName):
        info = []
        import whois
        try:
            whois_info = whois.whois(hostName)
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


import packageManager  # makes sure all necessary packages are installed
import art

art.tprint("Phishing-Detective")  # we can discuss fonts later, I say we get some of the primary code done before


def main():
    # To add a command, simply add a command(command title, required titles) object to commands
    global commands
    commands = []
    commands.append(setHost())
    commands.append(isDomainRegistered())
    commands.append(getDomainInfo())
    commands.append(hlp())  # Put the help addition at the end of adding commands to properly generate the help command

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
        if len(params) == 1:
            if params[0] == "hostname":
                try:
                    print("Current host name is \"" + hostname + "\"")
                except NameError:
                    print("No host name is set")
                executedCommand = True
        for command in commands:
            if command.matchesParams(params):
                command.execute(params[-1])
                executedCommand = True
        if not executedCommand:
            print("Invalid command")


main()
