import os
import subprocess
import time


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def installTor():
    import sys

    linuxURL = "https://www.torproject.org/dist/torbrowser/11.0.1/tor-browser-linux64-11.0.1_en-US.tar.xz"
    windowsURL = "https://www.torproject.org/dist/torbrowser/11.0.1/torbrowser-install-win64-11.0.1_en-US.exe"
    windowsInstallerName = windowsURL.split("/")[-1]

    if sys.platform.startswith('linux'):
        print("[ERROR]: Linux support has not been added as of now. Please check later.")
        # os.system("wget linuxURL")
        # Make sure to add linux support...
    elif sys.platform.startswith('win32'):
        if "torInstaller.exe" not in os.listdir():
            print("Installing TOR executable...", end="")

            import requests
            r = requests.get(windowsURL, allow_redirects=True)
            open("torInstaller.exe", "wb").write(r.content)

            print("Done!\n[WARNING] In 5 seconds the executable will be run!\nPLEASE COMPLETE THE INSTALLATION PROCESS, INSTALL IT INTO THE CURRENT DIRECTORY, AND NAME THE FOLDER 'Tor Browser'!")
            time.sleep(5)

        if "Tor Browser" not in os.listdir():
            os.system("start torInstaller.exe")

        print("Checking to make sure that TOR is installed on your machine in the proper directory...", end="")
        flag = False
        for x in range(0, 10):
            if "Tor Browser" in os.listdir():
                print("DONE!\nThank you for installing TOR")
                flag = True
                break
            time.sleep(0.5)
        if not flag:
            print("FAILED!\nMax reattempts reached. Please try again.")


installTor()
