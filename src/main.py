import telebot
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join("Data", 'settings.ini'))

bot = telebot.TeleBot(config["Telegram"]["bot_token"])

bot.send_message(config["Telegram"]["chat_id"], "Virus Started!")

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.reply_to(message, "Stopping bot")
    bot.stop_polling()


bot.polling()