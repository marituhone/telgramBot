import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['suggest_name'])
def suggest_name(message):
    bot.reply_to(message, "Please suggest a name for our new exective team:")


@bot.message_handler(func=lambda message: True)
def process_name_suggestion(message):
    name_suggestion = message.text
    bot.reply_to(
        message, f"Thank you for suggesting the name '{name_suggestion}'.")


print('Starting bot...')
bot.polling()
