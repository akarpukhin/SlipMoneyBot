import botdb
from telegram import ReplyKeyboardMarkup


def info(bot, update, args):
    if len(args) == 0:
        all_variants = botdb.Goal.query.filter(botdb.Goal.chat_id ==
                                               update.message.chat_id).filter(botdb.Goal.is_active).all()
        if len(all_variants) > 10:
            bot.sendMessage(update.message.chat_id, "Введите имя цели")
        else:
            reply_keyboard = []
            for i in range(0, len(all_variants)):
                reply_keyboard.append([all_variants[i].goal_name])
            bot.sendMessage(update.message.chat_id, "Какую информацию вы хотели бы получить?",
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return "Info_Name"
    else:
        name = args[0]
        chosen_fundraising = botdb.Goal.query.filter(botdb.Goal.chat_id ==
                                                     update.message.chat_id).filter(botdb.Goal.goal_name == name).all()
        if (len(chosen_fundraising) == 0):
            bot.sendMessage(update.message.chat_id, "Такой цели не существует. Попробуйте еще раз")
        else:
            information = "Имя цели: <b>" + name + "</b>\n"
            if chosen_fundraising[0].is_active:
                information = information + "Статус: <b>активна</b>\n"
            else:
                information = information + "Статус: <b>неактивна</b>\n"
            information = information + "Цель: <b>" + str(chosen_fundraising[0].goal_target) + "</b> руб.\n"
            information = information + "Собрано: <b>" + str(chosen_fundraising[0].goal_amount) + "</b> руб.\n"
            bot.sendMessage(update.message.chat_id, text=information, parse_mode="HTML")
    return "Menu"


def info_name(bot, update):
    name = update.message.text
    chosen_fundraising = botdb.Goal.query.filter(botdb.Goal.chat_id ==
                                                 update.message.chat_id).filter(botdb.Goal.goal_name == name).all()
    if (len(chosen_fundraising) == 0):
        bot.sendMessage(update.message.chat_id, "Такой цели не существует. Попробуйте еще раз")
    else:
        information = "Имя цели: <b>" + name + "</b>\n"
        if chosen_fundraising[0].is_active:
            information = information + "Статус: <b>активна</b>\n"
        else:
            information = information + "Статус: <b>неактивна</b>\n"
        information = information + "Цель: <b>" + str(chosen_fundraising[0].goal_target) + "</b> руб.\n"
        information = information + "Собрано: <b>" + str(chosen_fundraising[0].goal_amount) + "</b> руб.\n"
        bot.sendMessage(update.message.chat_id, text=information, parse_mode="HTML")
    return "Menu"
