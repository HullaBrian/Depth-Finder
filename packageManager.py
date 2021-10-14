import os
try:
    print("Verifying required libraries...", end="")
    import art  # Tries to import
    print("Done!")
except ModuleNotFoundError:
    print("Could not find required library.")
    print("Installing required libraries...")
    os.system("pip install -U art")  # Installs art if not already installed
    print("Done!")
    print("Restart PhishDetective")
    exit()  # we need to exit here or the code will die anyway
