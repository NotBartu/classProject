import os
import PyInstaller.__main__
from OpenGL.converters import Output
from colorama import init as colorama_init, Fore, Style

colorama_init()

# Set the paths
main_file = "main.py"
data_folder = "Data"
output_name = "Virus"

print(f"{Fore.CYAN}------------------------ {Style.RESET_ALL}")
print(f"{Fore.CYAN}Starting compiling {Fore.RED}Virus {Style.RESET_ALL}")
print(f"{Fore.CYAN}------------------------ {Style.RESET_ALL}")

PyInstaller.__main__.run([
    main_file,
    "--onefile",
    "--add-data", f"{data_folder}{os.pathsep}{data_folder}",
    "--name", output_name,
    "--clean",
    "--icon", f"{data_folder}/LOGO.ico",
    "--noconfirm",
    "--uac-admin",
    "--windowed",
    f"--log-level", "WARN",
])

print(f"{Fore.YELLOW}Compiled {output_name} {Fore.GREEN}successfully {Style.RESET_ALL}")

