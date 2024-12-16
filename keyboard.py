
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_reg = KeyboardButton(text='Регистрация')
button_info = KeyboardButton(text='Информация')
button_form = KeyboardButton(text='Рассчитать')
button_buy = KeyboardButton(text='Купить')
kb.row(button_reg, button_info)
kb.add(button_form, button_buy)

Inline = InlineKeyboardMarkup(resize_keyboard=True)
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data="calories")
button_formulas = InlineKeyboardButton(text='Формулы расчета', callback_data="formulas")
Inline.row(button_calories, button_formulas)

Inline2 = InlineKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
Inline2.row(button1, button2, button3, button4)
