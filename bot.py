from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
bot_token = os.getenv('TOKEN')
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я твой первый бот на aiogram! ✨")


@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = """
    Доступные команды:
    /start - Начать работу
    /help - Помощь
    /hello - Приветствие
    """
    await message.answer(help_text)


@dp.message()
async def echo(message: Message):
    await message.answer(f"Вы написали: {message.text}")


async def main():
    print("Бот запущен! 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

