"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from datetime import datetime
import settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

planets = {
    'sun': ephem.Sun(),
    'mercury': ephem.Mercury(),
    'venus': ephem.Venus(),
    'mars': ephem.Mars(),
    'jupiter': ephem.Jupiter(),
    'saturn': ephem.Saturn(),
    'uranus': ephem.Uranus(),
    'neptune': ephem.Neptune(),
    }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(update, context):
    planet = update.message.text.split()[1].lower()
    p = planets[planet]
    p.compute(datetime.now())
    update.message.reply_text(ephem.constellation(p))



def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
