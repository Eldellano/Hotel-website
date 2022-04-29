import telebot


with open('website/key/telegram_token.txt') as f:
    API_TOKEN = f.read().strip()

telegram_user_id = -414130804  # Для получения написать боту @getmyid_bot, указать полученный user id, либо chat id)
bot = telebot.TeleBot(API_TOKEN)


def send_message(message):
    """Отправка сообщения в телеграм по user_id"""
    bot.send_message(telegram_user_id, message)
