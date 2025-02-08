import telebot
from telebot import types
import time

wait = False
wait1 = False
wait_for_command_vernut = False
wait_for_command_vernut1 = False

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
    bot.send_message(message.from_user.id, "привет я бот анонимка напиши мне любое сообщение и я отправлю это сообщение от своего лица")
    bot.send_message(message.from_user.id,"пример: /anonim @Pechenkapro привет")
    bot.send_message(message.from_user.id, "/anonim отвечает за отправку сообщения анонимно (а по другому не как)")
    bot.send_message(message.from_user.id, "если захочешь вернуть сообщение введи /vernut, айди пользователя и сообщение")
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
    global wait, hid_us, wait1, target_name, target_message, wait_for_command_vernut, wait_for_command_vernut1, us, us_unshifr, target_message_for_vernut
    if message.text == "написать":
        bot.send_message(message.from_user.id, "напиши юзернейм кому ты хочешь написать")
        us = message.from_user.id
        #print(us)
        hid_us = cyph(us)
        #print(message.text)
        wait = True
        wait1 = True
    if message.text != "написать" and wait:
        target_name = message.text
        print(target_name)
        bot.send_message(message.from_user.id, "введи сообщение которое надо отправить")
        wait = False
        wait1 = True
    elif message.text != "введи сообщение которое надо отправить" and message.text != "напиши юзернейм кому ты хочешь написать" and message.text != "написать" and wait == False and wait1:
        target_message = message.text
        f = open('saves.txt', 'r')
        for line in f:
            if target_name in line:
                bot.send_message(line.split()[1], target_message)
                text = "айди отправителя " + str(hid_us)
                bot.send_message(message.from_user.id, text)
        f.close()
    elif message.text == "вернуть":
        bot.send_message(message.from_user.id, "напиши айди который тебе прислал бот")
        wait_for_command_vernut = True
        wait_for_command_vernut1 = False
    elif message.text != "вернуть" and wait_for_command_vernut and message.text != "напиши айди который тебе прислал бот" and wait_for_command_vernut1 == False:
        us = message.text
        us_unshifr = uncyph(us)
        bot.send_message(message.from_user.id, "введи сообщение")
        wait_for_command_vernut = False
        wait_for_command_vernut1 = True
    elif message.text != "введи сообщение" and message.text != "вернуть" and message.text != "напиши айди который тебе прислал бот" and wait_for_command_vernut == False and wait_for_command_vernut1:
        target_message_for_vernut = message.text
        f = open('saves.txt', 'r')
        for line in f:
            if str(us_unshifr) in line:
                bot.send_message(line.split()[1], target_message_for_vernut)


# привет я бот анонимка напиши мне имя пользователея и я напишу ему от своего лица твоё сообшение

bot.polling(none_stop=True)

