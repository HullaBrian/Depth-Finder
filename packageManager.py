import os


missingLibrary = False
print("Verifying required libraries...")
try:
    import art  # Tries to import
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    os.system("python -m pip install -U art -q")
    print("Done!")
try:
    import whois
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    os.system("python -m pip install -U python-whois -q")
    print("Done!")
try:
    import requests
    os.system("python -m pip install -U requests[socks] -q")
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    os.system("python -m pip install -U requests -q")
    print("Done!")
try:
    import chromedriver_autoinstaller
    chromedriver_autoinstaller.install()
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    os.system("python -m pip install -U chromedriver-autoinstaller -q")
    print("Done!")
try:
    import selenium
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    os.system("python -m pip install -U selenium -q")
    print("Done!")

if missingLibrary:
    print("Restarting to refresh content...")
    import main
    exit()
