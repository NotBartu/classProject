import PyInstaller.__main__

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

print(f"{Fore.CYAN}------------------------ {Style.RESET_ALL}")
print("")
print(f"{Fore.CYAN}Starting compiling {Fore.RED}Virus {Style.RESET_ALL}")
print(f"{Fore.CYAN}Starting compiling {Fore.RED}Virus {Style.RESET_ALL}")
print(f"{Fore.CYAN}Starting compiling {Fore.RED}Virus {Style.RESET_ALL}")
print("")
print(f"{Fore.CYAN}------------------------ {Style.RESET_ALL}")

PyInstaller.__main__.run([
    f"./virus/main.py",
    f"-n=Virus",
    f"--clean",
    f"--onefile",
    f"--windowed",
    f"--uac-admin",
    f"--noconfirm",
    f"--log-level=WARN",
    f"--add-data=virus/Data:./",
    f"--icon=./virus/Data/LOGO.ico"
])