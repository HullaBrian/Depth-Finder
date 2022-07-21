import os
import ssl
import subprocess
import time
import sys
import distro


def installTor():
    if sys.platform.startswith('linux'):
        try:
            print("Installing Tor...", end="")
            linux_type = distro.id()
            if str(linux_type) == "gentoo":
                os.system("sudo emerge --ask net-vpn/tor")
            if str(linux_type) == "debian" or str(linux_type) == "ubuntu" or str(linux_type) == "linuxmint" or str(linux_type) == "raspbian":
                os.system("sudo apt install tor")
            if str(linux_type) == "arch":
                os.system("sudo pacman -S tor")
            if str(linux_type) == "rhel" or str(linux_type) == "centos":
                print("You are going to have to enable EPEL repo and add tor yourself. Use this link for help https://community.torproject.org/relay/setup/bridge/centos-rhel/")
            if str(linux_type) == "fedora":
                os.sytsem("sudo dnf install tor")
            if str(linux_type) == "opensuse":
                os.system("sudo zypper install tor")


            print("Done!")
            return
        except:
            print("sorry the automated Tor install process for your distribution has failed. You will have to install Tor yourself")

    elif sys.platform.startswith('win32'):
        windowsURL = "https://www.torproject.org/dist/torbrowser/11.0.1/torbrowser-install-win64-11.0.1_en-US.exe"
        windowsInstallerName = windowsURL.split("/")[-1]
        if "torInstaller.exe" not in os.listdir() and "Tor_Browser" not in os.listdir():
            print("Installing TOR executable...", end="")
            try:
                import requests
            except ModuleNotFoundError:
                print("Could not find a required library. Please verify all libraries before attempting to install tor.")
            try:
                r = requests.get(windowsURL, allow_redirects=True)
            except requests.exceptions.SSLError and ssl.SSLCertVerificationError:
                print("Error installing tor browser. Please check that your organization has not blocked tor.")
                return
            open("torInstaller.exe", "wb").write(r.content)

            print("Done!\n[WARNING] In 5 seconds the executable will be run!\nPLEASE COMPLETE THE INSTALLATION PROCESS, INSTALL IT INTO THE CURRENT DIRECTORY, AND NAME THE FOLDER 'Tor_Browser'!")
            time.sleep(5)

        if "Tor_Browser" not in os.listdir():
            # os.system("start torInstaller.exe")
            subprocess.run(["start", "torInstaller.exe"])
            # time.sleep(40.0)  # Give user enough time to properly install TOR onto their machine.

        print("Checking to make sure that TOR is installed on your machine in the proper directory...")
        flag = False
        print("Verification attempt  0/20", end="")
        for x in range(1, 21):
            if "Tor_Browser" in os.listdir():
                print("\nThank you for installing TOR")
                flag = True
                break
            for y in range(len(str(x))):
                print("\b", end="")
            print("\b\b\b" + str(x) + "/20", end="")
            time.sleep(1)
        if not flag:
            print("\nTor verification FAILED!\nMax reattempts reached. Please try again.")
        else:
            print("\nVerified tor.")
            pass


installTor()
