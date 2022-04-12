import os
import sys
import subprocess
import json
import socket
import ssl

if sys.platform.startswith("linux"):
    if "SUDO_UID" in os.environ.keys():
        print("Depth-Finder does not function in sudo!")
        exit()

import selenium.common.exceptions
import urllib3.exceptions
import art
import requests
import whois

from sh3ll import IS

global url, commands, whiteListedPorts, settings

app = IS("df>")


@app.command(name="url", callName="url", aliases=[], help="sets the url to a given url", category="set")
def url(ctx):
    global url
    url = ctx.parameters[0]
    print(f"\nurl ==> {url}\n")


@app.command(name="info", callName="info", aliases=[], help="give the relevant information on a given url", category="get")
def info(ctx):
    info = []
    expirationDate = 0

    try:
        whois_info = whois.whois(url)
    except NameError:
        print("Please set a url.")
        return

    info = []
    info.append(bool(whois_info.domain_name))
    info.append(whois_info.registrar)
    info.append(whois_info.whois_server)
    info.append(whois_info.creation_date)
    info.append(whois_info)

    print("Registered: " + str(info[0]))
    print("Registrar: " + str(info[1]))
    print("Server: " + str(info[2]))
    print("Creation date: " + str(info[3]))
    print("Other info: " + str(info[4]))

    expirationDate = whois_info.expiration_date


@app.command(name="sslverify", callName="sslverify", aliases=["sv"], help="verifies the SSL certificate of the url", category="get")
def sslverify(ctx):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=url) as s:
            s.connect((url, 443))
        print(url + " has a VALID SSL certificate")
    except NameError:
        print("Please set a url.")
        return
    except Exception as e:
        print(url + " has an INVALID SSL certificate, error:", e)


@app.command(name="isRegistered", callName="isRegistered", aliases=["ir", "iR"], help="determines whether or not a domain is registered or not", category="get")
def isRegistered(ctx):
    try:
        whois_info = whois.whois(url)
    except NameError:
        print("Please set a url.")
        return
    except Exception:
        print("Invalid url")
        return
    tmp = bool(whois_info.domain_name)
    if tmp:
        print(url + " is a registered domain under " + whois_info.registrar)
    else:
        print(url + " is not a registered domain")


@app.command(name="port", callName="port", aliases=["p", "P"], help="retrieves the port of the url", category="get")
def getPort(ctx):
    try:
        port = int(url.split(":")[2].split("/")[0])  # Ex. https://google.com:80/ -> ["80/"] -> 80
    except IndexError:
        print("Could not find a port number in " + url)
        return
    except NameError:
        print("Please set a url.")
        return
    print(url + " runs through port", port)

    if port not in whiteListedPorts:
        print("Port detected as suspicious")
    else:
        print("Port detected as a commonly used port number") 


@app.command(name="ScreenShot", callName="ScreenShot", aliases=["SS", "ss"], help="retrieves a screenshot of a given url using TOR", category="get")
def screenShot(ctx):
    try:
        tmp = url
        del tmp
    except NameError:
        print("Please set a url.")
        return
    from selenium import webdriver

    linux = False
    if sys.platform.startswith('linux'):
        linux = True
        print("Starting Tor Service")
        os.system("service tor start")
        print("Added proxies can be configured in proxychains.conf file")
        print("It's also recommended to enable dynamic chains in the proxychains.conf file")

    if settings["browser"]["browser"] == "chrome":
        options = webdriver.ChromeOptions()
        if settings["browser"]["headlessMode"]:
            options.add_argument("--headless")  # Launch headless browser
        # options.add_argument(f"--window-size={settings['screenshot']['width']},{settings['screenshot']['height']}")

        if settings["browser"]["forceTor"] and not linux:
            os.system("start Tor_Browser/Browser/TorBrowser/Tor/tor.exe")
            print("Applying proxy...", end="")
            if settings["browser"]["proxy"] == "":
                options.add_argument('--proxy-server=%s' % "socks5://127.0.0.1:9050")  # Use tor proxy
            else:
                print("Proxy specified conflict with forceTor setting. Either change the proxy to \"\", or turn off forceTor")
            print("Done!")
        else:
            if settings["browser"]["proxy"] != "":
                print("Applying proxy...", end="")
                options.add_argument('--proxy-server=%s' % f"{settings['browser']['proxy']}")  # Use other proxy
                print("Done!")

        driver = webdriver.Chrome(options=options)

    elif settings["browser"]["browser"] == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions

        options = FirefoxOptions()

        if settings["browser"]["headlessMode"]:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)

    else:
        print("Invalid browser selected in config.json. Please change the name of the browser to match and restart the application.")
        return

    print("Loading url...", end="")
    try:
        driver.set_window_size(settings["screenshot"]["width"], settings["screenshot"]["height"])
        driver.get(url)
        print("Done!")
    except selenium.common.exceptions.WebDriverException:
        print("Failed to load url.")
    except NameError:
        print("Please set a url.")
        return

    print("Taking screenshot...", end="")
    try:
        subprocess.run(["mkdir", "screenshots"])
    except FileNotFoundError:
        pass
    driver.save_screenshot("screenshots/{}.png".format(url[url.index("//") + 2:].replace("/", "").replace(".", "")))
    print("Done!\nScreenshot will be saved under the 'screenshots' folder.")
    driver.quit()

    if settings["browser"]["forceTor"] and not linux:
        subprocess.run(["taskkill", "/F", "/IM", '"tor.exe"'.rstrip()])  # Make sure to end tor
        print("Killed tor client.")

    if linux:
        print("Stopping Tor Services...")
        os.system("service tor stop")
        print("Tor Service successfully stopped.")



art.tprint("Depth-Finder")

try:
    with open("config.json") as config:
        settings = json.load(config)

        if bool(settings["startup"]["verifyLibraries"]):
            import packageManager
        if bool(settings["startup"]["installTor"]):
            import installTor
except FileNotFoundError:
    print("Failed!\n\tConfiguration file not found. Creating new file...", end="")
    config = open("config.json", "w+")
    settings = {
        "screenshot": {
            "width": 1920,
            "height": 1080
        },
        "browser": {
            "browser": "chrome",
            "forceTor": False,
            "proxy": "",
            "defaultBrowser": "chrome",
            "headlessMode": True
        },
        "startup": {
            "verifyLibraries": True,
            "installTor": False
        }
    }
    json.dump(settings, config)

whiteListedPorts = [80, 443]

app.run()
