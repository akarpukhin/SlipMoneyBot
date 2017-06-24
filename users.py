import logging
from botdb import UserList, db_session, Users


def join(bot, update):
    mytext = "Привет {}!".format(update.message.chat.first_name)
    logging.info('Пользователь {} нажал /add'.format(update.message.chat.username))
    user_id = update.message.from_user.id
    user = bot.getChatMember(update.message.chat_id, user_id)
    last_name = user.user.last_name
    first_name = user.user.first_name
    username = user.user.username
    is_user = UserList.query.filter(UserList.user_id == user_id).all()
    if len(is_user) == 0:
        new_user = UserList(user_id)
        db_session.add(new_user)
        db_session.commit()
        new_user2 = Users(user_id, first_name, last_name, username)
        db_session.add(new_user2)
        db_session.commit()
    update.message.reply_text(mytext)
