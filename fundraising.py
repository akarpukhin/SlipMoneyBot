from telegram import ReplyKeyboardMarkup


def fund_raising_main(bot, update):
    bot.sendMessage(update.message.chat_id, text="Отлично! \n Вы решили создать новый сбор!\n"
        "Как мы его назовём?", parse_mode='HTML')
    return 'FundRaising'

def fund