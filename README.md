# Phishing-Detective

Phishing-Detective is a command line application for Windows 10 built to detect a phishing site from two url's

Note: If you want to be able to use this as a full CLA then you need to look at the releases and find the .exe installer. Then you must add the folder path to your System PATH variable

## How it works
A simple algorithm is used in order to determine if a URL is possibly a malicious link
  1. Input the URL of the malicious link in question
  2. Input a known safe URL
  3. Phishing-Detective pull information about the URL in question
  4. Phishing-Detective will compare the data of the URL in question with the known safe URL
  5. Phishing-Detective will give you an evaluation based on the data found
