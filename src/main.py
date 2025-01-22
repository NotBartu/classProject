import os
import sys
import configparser
from Modules.telegram_control import TelegramControl

# Define base path
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(base_path, "Data", "settings.ini")
messages_path = os.path.join(base_path, "Data", "messages.json")

# Load settings
config = configparser.ConfigParser()
config.read(config_path)

bot_token = config["Telegram"]["bot_token"]
chat_id = config["Telegram"]["chat_id"]

# Initialize Telegram control
telegram = TelegramControl(bot_token, chat_id, messages_path)

# Start listening for commands
telegram.start_listening()
