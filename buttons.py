from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


Menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="FAQ"), KeyboardButton(text="Yopiq Kanallar")],
        [KeyboardButton(text="Menejer bilan aloqa"), KeyboardButton(text="Biz haqimizda")],
    ],
    resize_keyboard=True
)




keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📞 Kontaktni yuborish", request_contact=True)]],
    resize_keyboard=True
)

guruhlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="SMM")],
        [KeyboardButton(text="Mobilografiya")],
        [KeyboardButton(text='Buxgalteriya')],
        [KeyboardButton(text='Videografiya')]
    ],
    resize_keyboard=True
)


def buttons_inlane(li):
    tugma = InlineKeyboardBuilder()
    tugma.add(InlineKeyboardButton(text=f"Kanalga qo'shilish", url=li))
    tugma.adjust(1)
    return tugma.as_markup()

malumot = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kanal haqida"), KeyboardButton(text="Kanal qoidalari")],
        [KeyboardButton(text="Obuna xolati"), KeyboardButton(text="Menejerlar bilan aloqa")],
        [KeyboardButton(text="F.A.Q")]
    ]
)

AboutButton = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Web sayt", url="https://www.datatalim.uz/biz-haqimizda"), InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/data_talim_stansiyasi")],
        [InlineKeyboardButton(text="Telegram", url="https://t.me/data_talim_stansiyasi"), InlineKeyboardButton(text="Online ro'yxatdan otish", url="https://www.datatalim.uz/royxatdan-otish")]
    ]
)