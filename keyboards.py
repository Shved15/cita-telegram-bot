from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import data_web_for_bot as choices

def kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text='Start the process!'))
    return kb


def kb_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text="Reset all settings!"))
    return kb


def kb_select_province() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for province in choices.names_of_provinces:
        kb = kb.add(KeyboardButton(text=f"{province}"))
    return kb


def kb_select_oficina() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for department in choices.choice_tramite:
        kb = kb.add(KeyboardButton(text=f"{department}"))
    return kb


def kb_select_reason_e() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for reason_e in choices.tramites_de_extranjeria:
        kb = kb.add(KeyboardButton(text=f"{reason_e}"))
    return kb


def kb_select_reason_p() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for reason_p in choices.tramites_de_policia:
        kb = kb.add(KeyboardButton(text=f"{reason_p}"))
    return kb


def kb_select_document() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for document in choices.choice_documents:
        kb = kb.add(KeyboardButton(text=f"{document}"))
    return kb

def kb_select_citizenship() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(row_width=4)
    for nation in choices.name_citizenship:
        kb = kb.add(KeyboardButton(text=f"{nation}"))
    return kb


def ikb_save_pogress() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='OK', callback_data='ok'), InlineKeyboardButton(text='No', callback_data='no')]
    ])
    return ikb
