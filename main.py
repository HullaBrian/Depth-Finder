command = ""


def help():
    print("set url <url>")
    print("set host <host url>")


def interpritCommand(command):
    if command == "help":
        help()


while command != "q":
    command = input("msf>")
    interpritCommand(command)