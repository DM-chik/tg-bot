from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
from dotenv import load_dotenv
import os



load_dotenv()
bot_token = os.getenv('TOKEN')
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет')