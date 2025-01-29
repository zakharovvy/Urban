import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

with open ('token.txt','r',encoding='UTF8') as file:
    bot_token = file.read()


bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())

Keyb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text= "Информация")
Keyb.add(button1)
Keyb.add(button2)

InlineKeyb = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text = 'Рассчитать норму калорий',callback_data='calories')
button4 = InlineKeyboardButton(text = 'Формулы расчёта',callback_data='formulas')
InlineKeyb.add(button3)
InlineKeyb.add(button4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = ['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = InlineKeyb)

@dp.callback_query_handler(text = ['formulas'])
async def get_formulas(call):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=
        'вариант формулы Миффлина-Сан Жеора: \n'
        'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; \n'
        'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.\n')

@dp.callback_query_handler (text = ['calories'])
async def set_age(call):
    await call.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler (state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age = int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = float(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=float(message.text))
    date = await state.get_data()
    person_age = date ['age']
    person_weight = date['weight']
    person_growth = date ['growth']
    cal_man = (10*person_weight) + (6.25*person_growth) - (5*person_age) + 5
    cal_woman = (10*person_weight) + (6.25*person_growth) - (5*person_age) - 161
    await message.answer(f'Ваша норма калорий {cal_man}, если вы мужчина, или {cal_woman} калорий, если вы женщина')
    await state.finish()

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.', reply_markup = Keyb)

@dp.message_handler (text = ['Информация'])
async def info(message):
    await message.answer(f'Ты сейчас просто так потратил пару секунд своей жизни, а мог бы заработать деняг')
@dp.message_handler()
async def all_massages(message):
    await message.answer(f'Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)