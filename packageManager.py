import os
try:
    print("Verifying required libraries...", end="")
    import art  # Tries to import
    import whois
    print("Done!")
except ModuleNotFoundError:
    print("Could not find required library.")
    print("Installing required libraries...")
    os.system("pip install -U art")  # Installs art if not already installed
    os.system("pip install -U python-whois")
    print("Done!")
    import main  # runs main again to avoid having to restart the program
    exit()  # we need to exit here or the code will die anyway
