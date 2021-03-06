import subprocess
import sys

if sys.platform.startswith('linux'):
    Linux = True
    mod = "3"
else:
    Linux = False
    mod = ""

missingLibrary = False
print("Verifying required libraries...", end="")
try:
    import art
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    subprocess.run([("python" + mod), "-m", "pip", "install", "-U", "art", "-q"])
    print("Done!")
try:
    import distro
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    subprocess.run([("python" + mod), "-m", "pip", "install", "-U", "distro", "-q"])
    print("Done!")
try:
    import whois
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    subprocess.run([("python" + mod), "-m", "pip", "install", "-U", "python-whois", "-q"])
    print("Done!")
try:
    import requests
    subprocess.run([("python" + mod), "-m", "pip", "install", "-U", "requests[socks]", "-q"])
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    subprocess.run([("python" + mod), "-m", "pip", "install", "-U", "requests", "-q"])
    print("Done!")
try:
    import chromedriver_autoinstaller
    chromedriver_autoinstaller.install()
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    subprocess.run([("python" + mod), "-m", "pip", "install", "-U", "chromedriver-autoinstaller", "-q"])
    print("Done!")
try:
    import selenium
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    subprocess.run([("python" + mod), "-m", "pip", "install", "-U", "selenium", "-q"])
    print("Done!")
try:
    from sh3ll import IS
except ModuleNotFoundError:
    missingLibrary = True
    print("Could not find a required library. Installing...", end="")
    subprocess.run([("python" + mod), "-m", "pip", "install", "-U", "sh3ll", "-q"])
    print("Done!")

if not missingLibrary:
    print("Done!")
