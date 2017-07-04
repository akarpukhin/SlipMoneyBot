from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


def join(bot, update):
    keyboard = [['Event'], ['Goal']]
    choise_keyboard = ReplyKeyboardMarkup(keyboard)
    bot.send_message(
        update.message.chat_id,
        text="Куда вы хотите присоедениться ?",
        reply_markup=choise_keyboard)
    return "Choise"


def choise(bot, update):
    choise = update.message.text
    remove_choise_keyboard = ReplyKeyboardRemove()
    bot.send_message(
        update.message.chat_id,
        text="Ты выбрал {choice}!".format(choice=choise),
        reply_markup=remove_choise_keyboard)
    return "Menu"
