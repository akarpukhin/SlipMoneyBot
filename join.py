from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from botdb import Goal, User
import botdb


def join(bot, update):
    keyboard = [['Event'], ['Goal']]
    choice_keyboard = ReplyKeyboardMarkup(keyboard)
    bot.send_message(
        update.message.chat_id,
        text="Куда вы хотите присоедениться ?",
        reply_markup=choice_keyboard)
    return "Choice"


def choose_goal(bot, update):
    # choice = update.message.text  не помню зачем добавлял, если не вспомню, удалю
    goal_list = [['Цель: {}'.format(g.goal_name)]
                 for g in Goal.query.filter_by(is_active=True,
                                               chat_id=update.message.chat.id)]

    if not goal_list:
        keyboard = [['Yes'], ['No']]
        choice_keyboard = ReplyKeyboardMarkup(keyboard)
        text = "Сейчас нет активных целей. Создать ?"
        state = "Choice"

    if len(goal_list) > 1:
        keyboard = goal_list
        choice_keyboard = ReplyKeyboardMarkup(keyboard)
        text = "Выбери цель:"
        state = "Join"

    if len(goal_list) == 1:
        keyboard = goal_list
        choice_keyboard = ReplyKeyboardMarkup(keyboard)
        text = "Вы хотите присоедениться к этой цели ?"
        state = "Join"

    bot.send_message(
        update.message.chat_id,
        text=text,
        reply_markup=choice_keyboard
    )
    return state


def join_goal(bot, update):
    goal_name = update.message.text
    goal_name = goal_name.split(': ')[1]
    goal_id = [g.id
               for g in Goal.query.filter_by(is_active=True,
                                             goal_name=goal_name,
                                             chat_id=update.message.chat.id)]

    user_name = '{last_name} {first_name}'.format(
                last_name=update.message.from_user.last_name,
                first_name=update.message.from_user.first_name)

    telegram_id = update.message.from_user.id

    user_count = User.query.filter(User.telegram_id == telegram_id).count()

    if user_count < 1:
            user = botdb.User(telegram_id=telegram_id, user_name=user_name)
            botdb.db_session.add(user)
            botdb.db_session.commit()
    else:
        print('уже есть')

    return 'Menu'


def event_join(bot, update):
    choice = update.message.text
    remove_choice_keyboard = ReplyKeyboardRemove()
    bot.send_message(
        update.message.chat_id,
        text="Ты выбрал {choice}!".format(choice=choice),
        reply_markup=remove_choice_keyboard
    )
    return "Menu"
