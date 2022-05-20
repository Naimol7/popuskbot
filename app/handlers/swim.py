from aiogram import Dispatcher, types 
from aiogram.dispatcher.filters import Text 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import requests
import os
import requests
import json

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
v1 = KeyboardButton(text='М')
v2 = KeyboardButton(text='Ж')
menu_kb.add(v1, v2)

menu_kb2 = ReplyKeyboardMarkup(resize_keyboard=True)


class SwimmingStates(StatesGroup):
    waitingSex = State()
    waitingStyle = State()
    waitingDistance = State()
    waitingTime = State()

async def menu1(message: types.Message):
    menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    v1 = KeyboardButton(text='М')
    v2 = KeyboardButton(text='Ж')
    menu_kb.add(v1, v2)
    await message.answer('Main.menu', reply_markup=menu_kb)

async def start(message: types.Message):
    await message.answer('Введите пол', reply_markup=menu_kb)
    await SwimmingStates.waitingSex.set()



async def sex(message: types.Message, state: FSMContext):
    if message.text not in ('Ж','М'):
        await message.answer("Вы ввели что-то неправильно", reply_markup=menu_kb)
    else:
        await state.update_data(sex=message.text)
        r = requests.get(url='http://192.168.1.120:5000/getstyles')
        styles_list = json.loads(r.text)
        print([i['name'] for i in styles_list])
        menu_kb2.add(*[i['name'] for i in styles_list] )
        await message.answer('Введите стиль', reply_markup=menu_kb2)
        await SwimmingStates.waitingStyle.set()

async def style(message: types.Message, state: FSMContext):
    if message.text not in ('Вольный','Спина','Брасс', 'Баттерфляй','Комплекс'):
        await message.answer("Вы ввели что-то неправильно", reply_markup=menu_kb)
    else:
        await state.update_data(style=message.text)
        await message.answer('Введите дистанцию (м)')
        if message.text == 'Вольный':
            await SwimmingStates.waitingDistance1.set()
        if message.text == 'Спина':
            await SwimmingStates.waitingDistance2.set()
        if message.text == 'Брасс':
            await SwimmingStates.waitingDistance3.set()
        if message.text == 'Баттерфляй':
            await SwimmingStates.waitingDistance4.set()
        if message.text == 'Комплекс':
            await SwimmingStates.waitingDistance5.set()

async def distance1(message: types.Message, state: FSMContext):

    await state.update_data(distance=message.text)
    await message.answer('Введите время (мм.сс,мсмс)')
    await SwimmingStates.waitingTime.set()

async def time(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    user_data = await state.get_data()
    # await message.answer(user_data)
    # array = list(user_data.values())
    sex = user_data['sex']
    style = user_data['style']
    distance = user_data['distance']
    # time = user_data['time']
    await message.answer(sex, style, distance)
    

def register_by_swimming_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*')
    dp.register_message_handler(sex, state=SwimmingStates.waitingSex)
    dp.register_message_handler(style, state=SwimmingStates.waitingStyle)
    # dp.register_message_handler(distance, state=SwimmingStates.waitingDistance)
    dp.register_message_handler(time, state=SwimmingStates.waitingTime)
