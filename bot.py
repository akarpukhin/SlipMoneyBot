from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.chat import Chat
import os
from datetime import datetime
import configs
import logging
import botdb


if not os.path.exists(configs.LOG_FILE):
    os.mkdir(os.path.dirname(configs.LOG_FILE))


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=configs.LOG_FILE
                    )

def start_bot(bot, update):
    mytext = "Привет {}! Спасибо, что добавили меня!".format(update.message.chat.first_name)
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

    userlist = list = bot.getChatMember(update.message.chat.id)
    print(userlist)


def main():
    updtr = Updater(configs.TELEGRAM_BOT_KEY)

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    logging.info('Bot started')
    main()