import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
import asyncio


from test_scrap import scrab_web
from config import TOKEN_API_2

bot = Bot(TOKEN_API_2)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer("I am working", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='Start process')))

@dp.message_handler(Text(equals='Start process'))
async def send_message_info(message: types.Message):
    await message.answer('Please waiting...', reply_markup=ReplyKeyboardRemove())
    scr = scrab_web()
    while True:
        if scr == "Yes":
            await bot.send_message(chat_id=message.from_user.id, text='Yes', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='Stop')))
        await asyncio.sleep(30)

        # @dp.message_handler(Text(equals='Stop'))
        # async def zalupa(message: types.Message):
        #     await message.answer('Ok', reply_markup=ReplyKeyboardRemove())
        # break





if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
