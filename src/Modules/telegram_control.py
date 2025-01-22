import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
from computer_control import ComputerControl

class TelegramControl:
    def __init__(self, token, chat_id, messages_file):
        self.bot = telebot.TeleBot(token)
        self.chat_id = chat_id
        self.messages = self._load_messages(messages_file)
        self.pc_keyboard = None

    def _load_messages(self, file_path):
        """Load messages from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading messages: {e}")
            return {}

    def start_listening(self):
        """Start listening for commands."""
        # Main keyboard
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        shutdown_button = KeyboardButton("Выключение")
        pc_control_button = KeyboardButton("Управление ПК")
        keyboard.add(shutdown_button, pc_control_button)

        # PC control keyboard
        self.pc_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        lock_button = KeyboardButton("Заблокировать ПК")
        shutdown_pc_button = KeyboardButton("Выключить ПК")
        cancel_button = KeyboardButton("Отмена")
        self.pc_keyboard.add(lock_button, shutdown_pc_button, cancel_button)

        # Define handlers
        @self.bot.message_handler(func=lambda message: message.text == "Выключение")
        def shutdown(message):
            self.bot.reply_to(message, self.messages["bot_control"]["shutdown"])
            self.bot.stop_polling()

        @self.bot.message_handler(func=lambda message: message.text == "Управление ПК")
        def pc_control(message):
            self.bot.send_message(self.chat_id, self.messages["pc_control"]["control"], reply_markup=self.pc_keyboard)

        @self.bot.message_handler(func=lambda message: message.text == "Заблокировать ПК")
        def lock_pc(message):
            if ComputerControl.lock_pc():
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["lock_pc"])
            else:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["lock_pc_error"])

        @self.bot.message_handler(func=lambda message: message.text == "Выключить ПК")
        def shutdown_pc(message):
            if ComputerControl.shutdown_pc():
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["shutdown_pc"])
            else:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["shutdown_pc_error"])

        @self.bot.message_handler(func=lambda message: message.text == "Отмена")
        def cancel(message):
            self.bot.send_message(self.chat_id, self.messages["bot_control"]["cancel"], reply_markup=keyboard)

        # Start polling
        self.bot.send_message(self.chat_id, self.messages["bot_control"]["welcome"], reply_markup=keyboard)
        self.bot.polling()

    def send_message(self, message):
        try:
            self.bot.send_message(self.chat_id, message)
        except Exception as e:
            print(f"Error sending message: {e}")
