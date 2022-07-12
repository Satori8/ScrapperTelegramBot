import telebot
from MemesScrapper import MemesScrapper
import requests
users = []


def start_bot():
    bot = telebot.TeleBot("5463228182:AAEdFc9uArEYh4ps1rpQgxtqkRe5jaG4LOE", parse_mode=None)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    @bot.message_handler(commands=['memes'])
    def send_memes(message):
        chatid = message.chat.id
        memes = MemesScrapper.get_memes()
        for mem in memes:
            photo = requests.get(mem).content
            bot.send_photo(chatid, photo)

    bot.infinity_polling()

