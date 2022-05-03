from aiogram import Dispatcher, types

async def echo(message: types.Message):
    print(message)
    await message.answer(message.text)

def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(echo, content_types=types.message.ContentType.TEXT)