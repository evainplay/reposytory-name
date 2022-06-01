import telebot
from telebot import types
import random

bot = telebot.TeleBot('5310946586:AAGlG323cK9yWLzEbCbtq7mH0ImTWgUr-G4')

items = types.InlineKeyboardMarkup()
k = types.InlineKeyboardButton(text="Камень", callback_data="Камень")
g = types.InlineKeyboardButton(text="Ножницы", callback_data="Ножницы")
b = types.InlineKeyboardButton(text="Бумага", callback_data="Бумага")
items.add(k, g, b)

ask = types.InlineKeyboardMarkup()
y = types.InlineKeyboardButton(text="Да", callback_data="Да")
n = types.InlineKeyboardButton(text="Нет", callback_data="Нет")
ask.add(y, n)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, чтобы начать играть введи команду: /play\n\nНо в начале лучше почитай правила:\n\nПравила игры в - Камень Ножницы Бумагу:\nКогда ты напишешь играть то начнется твоя игра с ботом, попробуй победить бота в этой игре :)\nТвоя задача выбрать что ты хочешь использовать против бота, тут список что ты можешь выбрать = (Камень, Ножницы, Бумага)\nВсе это нажимается на кнопках!\nНа этом все удачной игры!\nЧтобы начать играть введи комманду: /play')


@bot.message_handler(commands=['play'])
def kgb_message(message):
    bot.send_message(message.chat.id, "Выберите один из предметов: ", reply_markup=items)


@bot.callback_query_handler(func=lambda call: call.data in ["Камень", "Ножницы", "Бумага"])
def query_handler(call):
    kgb = random.choice(["Камень", "Ножницы", "Бумага"])

    bot.answer_callback_query(callback_query_id=call.id, text='Ваш ход принят!')
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f"Вы выбрали: {call.data}", reply_markup=None)

    win = {"Камень": "Ножницы", "Ножницы": "Бумага", "Бумага": "Камень"}

    if win[call.data] == kgb:
        bot.send_message(call.message.chat.id, f"Вы победили! Бот выбрал: {kgb}")
    elif call.data == kgb:
        bot.send_message(call.message.chat.id, f"У вас ничья! Бот выбрал: {kgb}")
    else:
        bot.send_message(call.message.chat.id, f"Вы проиграли! Бот выбрал: {kgb}")

    bot.send_message(call.message.chat.id, "Попробовать еще? ", reply_markup=ask)


@bot.callback_query_handler(func=lambda call: call.data in ["Да", "Нет"])
def replay(call):
    if call.data == 'Да':
        bot.answer_callback_query(callback_query_id=call.id, text='Новая игра!')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите один из предметов: ", reply_markup=items)
    else:
        bot.answer_callback_query(callback_query_id=call.id, text='Игра окончена!')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за игру.", reply_markup=None)

bot.infinity_polling()
