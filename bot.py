from create_bot import bot, dp
from aiogram.utils import executor

def add_handlers():
    from app.handlers.swim import register_by_swimming_handlers
    register_by_swimming_handlers(dp)

if __name__ == "__main__":
    add_handlers()
    executor.start_polling(dp, skip_updates=True)