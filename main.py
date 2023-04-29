import telegram
from telegram.ext import *

# Replace this with your actual token
TOKEN = "6248388608:AAEbgV0xjJAklYveBCsXdA1SvwVrgfZklvs"

# Store names in a list
names = []

# Define the handlers for the commands
def start_command(update, context):
    update.message.reply_text("Hello! Please suggest a name for the next executive team.")

def batch_command(update, context):
    update.message.reply_text("Please enter their batch.")

def department_command(update, context):
    update.message.reply_text("Please enter their department if known.")

# Define the handler for messages
def handle_message(update, context):
    text = update.message.text.strip()
    names.append(text)
    update.message.reply_text("Name {} has been added to the list.".format(text))

def main():
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add the command handlers
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('batch', batch_command))
    dp.add_handler(CommandHandler('department', department_command))

    # Add the message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
