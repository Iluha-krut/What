import telebot
import Parser_for_my_Bot
import Sorter

bot_token = '7496534822:AAGIufL8--QZf5lfJIZ9lGY-2MkjUf_Np5I'
bot = telebot.TeleBot(bot_token)
bot_name = 'https://t.me/Bot_po_praktike_bot'
avionics_rus = 'Яндекс патенты: https://yandex.ru/patents?dco=RU&dco=SU&dl=ru&dt=0&dty=1&dty=2&s=1&sp=0&spp=10&st=0&text=%D0%B0%D0%B2%D0%B8%D0%BE%D0%BD%D0%B8%D0%BA%D0%B0'
avionics_eng = 'Иностранные патенты: https://patentscope.wipo.int/search/en/result.jsf?_vid=P10-LYZPWS-70739'
selhoz = open('Сельхоз.txt', 'r', encoding='utf-8')
sp_selhoz = selhoz.read().split('\n')
shindex = 0
war = open('Военные дроны.txt', 'r')
sp_war = war.read().split('\n')
warindex = 0
another = open('Другое.txt', 'r', encoding='utf-8')
sp_another = another.read().split('\n')
anotherindex = 0
sp_komands = ['БПЛА', 'С/Х дроны', 'Военные дроны', 'Другое', 'Назад', 'Авионика', 'Наши патенты', 'Зарубежные патенты', 'Обновить базу']

@bot.message_handler(commands=['start'])
def start_message(message):
    hello_message = 'Здравствуйте, данный бот предназначен для поиска новостей о БПЛА и авионике по тегам из клавиатуры'
    bot.send_message(message.chat.id, hello_message, reply_markup=keyboard())
    bot.send_message(message.chat.id, 'Воспользуйтесь клавиатурой')


@bot.message_handler(func=lambda message: message.text == 'БПЛА')
def bpla(message):
    klava = telebot.types.ReplyKeyboardMarkup()
    button_sh = telebot.types.KeyboardButton('С/Х дроны')
    button_war = telebot.types.KeyboardButton('Военные дроны')
    button_another = telebot.types.KeyboardButton('Другое')
    button_back = telebot.types.KeyboardButton('Назад')
    klava.add(button_sh, button_war, button_another, button_back)
    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=klava)


@bot.message_handler(func=lambda message: message.text == 'Другое')
def another_drones(message):
    global anotherindex
    if anotherindex < len(sp_another) - 1:
        bot.send_message(message.chat.id, sp_another[anotherindex])
        anotherindex += 1
    else:
        bot.send_message(message.chat.id, 'Вы просмотрели все новости по данной теме')
        anotherindex += 1


@bot.message_handler(func=lambda message: message.text == 'С/Х дроны')
def sh_drones(message):
    global shindex
    if shindex < len(sp_selhoz) - 1:
        bot.send_message(message.chat.id, sp_selhoz[shindex])
        shindex += 1
    else:
        bot.send_message(message.chat.id, 'Вы просмотрели все новости по данной теме')
        shindex += 1


@bot.message_handler(func=lambda message: message.text == 'Военные дроны')
def war_drones(message):
    global warindex
    if warindex < len(sp_war) - 1:
        bot.send_message(message.chat.id, sp_war[warindex])
        warindex += 1
    else:
        bot.send_message(message.chat.id, 'Вы просмотрели все новости по данной теме')
        warindex += 1


@bot.message_handler(func=lambda message: message.text == 'Авионика')
def avionics(message):
    bot.send_message(message.chat.id, 'Обратите внимание, сайтов с новостями конкретно об авионике нет, а парсинг поисковиков требует средств, недоступных обычным студентам, а также он бесполезен сам по себе(это то же самое, что просто найти в интернете "авионика"). По этой причине мы приняли решение предоставить пользователю сайты с патентами, о которых он возможно не знал, с готовыми фильтрами и поиском. Воспользуйтесь клавиатурой')
    klava = telebot.types.ReplyKeyboardMarkup()
    button_rus = telebot.types.KeyboardButton('Наши патенты')
    button_eng = telebot.types.KeyboardButton('Зарубежные патенты')
    button_back = telebot.types.KeyboardButton('Назад')
    klava.add(button_rus, button_eng, button_back)
    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=klava)


@bot.message_handler(func=lambda message: message.text == 'Наши патенты')
def nashi_patenti(message):
    global avionics_rus
    bot.send_message(message.chat.id, avionics_rus)


@bot.message_handler(func=lambda message: message.text == 'Зарубежные патенты')
def zarubezh(message):
    global avionics_eng
    bot.send_message(message.chat.id, avionics_eng)


@bot.message_handler(func=lambda message: message.text not in sp_komands)
def not_komand(message):
    bot.send_message(message.chat.id, 'Данный бот не отвечает на сообщения, которых нет в клавиатуре. Воспользуйтесь клавиатурой')


@bot.message_handler(func=lambda message: message.text == 'Обновить базу')
def obnova(message):
    bot.send_message(message.chat.id, 'Обновление займет около 5-ти минут, после этого могут появиться свежие новости')
    Parser_for_my_Bot.parcing()
    Sorter.sorting()


@bot.message_handler(func=lambda message: message.text == 'Назад')
def back(message):
    global shindex
    shindex = 0
    global avindex
    avindex = 0
    global warindex
    warindex = 0
    global anotherindex
    anotherindex = 0
    bot.send_message(message.chat.id, 'Воспользуйтесь клавиатурой', reply_markup=keyboard())


def keyboard():
    klava = telebot.types.ReplyKeyboardMarkup()
    button_bpla = telebot.types.KeyboardButton('БПЛА')
    button_avionics = telebot.types.KeyboardButton('Авионика')
    button_obnov = telebot.types.KeyboardButton('Обновить базу')
    klava.add(button_avionics, button_bpla, button_obnov)
    return klava


bot.infinity_polling()
