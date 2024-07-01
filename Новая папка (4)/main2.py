import telebot
import random
API_TOKEN ='7288614642:AAF2KdX2KmcWPZFx4dRQQk8-XMX1WT9ihlg'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=["start"])
def semd_welcom(message):
     bot.reply_to(message, "<b>Добро</b> пожаловать!")

@bot.message_handler(commands=["info"])
def semd_welcom(message):
    bot.reply_to(message, "Кандай биздин бот иштеди!")
    help_text = (
        "<b>Доступные команды:</b> \n"
        "/start - запуск бота\n"
        "/info - список команд и функциал бота\n"
    )
    bot.reply_to(message, help_text)



@bot.message_handler(commands=['rad'])
def send_help(message):
    try:
        random_index = random.randint(0,9)
        image_path = f"./img/image{random_index}.jpg"
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    except Exception as e:
        bot.reply_to(message, f"Призошла ошибка: {e}")

@bot.message_handler()
def handle_unknown_command(message):
    response = "<b>Просите я не знаю такой команды</b>."
    bot.reply_to(message, response)

bot.polling(none_stop=True)
