import os
try:
    print("Verifying required libraries...", end="")
    import art  # Tries to import
    print("Done!")
except ModuleNotFoundError:
    click.echo("Could not find required library.")
    click.echo("Installing required libraries...", nl=False)
    os.system("pip install -U art")  # Installs click if not already installed
    click.echo("Done!")
