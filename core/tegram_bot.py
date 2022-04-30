import telebot
import json

with open('website/key/telegram_token.txt') as f:
    data = json.load(f)
    API_TOKEN = data['TOKEN']
    TELEGRAM_USER_ID = data['telegram_user_id']
    # Для получения TOKEN написать боту @BotFather, создать своего бота, указать полученный TOKEN
    # Для получения TELEGRAM_USER_ID написать боту @getmyid_bot, указать полученный user id, либо chat id

bot = telebot.TeleBot(API_TOKEN)


def send_message(message):
    """Отправка сообщения в телеграм по user_id"""
    bot.send_message(TELEGRAM_USER_ID, message)
