import packageManager  # makes sure all necessary packages are installed
import click  # imports click libarary


@click.group()
@click.option('--set', default="")
def set(command):
    print("Set received command" + command)
    pass


@set.group()
@click.option("--hostname", default="", help="sets the hostname")
@click.argument("hostname", default="")
def sethostname(hostname):
    click.echo("Set host name to " + hostname)


if __name__ == '__main__':
    set()


"""
Current Error:
    Input: >python main.py --set --hostname https://google.com/
    Error message:
    
        Verifying required libraries...Done!
        Usage: main.py [OPTIONS] COMMAND [ARGS]...
        Try 'main.py --help' for help.
        
        Error: No such command 'https://google.com/'.
        
"""
