import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.INFO)

TOKEN = '7008404300:AAFdiNF-5cKbDo3DN2xpIv_8ZmlfSKd3bck'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to the group!')

def goodbye(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Goodbye!')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, start))
    dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, goodbye))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
