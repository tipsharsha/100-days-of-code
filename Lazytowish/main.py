"""wishes on the days that i don't"""
import telebot
import holidays
import datetime

API = "5322356363:AAH9CQKxPVuflmTeAQvazdaiBoQ28QwRYQ4"
bot = telebot.TeleBot(API)
@bot.message_handler(commands = ["hello"])
def greet(message):
    bot.reply_to(message,"Maybe")
    

bot.polling()