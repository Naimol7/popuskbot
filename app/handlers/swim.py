from aiogram import Dispatcher, types 
from aiogram.dispatcher.filters import Text 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import requests
import os





class SwimmingStates(StatesGroup):


async def day(message: types.Message, state: FSMContext):
    await 