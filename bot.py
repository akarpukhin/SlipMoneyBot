from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.chat import Chat
import os
from datetime import datetime
import sys
import time
import configs
import logging
from botdb import db_session, engine
from botdb import Base, User, UserList, Goal, Event, List


if not os.path.exists(configs.LOG_FILE):
    os.mkdir(os.path.dirname(configs.LOG_FILE))

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=configs.LOG_FILE
                    )


def start_bot(bot, update):
    mytext = "Привет {}! Спасибо, что добавили меня!".format(update.message.chat.first_name)
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.first_name))
    update.message.reply_text(mytext)
    user = User(update.message.chat.id, update.message.chat.first_name)
    db_session.add(user)
    db_session.commit()


def restart(bot, update):
    bot.send_message(update.message.chat_id, "Bot is restarting...")
    time.sleep(0.2)
    os.execl(sys.executable, sys.executable, *sys.argv)


# добавление новой цели
def goal_add(bot, update):
# получаем строку от пользователя и разбиваем её на части по пробелам 
# формат строки должен быть следующим /goal <имя цели - может быть из нескольких слов> <целевая_сумма - целое число>
# при этом главное, чтобы в конце строки было целое число, а до него может идти имя цели из нескльких слов

# N.B. !!! будет расширено - пока минимальная заглушка для задания цели

    goal_string = update.message.text.split()
    if (len(goal_string) > 2)  and goal_string[-1].isdigit():
        print (goal_string)
        if len(goal_string) > 3:
            goal_name = " ".join(goal_string[1:-1])
        else:
            goal_name = goal_string[1]
        print (goal_name)
        goal = Goal(goal_name = goal_name, goal_target = int(goal_string[-1]))
        db_session.add(goal)
        db_session.commit()


def main():
    Base.metadata.create_all(bind=engine)

    updtr = Updater(configs.TELEGRAM_BOT_KEY)

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(CommandHandler('r', restart))

# обработчик добавления новой цели
    updtr.dispatcher.add_handler(CommandHandler('goal', goal_add))


    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    logging.info('Bot started')
    main()
