import os


missingLibrary = False
print("Verifying required libraries...", end="")
try:
    import art  # Tries to import
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...")
    os.system("pip install -U art")
    print("Done!")
try:
    import whois
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...")
    os.system("pip install -U python-whois")
    print("Done!")
try:
    import requests
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...")
    os.system("pip install -U requests")
    print("Done!")

if missingLibrary:
    print("Restarting to refresh content...")
    import main
    exit()