# Phishing-Detective
Phishing-Detective is a command line application for Windows 10+ (and hopefully Linux) built for the purpose of detecting phishing attempts.

## How it works
Phishing-Detective has a variety of tools to assist you in safely finding out whether or not a given url is phishing or not:
  - Get WHOIS data
    - Gathers data from WHOIS on the given url and presents it back to you in a convienent dictionary split among multiple lines.
  - Get the SSL certificate status
    - Determines if the SSL certificate of the given url is valid or not.
  - Get the port number of the site
    - A bit less useful than the other commands, but still useful for beginners.
    - Splices the given url and retrieves the port number that the url is trying to access.
  - Get registration
    - Determines if the given url is registered and, if it is, what organization has registered it.
  - Get screenshot
    - The most complex tool to date.
    - Anonomously browses to the given url using tor, then uses selenium to capture a screenshot of the webpage.
 
## Requirements
*Note: Phishing-Detective will only verify and install libraries if you have the "verifyLibraries" configuration set to true in config.json*

Phishing-Detective requires a few libraries, but don't worry! Phishing-Detective, when run, will verify that all libraries are installed, and install them for you if needed.
In regards to tor, you will need to do some of the steps yourself, but you will only need to go through the installation process.
The installer will run for you, and the only thing you need to do is name the directory "Tor_Browser"
Other than installing tor yourself, you will not need to install anything, but if you do want a list of required libraries:
  - [art](https://pypi.org/project/art/)
  - [whois](https://pypi.org/project/python-whois/)
  - [requests](https://pypi.org/project/requests/)
  - [chromedriver_autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/)
  - [selenium](https://pypi.org/project/selenium/)

## Use
For a list of usable arguments type 
```
pd> help
```
```

help   Displays this menu
"Set" Commands
--------------
	Command            Description
	-------            -----------
	set url            sets the url to a given url

"Get" Commands
--------------
	Command            Description
	-------            -----------
	get info           give the relevant information on a given url
	get sslverify      verifies the SSL certificate of the url
	get port           retrieves the port of the url
	get registration   determines whether or not a domain is registered or not
	get screenshot     retrieves a screenshot of a given url using TOR
```
## Customization
Phishing-Detective offers a few ways to customize it:
  - Screenshot width and height (Default 1920x1080)
  - Browser (Default "chrome")
  - Force tor (Default false)
  - Proxy (Default "")
  - Headless browser (Default true)
  - Verify libraries (Default true)
  - Install tor (Default false)

You can customize these settings in the config.json file within the directory that main.py is stored in.
