import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define command handler functions
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Sou um bot do Telegram.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Main function to start the bot
def main():
    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Read token from token.txt file
    token_file = os.path.join(current_dir, 'token.txt')
    with open(token_file, 'r') as file:
        token = file.read().strip()

    # Create the Updater and pass it your bot's token
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("echo", echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
