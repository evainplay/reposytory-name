from telebot import *
import random

bot = telebot.TeleBot('5310946586:AAGlG323cK9yWLzEbCbtq7mH0ImTWgUr-G4')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, чтобы начать играть введи комманду: /play\n\nНо в начале лучше почитай правила:\n\nПравила игры в - Камень Ножницы Бумагу:\nКогда ты напишешь играть то начнется твоя игра с ботом, попробуй победить бота в этой игре :)\nТвоя задача выбрать что ты хочешь использовать против бота, тут список что ты можешь выбрать = (Камень, Ножницы, Бумага)\nВсе это нажимается на кнопках!\nНа этом все удачной игры!\nЧтобы начать играть введи комманду: /play')

@bot.message_handler(commands=['play'])
def kgb_message(message):
    markup = types.InlineKeyboardMarkup()
    k = types.InlineKeyboardButton(text="Камень", callback_data="Камень")
    g = types.InlineKeyboardButton(text="Ножницы", callback_data="Ножницы")
    b = types.InlineKeyboardButton(text="Бумага", callback_data="Бумага")

    markup.add(k, g, b)
    bot.send_message(message.chat.id, "Выберите один из предметов: ", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    city_list = ["Камень", "Ножницы", "Бумага"]
    kgb = random.choice(city_list)

    if call.data == 'Камень':
        bot.answer_callback_query(callback_query_id=call.id, text='Ваш ход принят!')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали: Камень", reply_markup=None)

    elif call.data == 'Ножницы':
        bot.answer_callback_query(callback_query_id=call.id, text='Ваш ход принят!')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали: Ножницы", reply_markup=None)
    elif call.data == 'Бумага':
        bot.answer_callback_query(callback_query_id=call.id, text='Ваш ход принят!')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали: Бумагу", reply_markup=None)

    if call.data == kgb:
        bot.send_message(call.message.chat.id, f"У вас ничья! Бот выбрал: {kgb}\n\nЧто бы начать новую игру напишите: /play")

    elif call.data == "Камень":
        if kgb == "Ножницы":
            bot.send_message(call.message.chat.id, f"Вы победили! Бот выбрал: {kgb}\n\nЧто бы начать новую игру напишите: /play")

        else:
            bot.send_message(call.message.chat.id, f"Вы проиграли! Бот выбрал: {kgb}\n\nЧто бы начать новую игру напишите: /play")

    elif call.data == "Бумага":
        if kgb == "Камень":
            bot.send_message(call.message.chat.id, f"Вы победили! Бот выбрал: {kgb}\n\nЧто бы начать новую игру напишите: /play")

        else:
            bot.send_message(call.message.chat.id, f"Вы проиграли! Бот выбрал: {kgb}\n\nЧто бы начать новую игру напишите: /play")

    elif call.data == "Ножницы":
        if kgb == "Бумага":
            bot.send_message(call.message.chat.id, f"Вы победили! Бот выбрал: {kgb}\n\nЧто бы начать новую игру напишите: /play")

        else:
            bot.send_message(call.message.chat.id, f"Вы проиграли! Бот выбрал: {kgb}\n\nЧто бы начать новую игру напишите: /play")

bot.infinity_polling()