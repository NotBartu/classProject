import os

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
