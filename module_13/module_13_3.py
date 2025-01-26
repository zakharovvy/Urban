import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

with open ('token.txt','r',encoding='UTF8') as file:
    bot_token = file.read()


bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
    await message.answer(f'Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)