from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
import data_web_for_bot as choices


cb = CallbackData('ikb', 'action')


def ikb_start() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(InlineKeyboardButton(text='Start the process!', callback_data=cb.new('starts')))
    return ikb


def kb_cancel() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton(text="Reset all settings!"))
    return kb


def ikb_select_province() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for province in choices.names_of_provinces:
        ikb = ikb.add(InlineKeyboardButton(text=f"{province}", callback_data=cb.new(f"{province}")))
    return ikb


def ikb_select_oficina() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for department in choices.choice_tramite:
        ikb = ikb.add(InlineKeyboardButton(text=f"{department}", callback_data=cb.new(f"{department[-3:]}")))
    return ikb


def ikb_select_reason_e() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    for key, value in choices.tramites_de_extranjeria.items():
        ikb = ikb.add(InlineKeyboardButton(text=f"{key}", callback_data=cb.new(f"{value}")))
    return ikb


def ikb_select_reason_p() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    for key, value in choices.tramites_de_policia.items():
        ikb = ikb.add(InlineKeyboardButton(text=f"{key}", callback_data=cb.new(f"{value}")))
    return ikb


def ikb_select_document() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for document in choices.choice_documents:
        ikb = ikb.add(InlineKeyboardButton(text=f"{document}", callback_data=cb.new(f"{document}")))
    return ikb

def ikb_select_citizenship() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for nation in choices.name_citizenship:
        ikb = ikb.add(InlineKeyboardButton(text=f"{nation}", callback_data=cb.new(f"{nation}")))
    return ikb

def ikb_next() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=input(), callback_data=cb.new(input()))]
    ])
    return ikb


def ikb_correct() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Enter correct datas', callback_data=cb.new('correct'))]
    ])
    return ikb
