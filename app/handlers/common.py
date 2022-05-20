from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup


# async def menu(message: types.Message):
#     menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
#     v1 = KeyboardButton(text='пытик')
#     v2 = KeyboardButton(text='пытёночек')
#     v3 = KeyboardButton(text='пытёныш')
#     menu_kb.add(v1, v2, v3)

#     inline_menu_kb = InlineKeyboardMarkup()
#     b1 = InlineKeyboardButton(text='1', callback_data='callback1')
#     b2 = InlineKeyboardButton(text='2', callback_data='callback2')
#     b3 = InlineKeyboardButton(text='3', callback_data='callback3')
#     inline_menu_kb.add(b1,b2,b3)
    
#     await message.answer('Main.menu', reply_markup=inline_menu_kb)

    

async def callback_handler(message: types.Message):
    if message.data == 'callback1':
        await message.answer('1')
    if message.data == 'callback2':
        await message.answer('2')
    if message.data == 'callback3':
        await message.answer('3')

# async def v3(message: types.Message):
#     await message.answer('пытик')
# async def v2(message: types.Message):
#     await message.answer('пытёночек')
# async def v1(message: types.Message):
#     await message.answer('пытёныш')




# async def echo(message: types.Message):
#     print(message)
#     await message.answer(message.text)

def register_common_handlers(dp: Dispatcher):
    # dp.register_message_handler(echo, content_types=types.message.ContentType.TEXT)
    dp.register_message_handler(menu, commands='menu', state='*')
    dp.register_message_handler(v3, Text(equals='пытик', ignore_case=True))
    dp.register_message_handler(v2, Text(equals='пытёночек', ignore_case=True))
    dp.register_message_handler(v1, Text(equals='пытёныш', ignore_case=True))
    dp.register_callback_query_handler(callback_handler)