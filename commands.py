from command import command


class hlp(command):
    def __init__(self, commands):
        super().__init__("help", ["help"])
        self.commands = commands

    def execute(self, filler):
        print(" ")
        print("Commands")
        print("=============")
        print("\"help\" or \"?\" ---- prints help menu")
        self.commands.remove(self)
        for command in self.commands:
            print(f"\"{command.title} [", end="")
            for param in command.requiredCommands[:-1]:
                print(param + ", ", end="")
            print(command.requiredCommands[-1] + "] ---- " + str(command.hlp))
        print(" ")


class setHost(command):
    def __init__(self):
        super().__init__("set host", ["set", "host"], hlp="Sets the hostname to a given url")
        self.hostName = ""
        self.hlp = "Sets the hostname to a given url"

    def execute(self, name):
        self.hostName = name
        print("Set host name to " + self.hostName)


class isDomainRegistered(command):
    def __init__(self):
        super().__init__("isDomainRegistered", ["isDomainRegistered"], hlp="Checks if the current domain name set is a valid, registered domain")
        self.hlp = "Checks if the current domain name set is a valid, registered domain"

    def execute(self, hostName):
        if hostName == "" or hostName == "isDomainRegistered":
            print("Missing required parameter \"hostname\"")
            return
        import whois
        print("Verifying domain...", end="")
        try:
            if whois.whois(hostName).domain_name:
                print("Done!\nDomain " + hostName + " is registered.")
            else:
                print("Done!\nDomain " + hostName + " is not registered.")
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
