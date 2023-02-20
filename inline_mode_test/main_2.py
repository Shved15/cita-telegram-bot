from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

import inline_mode_test.keyboards_2 as kb_sel
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
    await message.answer("Let's start the process to save datas for your cita!", reply_markup=kb_sel.ikb_start())
    await message.delete()


@dp.callback_query_handler(kb_sel.cb.filter())
async def selecet_province(callback: types.CallbackQuery, callback_data: dict):
    if callback_data['action'] == 'starts':
        await callback.message.edit_text(text='Please choice the province',
                                         reply_markup=kb_sel.ikb_select_province())
        await callback.answer()
        await ProfileStatesGroup.province.set()


@dp.callback_query_handler(kb_sel.cb.filter(), state=ProfileStatesGroup.province)
async def load_province(callback: types.CallbackQuery, callback_data: dict, state:FSMContext):
    async with state.proxy() as datas:
        datas['province'] = callback.data
    if callback_data['action'] == 'Tarragona':
        await callback.message.edit_text(text='Please choice the department for cita',
                                         reply_markup=kb_sel.ikb_select_oficina())
        await callback.answer(callback_data['action'])
        await ProfileStatesGroup.next()



@dp.callback_query_handler(kb_sel.cb.filter(), state=ProfileStatesGroup.department)
async def load_department(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    async with state.proxy() as datas:
        datas['department'] = callback.data
    if callback_data['action'] == 'RÍA':
        await callback.message.edit_text(text='Please choice the reason for cita!',
                                         reply_markup=kb_sel.ikb_select_reason_e())
        await callback.answer()
        await ProfileStatesGroup.next()
    else:
        await callback.message.edit_text(text='Please choice the reason for cita!',
                                         reply_markup=kb_sel.ikb_select_reason_p())
        await callback.answer()
        await ProfileStatesGroup.next()


@dp.callback_query_handler(kb_sel.cb.filter(), state=ProfileStatesGroup.reason)
async def load_reason(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    async with state.proxy() as datas:
        datas['reason'] = callback.data
    if callback_data['action'] in choices.tramites_de_extranjeria.values() or choices.tramites_de_policia.values():
        await callback.message.edit_text(text='Please choice the document for identify',
                                         reply_markup=kb_sel.ikb_select_document())
        await callback.answer()
        await ProfileStatesGroup.next()

    else:
        await callback.message.edit_text(text='Please choice the document for identyfy',
                                         reply_markup=kb_sel.ikb_select_document())
        await callback.answer()
        await ProfileStatesGroup.next()


@dp.callback_query_handler(kb_sel.cb.filter(), state=ProfileStatesGroup.document)
async def load_document(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    async with state.proxy() as datas:
        datas['document'] = callback.data
    if callback_data['action'] == 'N.I.E.':
        await callback.message.edit_text(text='Please enter your N.I.E.')
        await callback.answer()
        await ProfileStatesGroup.next()
    elif callback_data['action'] == 'PASAPORTE':
        await callback.message.edit_text(text='Please enter your passport"s data')
        await callback.answer()
        await ProfileStatesGroup.next()
    else:
        await callback.message.edit_text(text='In this province can"t use this document, please, choice other document',
                                         reply_markup=kb_sel.ikb_select_document())
        await callback.answer()


@dp.edited_message_handler(lambda message: not len(message.text) < 15 or len(message.text) <= 1, state=ProfileStatesGroup.numb_doc)
async def check_number_of_doc(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Please enter correct data of document!")
    next_id = message.message_id
    await message.delete(next_id)
    await message.delete()


@dp.message_handler(state=ProfileStatesGroup.numb_doc)
async def load_number_of_doc(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['numb_doc'] = message.text
    await message.edit_text(text='Please, enter your name and sername')
    await ProfileStatesGroup.next()
    await message.delete()


# @dp.message_handler(lambda message: not len(message.text) < 50 or len(message.text) <= 1, state=ProfileStatesGroup.name_sername)
# async def check_name_sername(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text="Please enter correct name and sername!")
#     await message.delete()


# @dp.message_handler(state=ProfileStatesGroup.name_sername)
# async def load_name_sername(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['name_sername'] = message.text
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Please, enter your year of birth')
#     await ProfileStatesGroup.next()
#     await message.delete()


# @dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) < 1910, state=ProfileStatesGroup.age)
# async def check_age(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text="Please enter correct the year of birth!")
#     await message.delete()


# @dp.message_handler(state=ProfileStatesGroup.age)
# async def load_age(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['age'] = message.text
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Please, choice your citizenship',
#                            reply_markup=kb_sel.kb_select_citizenship())
#     await ProfileStatesGroup.next()
#     await message.delete()


# @dp.message_handler(Text(equals=choices.name_citizenship), state=ProfileStatesGroup.nation)
# async def load_citizenship(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['nation'] = message.text
#     if message.text in choices.name_citizenship:
#         await bot.send_message(chat_id=message.from_user.id,
#         text=f"Your datas for cita\n\n{data['province']}\n{data['department']}\n{data['reason']}\n{data['numb_doc']}\n{data['name_sername']}\n{data['age']}\n{data['nation']}\n\nHas been save", reply_markup=ReplyKeyboardRemove())
#     await message.reply('Your datas for cita has been save!')
#     await state.finish()
#     await message.delete()

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
