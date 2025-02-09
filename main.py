import telebot
from telebot import types
import time

wait = False
wait1 = False
wait_for_command_vernut = False
wait_for_command_vernut1 = False
a = 0

def cyph(j):
    d = [int(d) + 1 for d in str(j)]
    hid = ''
    for i in d:
        if i == 10:
            i = i - 10
        hid += str(i)
    hid = int(hid)
    return(hid)

def uncyph(j):
    d = [int(d) - 1 for d in str(j)]
    hid = ''
    for i in d:
        if i < 0:
            i = i + 10
        hid += str(i)
    hid = int(hid)
    return (hid)

found = False

f = open("saves.txt", "a")  # , encoding="utf-8")

token = "7482941140:AAHZw8seV2nKmj74EIt4Mc_kiqJi8Y8GLCw"

bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    a1 = str(message.from_user.id)
    if message.from_user.username == None:
        bot.send_message(message.from_user.id, "заведите себе 'юзернэйм'")
        a2 = message.from_user.first_name
    else:
        a2 = message.from_user.username
    a = "@" + a2 + " " + a1 + "\n"
    f = open('saves.txt', 'r')
    db = f.read()
    f.close()
    f = open('saves.txt', 'a')
    if not (a in db):
        f.write(a)
    f.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("написать")
    btn1 = types.KeyboardButton("вернуть")
    markup.add(btn, btn1)
    bot.send_message(message.from_user.id,"снизу кнопка чтобы написать, если ее нет то просто напиши слово 'написать'", reply_markup=markup)

    # bot.send_message(message.from_user.id,"пример @MIKHAILYANOV")
    # users[message.from_user.first_name] = message.from_user.id


#@bot.message_handler(commands=['users'])
#def send(message):
    #bot.send_message


@bot.message_handler(content_types=['text'])
def anonim(message):
    global wait, hid_us, wait1, target_name, target_message, wait_for_command_vernut, wait_for_command_vernut1, us, us_unshifr, target_message_for_vernut, a
    if message.text == "написать":
        bot.send_message(message.from_user.id, "напиши юзернейм кому ты хочешь написать")
        us = message.from_user.id
        #print(us)
        hid_us = cyph(us)
        #print(message.text)
        wait = True
        wait1 = False
    elif wait and not wait1:
        target_name = message.text
        print(target_name)
        bot.send_message(message.from_user.id, "введи сообщение которое надо отправить")
        wait = False
        wait1 = True
    elif not wait and wait1:
        wait1 = False
        target_message = message.text
        f = open('saves.txt', 'r')
        for line in f:
            if target_name in line:
                bot.send_message(line.split()[1], target_message)
                text = "айди отправителя " + str(hid_us)
                bot.send_message(line.split()[1], text)
                bot.send_message(message.from_user.id, "сообщение отправленно")
        f.close()
    elif message.text == "вернуть":
        bot.send_message(message.from_user.id, "напиши айди который тебе прислал бот")
        wait_for_command_vernut = True
        wait_for_command_vernut1 = False
    elif wait_for_command_vernut and not wait_for_command_vernut1:
        us = message.text
        us_unshifr = uncyph(us)
        bot.send_message(message.from_user.id, "введи сообщение")
        wait_for_command_vernut = False
        wait_for_command_vernut1 = True
    elif not wait_for_command_vernut and wait_for_command_vernut1:
        target_message_for_vernut = message.text
        f = open('saves.txt', 'r')
        for line in f:
            if str(us_unshifr) in line:
                bot.send_message(line.split()[1], target_message_for_vernut)
                text_for_vozvrat = message.from_user.id
                bot.send_message(line.split()[1], "сообщение написал: " + str(text_for_vozvrat))


# привет я бот анонимка напиши мне имя пользователея и я напишу ему от своего лица твоё сообшение

bot.polling(none_stop=True)

