import subprocess
import sys
import os

if sys.platform.startswith('linux'):
    Linux = True
    missingLibrary = False
    print("Verifying required libraries...")
    try:
        import art
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python3", "-m", "pip", "install", "-U", "art", "-q"])
        print("Done!")
    try:
        import whois
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python3", "-m", "pip", "install", "-U", "python-whois", "-q"])
        print("Done!")
    try:
        import requests
        subprocess.run(["python3", "-m", "pip", "install", "-U", "requests[socks]", "-q"])
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python3", "-m", "pip", "install", "-U", "requests", "-q"])
        print("Done!")
    try:
        import chromedriver_autoinstaller
        chromedriver_autoinstaller.install()
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python3", "-m", "pip", "install", "-U", "chromedriver-autoinstaller", "-q"])
        print("Done!")
    try:
        import selenium
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python3", "-m", "pip", "install", "-U", "selenium", "-q"])
        print("Done!")

    if missingLibrary:
        print("Restarting to refresh content...")
        import main
        exit()
if Linux != True:
    missingLibrary = False
    print("Verifying required libraries...")
    try:
        import art
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python", "-m", "pip", "install", "-U", "art", "-q"])
        print("Done!")
    try:
        import whois
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python", "-m", "pip", "install", "-U", "python-whois", "-q"])
        print("Done!")
    try:
        import requests
        subprocess.run(["python", "-m", "pip", "install", "-U", "requests[socks]", "-q"])
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python", "-m", "pip", "install", "-U", "requests", "-q"])
        print("Done!")
    try:
        import chromedriver_autoinstaller
        chromedriver_autoinstaller.install()
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python", "-m", "pip", "install", "-U", "chromedriver-autoinstaller", "-q"])
        print("Done!")
    try:
        import selenium
    except ModuleNotFoundError:
        missingLibrary = True
        print("Could not find a required library. Installing...", end="")
        subprocess.run(["python", "-m", "pip", "install", "-U", "selenium", "-q"])
        print("Done!")

    if missingLibrary:
        print("Restarting to refresh content...")
        import main
        exit()

