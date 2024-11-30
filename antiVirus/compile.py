import PyInstaller.__main__
import os

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

print(f"{Fore.CYAN}---------------------------- {Style.RESET_ALL}")
print("")
print(f"{Fore.CYAN}Starting compiling {Fore.GREEN}AntiVirus {Style.RESET_ALL}")
print(f"{Fore.CYAN}Starting compiling {Fore.GREEN}AntiVirus {Style.RESET_ALL}")
print(f"{Fore.CYAN}Starting compiling {Fore.GREEN}AntiVirus {Style.RESET_ALL}")
print("")
print(f"{Fore.CYAN}---------------------------- {Style.RESET_ALL}")

PyInstaller.__main__.run([
    f"./antiVirus/main.py",
    f"-n=AntiVirus",
    f"--clean",
    f"--onefile",
    f"--windowed",
    f"--uac-admin",
    f"--noconfirm",
    f"--log-level=WARN",
    f"--add-data=virus/Data:./",
    f"--icon=./antiVirus/Data/LOGO.ico"
])