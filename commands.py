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