import logging
import os

import aiohttp
from aiohttp.client import ContentTypeError

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
from dotenv import load_dotenv

from bot.constants import *
# from buttons import calendar

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

class TaskInput(state.StatesGroup):
    event_name = state.State()
    date = state.State()
    time = state.State()
    location = state.State()
    description = state.State()
    public = state.State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        (
        f'Привет, {message.from_user.username}!!!\n'
        f'Список доступных комманд {COMMANDS_OFFER}\n'
        )
    )
    print(message)

# +++
async def reciver(message: types.Message, state: FSMContext, key: str, bot_answer: str):
    """
    Common function for reciving data and save data to StateGroup.
    Also invites you to take the next step.
    """
    data = {key: message.text}
    await state.update_data(data=data)
    await message.answer(text=bot_answer)
    await TaskInput.next()
# +++

@dp.message_handler(commands=['remindus'])
async def remind_us(message: types.Message, state: FSMContext):
    """Starts reminding script for all group members."""
    await message.answer('Введите название мероприятия')
    await TaskInput.event_name.set()


@dp.message_handler(state=TaskInput.event_name)
async def name_reciver(message: types.Message, state: FSMContext):
    """Recive event name and next step."""
    await state.update_data(public=True)
    await reciver(message, state, 'event_name', 'Введите дату')


@dp.message_handler(state=TaskInput.date)
async def date_reciver(message: types.Message, state: FSMContext):
    """Recive event date and next step."""
    await reciver(message, state, 'event_date', 'Введите время')


@dp.message_handler(state=TaskInput.time)
async def time_reciver(message: types.Message, state: FSMContext):
    """Recive event time and next step."""
    await reciver(message, state, 'event_time', 'Добавте локацию')


@dp.message_handler(state=TaskInput.location)
async def location_reciver(message: types.Message, state: FSMContext):
    """Recive event location and next step."""
    await reciver(message, state, 'event_location', 'Добавте описание')


@dp.message_handler(state=TaskInput.description)
async def description_reciver_and_finish(message: types.Message, state: FSMContext):
    """Recive event description and_script_finish."""
    description = message.text
    await state.update_data(description=description)
    data = await state.get_data()
    await message.answer(text=data)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)