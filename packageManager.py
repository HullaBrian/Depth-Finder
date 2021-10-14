import os
try:
    import click  # Tries to import
except ModuleNotFoundError:
    os.system("pip install -U click")  # Installs click if not already installed