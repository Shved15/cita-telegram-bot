from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

import keyboards as kb_sel
import data_web_for_bot as choices
from config import TOKEN_API


storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    province = State()
    department = State()
    reason = State()
    document = State()
    numb_doc = State()
    name_sername = State()
    age = State()
    nation = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer("Let's start the process to save datas for your cita!", reply_markup=kb_sel.kb_start())
    await message.delete()


@dp.message_handler(Text(equals='Start the process!'))
async def selecet_province(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text='Please choice the province',
                           reply_markup=kb_sel.kb_select_province())
    await message.delete()
    await ProfileStatesGroup.province.set()


@dp.message_handler(Text(equals=choices.names_of_provinces), state=ProfileStatesGroup.province)
async def load_province(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['province'] = message.text
    if message.text == 'Tarragona':
        await bot.send_message(chat_id=message.from_user.id,
                               text='Please choice the department for cita',
                               reply_markup=kb_sel.kb_select_oficina())
        await ProfileStatesGroup.next()
        await message.delete()


@dp.message_handler(Text(equals=choices.choice_tramite), state=ProfileStatesGroup.department)
async def load_department(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['department'] = message.text
    if message.text == 'TRÁMITES OFICINAS DE EXTRANJERÍA':
        await bot.send_message(chat_id=message.from_user.id,
                               text='Please choice the reason for cita!',
                               reply_markup=kb_sel.kb_select_reason_e())
        await ProfileStatesGroup.next()
        await message.delete()
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Please choice the reason for cita!',
                               reply_markup=kb_sel.kb_select_reason_p())
        await ProfileStatesGroup.next()
        await message.delete()


@dp.message_handler(Text(equals=choices.tramites_all), state=ProfileStatesGroup.reason)
async def load_reason(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['reason'] = message.text
    if message.text in choices.tramites_de_extranjeria:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Please choice the document for identify',
                               reply_markup=kb_sel.kb_select_document())
        await ProfileStatesGroup.next()
        await message.delete()
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Please choice the document for identyfy',
                               reply_markup=kb_sel.kb_select_document())
        await ProfileStatesGroup.next()
        await message.delete()


@dp.message_handler(Text(equals=choices.choice_documents), state=ProfileStatesGroup.document)
async def load_document(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['document'] = message.text
    if message.text == 'N.I.E.':
        await bot.send_message(chat_id=message.from_user.id,
                               text='Please enter your N.I.E.',
                               reply_markup=ReplyKeyboardRemove())
        await ProfileStatesGroup.next()
        await message.delete()
    elif message.text == 'PASAPORTE':
        await bot.send_message(chat_id=message.from_user.id,
                               text='Please enter your passport"s data',
                               reply_markup=ReplyKeyboardRemove())
        await ProfileStatesGroup.next()
        await message.delete()
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text='In this province can"t use this document, please, choice other document',
                               reply_markup=kb_sel.kb_select_document())
        await message.delete()


@dp.message_handler(lambda message: not len(message.text) < 15 or len(message.text) <= 1, state=ProfileStatesGroup.numb_doc)
async def check_number_of_doc(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Please enter correct data of document!")
    await message.delete()


@dp.message_handler(state=ProfileStatesGroup.numb_doc)
async def load_number_of_doc(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['numb_doc'] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text='Please, enter your name and sername')
    await ProfileStatesGroup.next()
    await message.delete()


@dp.message_handler(lambda message: not len(message.text) < 50 or len(message.text) <= 1, state=ProfileStatesGroup.name_sername)
async def check_name_sername(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Please enter correct name and sername!")
    await message.delete()


@dp.message_handler(state=ProfileStatesGroup.name_sername)
async def load_name_sername(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name_sername'] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text='Please, enter your year of birth')
    await ProfileStatesGroup.next()
    await message.delete()


@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) < 1910, state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Please enter correct the year of birth!")
    await message.delete()


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text='Please, choice your citizenship',
                           reply_markup=kb_sel.kb_select_citizenship())
    await ProfileStatesGroup.next()
    await message.delete()


@dp.message_handler(Text(equals=choices.name_citizenship), state=ProfileStatesGroup.nation)
async def load_citizenship(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nation'] = message.text
    if message.text in choices.name_citizenship:
        await bot.send_message(chat_id=message.from_user.id,
        text=f"Your datas for cita\n\n{data['province']}\n{data['department']}\n{data['reason']}\n{data['numb_doc']}\n{data['name_sername']}\n{data['age']}\n{data['nation']}\n\nHas been save", reply_markup=ReplyKeyboardRemove())
    await message.reply('Your datas for cita has been save!')
    await state.finish()
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
