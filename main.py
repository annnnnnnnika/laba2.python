import random
import telebot
from telebot import types
TOKEN = "7001971554:AAEUydGqDMBIR6O_cbrspokZr2tYoo9-wYE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, ' Введите число от 1 до 100'.format(message.from_user))
    bot.random_number = random.randint(1, 100)
@bot.message_handler(func = lambda message:True)
def guess_number(message):
    try:
        number = int(message.text)
        if number > bot.random_number:
            bot.send_message(message.chat.id, ' Мое число меньше чем ' + str(number))
        elif number < bot.random_number:
            bot.send_message(message.chat.id, ' Мое число больше чем ' + str(number))
        else:
            bot.send_message(message.chat.id, ' Поздравляю, вы победили!')
            bot.send_message(message.chat.id, ' Чтобы сыграть заново нажми /start')
    except ValueError:
        bot.send_message(message.chat.id, ' Введите число от 1 до 100')

bot.polling(none_stop = True)
