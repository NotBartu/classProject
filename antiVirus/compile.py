import PyInstaller.__main__
from colorama import init as colorama_init, Fore, Style

colorama_init()

print("\033[H\033[J", end="")

print(f"{Fore.CYAN}---------------------------- {Style.RESET_ALL}")
print(f"{Fore.CYAN}Starting compiling {Fore.GREEN}AntiVirus {Style.RESET_ALL}")
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

print(f"{Fore.YELLOW}Compiled AntiVirus {Fore.GREEN}successfully {Style.RESET_ALL}")