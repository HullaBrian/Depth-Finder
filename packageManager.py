import os


missingLibrary = False
print("Verifying required libraries...")
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
    os.system("pip install -U requests[socks]")
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...")
    os.system("pip install -U requests")
    print("Done!")
try:
    import chromedriver_autoinstaller
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...")
    os.system("pip install -U chromedriver-autoinstaller")
    print("Done!")
try:
    import selenium
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...")
    os.system("pip install -U selenium")
    print("Done!")

if missingLibrary:
    print("Restarting to refresh content...")
    import main
    exit()
