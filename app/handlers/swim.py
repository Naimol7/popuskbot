from aiogram import Dispatcher, types 
from aiogram.dispatcher.filters import Text 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import requests
import os


class SwimmingStates(StatesGroup):
    waitingSex = State()
    waitingStyle = State()
    waitingDistance = State()
    waitingTime = State()
async def start(message: types.Message):
    await message.answer('Введите пол (муж/жен)')
    await SwimmingStates.waitingSex.set()
async def sex(message: types.Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await message.answer('Введите стиль')
    await SwimmingStates.waitingStyle.set()

async def style(message: types.Message, state: FSMContext):
    await state.update_data(style=message.text)
    await message.answer('Введите дистанцию (м)')
    await SwimmingStates.waitingDistance.set()

async def distance(message: types.Message, state: FSMContext):
    await state.update_data(distance=message.text)
    await message.answer('Введите время (мм.сс,мсмс')
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
    dp.register_message_handler(distance, state=SwimmingStates.waitingDistance)
    dp.register_message_handler(time, state=SwimmingStates.waitingTime)
