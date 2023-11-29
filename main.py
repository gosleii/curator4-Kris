import telebot

bot = telebot.TeleBot('6740319292:AAE76ooBh99i1dDp9XuZE9qs7-_J_fhC-Tk')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Доброго времени суток, хотите ли вы окунуться в мир поэзии?\nЕсли вы готовы, то давайте начнем!', parse_mode = 'Markdown')

@bot.message_handler(commands=['read'])
def main(message):
    bot.send_message(message.chat.id,
                        'Я вижу каменное небо \nНад тусклой паутиной вод. \nВ тисках постылого Эреба \nДуша томительно живет. \nЯ понимаю этот ужас \nИ постигаю эту связь: \nИ небо падает, не рушась, \nИ море плещет, не пенясь. \n*О.Мандельштам*', parse_mode = 'Markdown')

@bot.message_handler(commands=['learn_more'])
def main(message):
        bot.send_message(message.chat.id,
                              'Для того, чтобы ознакомиться с полным собранием сочинений Осипа Мандельштама, перейдите по [ссылке](https://www.culture.ru/literature/poems/author-osip-mandelshtam)', parse_mode = 'Markdown')

bot.infinity_polling()