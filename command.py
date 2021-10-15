

class command(object):  # To make a command a child of this, use class <command name>(command):
    """
    An object that simplifies the command making progress
    """
    def __init__(self, title, requiredCommands, hlp=""):
        self.title = title
        self.requiredCommands = requiredCommands
        self.help = hlp

    def matchesParams(self, params):
        """
        A method for validating that the parameters given match the required parameters
        """
        count = 0
        if len(params) >= len(self.requiredCommands):
            for x in range(len(self.requiredCommands)):
                if self.requiredCommands[x] == params[x]:
                    count += 1
        if count == len(self.requiredCommands):
            return True
        return False

    def execute(self, data):
        pass
