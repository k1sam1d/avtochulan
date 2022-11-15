import telebot
from telebot import types

TOKEN = '5746786080:AAHVIPHS0ftz15JKzeAZaSsP-tfXDsU2l7s'

bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("/start")
item2 = types.KeyboardButton("/help")
item3 = types.KeyboardButton("/BMW")
item4 = types.KeyboardButton("/MERCEDES")
item5 = types.KeyboardButton("/AUDI")

markup.add(item1, item2, item3, item4, item5)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Приветствую, сотрудник компании Avtochulan.
Этот бот поможет тебе конвертировать номер детали в удобный для внесения в BAZON вид.

Если возникнут трудности - напиши /help''')
    bot.send_message(message.chat.id, """Для начала выбери марку своей машины!
    /BMW — конвертация номера запчасти BMW
    /MERCEDES — конвертация номера запчасти Mercedes
    /AUDI — конвертация номера запчасти Audi
    """)


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id, '''/start - запуск бота
/help - справка
/BMW - конвертация номера детали BMW
/MERCEDES - конвертация номера детали Mercedes
/AUDI - конвертация номера детали Audi''')


@bot.message_handler(commands=['BMW'])
def welcome_bmw(message):
    sent = bot.send_message(message.chat.id, '''Отправь мне номер детали BMW
Например, 54124567890''')
    bot.register_next_step_handler(sent, bmw)


@bot.message_handler(commands=['MERCEDES'])
def welcome_mercedes(message):
    sent = bot.send_message(message.chat.id, '''Отправь мне номер детали Mercedes
Например, A2056243802''')
    bot.register_next_step_handler(sent, mb)


@bot.message_handler(commands=['AUDI'])
def welcome_audi(message):
    sent = bot.send_message(message.chat.id, '''Отправь мне номер детали Audi
Например, 80A567931''')
    bot.register_next_step_handler(sent, audi)


def create_string_with_space_for_bmw(number):
    new_string = [number[0:2], number[2:4], number[4:5], number[5:8], number[8:]]
    new_string = ' '.join(new_string)
    return new_string


def create_string_with_space_for_mb(number):
    new_string = [number[0:1], number[1:4], number[4:7], number[7:9], number[9:]]
    new_string = ' '.join(new_string)
    return new_string


def create_string_with_space_for_audi(number):
    new_string = []
    if len(number) == 9:
        new_string = [number[0:3], number[3:6], number[6:]]
    elif len(number) == 10:
        new_string = [number[0:3], number[3:6], number[6:9], number[9:]]
    new_string = ' '.join(new_string)
    return new_string


def choice(message, result):
    bot.send_message(message.chat.id, result)
    bot.send_message(message.chat.id, '''
/BMW - конвертация номера детали BMW
/MERCEDES - конвертация номера детали Mercedes
/AUDI - конвертация номера детали Audi''')


def translate(code):
    code = code.replace('A', 'А')
    code = code.replace('M', 'М')
    code = code.replace('K', 'К')
    code = code.replace('W', 'В')
    code = code.replace('D', 'Д')
    code = code.replace('C', 'С')
    code = code.replace('B', 'Б')
    code = code.replace('L', 'Л')
    code = code.replace('T', 'Т')
    code = code.replace('E', 'Е')
    return code


def bmw(message):
    result = ''
    list_of_numbers = message.text.split()
    for number in list_of_numbers:
        first = create_string_with_space_for_bmw(number)
        second = number[4:]

        result += ', '.join([number, first, second]) + '\n'

    choice(message, result)


def mb(message):
    result = ''
    list_of_numbers = message.text.split()
    for number in list_of_numbers:
        first = create_string_with_space_for_mb(number)
        second = create_string_with_space_for_mb(number)
        third = number

        result += ', '.join([number, first, translate(second), translate(third)]) + '\n'

    choice(message, result)


def audi(message):
    result = ''
    list_of_numbers = message.text.split()
    for number in list_of_numbers:
        first = create_string_with_space_for_audi(number)
        second = create_string_with_space_for_audi(number)
        third = number

        result += ', '.join([number, first, translate(second), translate(third)]) + '\n'

    choice(message, result)

headers ={
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}

bot.polling(none_stop=True)