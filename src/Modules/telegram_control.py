import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
from Modules.computer_control import ComputerControl
import os

class TelegramControl:
    def __init__(self, token, chat_id, messages_file):
        self.bot = telebot.TeleBot(token)
        self.chat_id = chat_id
        self.messages = self._load_messages(messages_file)
        self.pc_keyboard = None
        self.is_command_running = False  # Переменная состояния выполнения команды

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
        # Главная клавиатура
        self.main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        shutdown_button = KeyboardButton("Выключение")
        pc_control_button = KeyboardButton("Управление ПК")
        self.main_keyboard.add(shutdown_button, pc_control_button)

        # Клавиатура управления ПК
        self.pc_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        lock_button = KeyboardButton("Заблокировать ПК")
        shutdown_pc_button = KeyboardButton("Выключить ПК")
        restart_pc_button = KeyboardButton("Перезагрузить ПК")
        run_command_button = KeyboardButton("Выполнить команду на ПК")
        bsod_pc_button = KeyboardButton("Вызвать BSOD")
        screenshot_button = KeyboardButton("Получить скриншот")
        off_screen_button = KeyboardButton("Выключить экран")
        lock_input_button = KeyboardButton("Заблокировать ввод")
        unlock_input_button = KeyboardButton("Разблокировать ввод")
        cancel_button = KeyboardButton("Отмена")
        self.pc_keyboard.add(
            lock_button,
            shutdown_pc_button,
            restart_pc_button,
            run_command_button,
            bsod_pc_button,
            screenshot_button,
            off_screen_button,
            lock_input_button,
            unlock_input_button,
            cancel_button
        )

        # Обработчики
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

        @self.bot.message_handler(func=lambda message: message.text == "Перезагрузить ПК")
        def restart_pc(message):
            if ComputerControl.restart_pc():
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["restart_pc"])
            else:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["restart_pc_error"])

        @self.bot.message_handler(func=lambda message: message.text == "Выполнить команду на ПК")
        def run_command_init(message):
            self.bot.send_message(self.chat_id, self.messages["pc_control"]["run_command_on_pc_step1"])
            self.is_command_running = True

        @self.bot.message_handler(func=lambda message: message.text == "Вызвать BSOD")
        def restart_pc(message):
            self.bot.send_message(self.chat_id, self.messages["pc_control"]["bsod_pc"])
            if not ComputerControl.bsod_pc():
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["bsd_pc_error"])

        @self.bot.message_handler(func=lambda message: message.text == "Получить скриншот")
        def get_screenshot(message):
            """Capture a screenshot and send it via Telegram."""
            screenshot_path = ComputerControl.get_screenshot()
            if screenshot_path:
                with open(screenshot_path, "rb") as screenshot:
                    self.bot.send_photo(self.chat_id, screenshot)
                os.remove(screenshot_path)  # Удаляем скриншот после отправки
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["get_screenshot"])
            else:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["get_screenshot_error"])

        @self.bot.message_handler(func=lambda message: message.text == "Выключить экран")
        def turn_off_screen(message):
            """Turn off the screen."""
            if ComputerControl.turn_off_screen():
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["turn_off_screen"])
            else:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["turn_off_screen_error"])

        @self.bot.message_handler(func=lambda message: message.text == "Заблокировать ввод")
        def lock_input(message):
            """Lock input."""
            if ComputerControl.lock_input():
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["lock_input"])
            else:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["lock_input_error"])

        @self.bot.message_handler(func=lambda message: message.text == "Разблокировать ввод")
        def unlock_input(message):
            """Unlock input."""
            if ComputerControl.unlock_input():
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["unlock_input"])
            else:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["unlock_input_error"])

        @self.bot.message_handler(func=lambda message: message.text == "Отмена")
        def cancel(message):
            """Handle cancel button to return to the main keyboard."""
            self.is_command_running = False  # Сбрасываем состояние выполнения команды
            self.bot.send_message(self.chat_id, self.messages["bot_control"]["cancel"], reply_markup=self.main_keyboard)

        @self.bot.message_handler(func=lambda message: self.is_command_running)
        def handle_command(message):
            """Handle command execution on the PC."""
            success = ComputerControl.run_command_on_pc(message.text)  # Выполняем команду
            if success:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["run_command_on_pc_step2"])
            else:
                self.bot.send_message(self.chat_id, self.messages["pc_control"]["run_command_on_pc_step2_error"])
            self.is_command_running = False  # Сбрасываем флаг выполнения команды
            self.bot.send_message(self.chat_id, self.messages["pc_control"]["control"], reply_markup=self.pc_keyboard)

        # Запуск бота
        self.bot.send_message(self.chat_id, self.messages["bot_control"]["welcome"], reply_markup=self.main_keyboard)
        self.bot.polling()

    def send_message(self, message):
        try:
            self.bot.send_message(self.chat_id, message)
        except Exception as e:
            print(f"Error sending message: {e}")
