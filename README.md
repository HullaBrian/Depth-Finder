# Depth-Finder
Depth-Finder is a command line application for Windows and Linux built for the purpose of detecting phishing attempts.

## How it works
Depth-Finder has a variety of tools to assist you in safely finding out whether or not a given url is phishing or not:
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
*Note: Depth-Finder will only verify and install libraries if you have the "verifyLibraries" configuration set to true in config.json*

Depth-Finder requires a few libraries, but don't worry! Depth-Finder, when run, will verify that all libraries are installed, and install them for you if needed.
In regards to tor, you will need to do some of the steps yourself, but you will only need to go through the installation process.
The installer will run for you, and the only thing you need to do is name the directory "Tor_Browser"
Other than installing tor yourself, you will not need to install anything, but if you do want a list of required libraries:
  - [art](https://pypi.org/project/art/)
  - [whois](https://pypi.org/project/python-whois/)
  - [requests](https://pypi.org/project/requests/)
  - [chromedriver_autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/)
  - [selenium](https://pypi.org/project/selenium/)
  - [sh3ll](https://pypi.org/project/sh3ll/)

## Use
For a list of usable arguments type 
```
df>help
```
```
help	Displays this menu

"set" Commands:
---------------
	Command    Aliases         Help                           
	-------    --------          ----
	set url    []    sets the url to a given url

"get" Commands:
---------------
	Command             Aliases         Help                                                       
	-------             --------        ----
	get info            []              give the relevant information on a given url           
	get sslverify       ['sv']          verifies the SSL certificate of the url                
	get isRegistered    ['ir', 'iR']    determines whether or not a domain is registered or not
	get port            ['p', 'P']      retrieves the port of the url                          
	get ScreenShot      ['SS', 'ss']    retrieves a screenshot of a given url using TOR
```
*Please note: the help menu for the sh3ll library is extremely basic, and often unhelpful as of now. Under further the development (coming soon), the menu should become much more helpful to those using depth-finder.*
## Customization
Depth-Finder offers a few ways to customize it:
  - Screenshot width and height (Default 1920x1080)
  - Browser (Default "chrome")
  - Force tor (Default false)
  - Proxy (Default "")
  - Headless browser (Default true)
  - Verify libraries (Default true)
  - Install tor (Default false)

You can customize these settings in the config.json file within the directory that main.py is stored in.
