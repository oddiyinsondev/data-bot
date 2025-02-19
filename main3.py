import asyncio
import logging
from config import token, admin
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from data import KantakQosh, KantakOqish
from buttons import keyboard, guruhlar, buttons_inlane
import time
import requests

# Telegram bot kanallari
smm1 = -1002264165151
mblografiya = -1002405625404
bugalter = -1002375726826

# Sheets API URL
sheet_api_url = "https://sheetdb.io/api/v1/wa33txehgmlyx"

bot = Bot(token=token)
dp = Dispatcher()
router = Router()
logging.basicConfig(level=logging.INFO)
dp.include_router(router)

class UserState(StatesGroup):
    ism1 = State()
    waiting_for_contact = State()

class Reklama(StatesGroup):
    yubor = State()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        f"Assalomu alaykum !\nIsm familyangizni to'liq yozing: ",
    )
    await state.set_state(UserState.ism1)


@router.message(UserState.ism1, F.text)
async def process_contact(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await message.answer(f"Rahmat {ism}, endi telefon raqamingizni yuboring.\n\nIltimos, telefon raqamingizni tugmani bosish orqali yuboring", reply_markup=keyboard)
    await state.set_state(UserState.waiting_for_contact)


@router.message(UserState.waiting_for_contact)
async def process_contact(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    user_id = message.from_user.id
    username = message.from_user.username
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer("Telefoningiz qabul qilindi !")
    
    # Telefon raqami va Telegram IDni bazaga qo'shish yoki yangilash
    KantakQosh(user_id=user_id, username=username, fullname=ism, contact=phone)
    time.sleep(2)
    
    await message.answer("Qaysi yopiq kanalimizga qo'shilmoqchisiz ?\n\nPastdagi tugma orqali belgilang !", reply_markup=guruhlar)
    await state.clear()


@router.message(F.text)
async def process_contact(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_data = {
        "telegram id": user_id,
        "username": username,
        "SMM": "null",
        "Mobilografiya": "null",
        "Buxgalteriya": "null",
        "Telefon nomer": "null"
    }

    # Tanlangan bo'limni yangilash
    if message.text == "SMM":
        user_data["SMM"] = "TRUE"
        chat = await bot.get_chat(smm1)
        invite_link = await bot.create_chat_invite_link(chat.id, member_limit=1)
        await message.answer(f"SMM kanaliga xush kelibsiz! \n\n🔗 Kanalga qo'shilish uchun: {invite_link.invite_link}", disable_web_page_preview=True, reply_markup=buttons_inlane(li=invite_link.invite_link))
    
    elif message.text == "Mobilografiya":
        user_data["Mobilografiya"] = "TRUE"
        chat = await bot.get_chat(mblografiya)
        invite_link = await bot.create_chat_invite_link(chat.id, member_limit=1)
        await message.answer(f"Mobilografiya kanaliga xush kelibsiz! \n\n🔗 Kanalga qo'shilish uchun: {invite_link.invite_link}", disable_web_page_preview=True, reply_markup=buttons_inlane(li=invite_link.invite_link))
    
    elif message.text == "Buxgalteriya":
        user_data["Buxgalteriya"] = "TRUE"
        chat = await bot.get_chat(bugalter)
        invite_link = await bot.create_chat_invite_link(chat.id, member_limit=1)
        await message.answer(f"Buxgalteriya kanaliga xush kelibsiz! \n\n🔗 Kanalga qo'shilish uchun: {invite_link.invite_link}", disable_web_page_preview=True, reply_markup=buttons_inlane(li=invite_link.invite_link))
    
    else:
        await message.answer("Iltimos, to'g'ri bo'limni tanlang: SMM, Mobilografiya yoki Buxgalteriya")

    # Sheets ma'lumotlarini yangilash
    # POST request bilan yangilash: telefon va kanalga tegishli bo'limni "TRUE" qiling
    response = requests.get(f"https://sheetdb.io/api/v1/wa33txehgmlyx?telegram_id={user_id}")
    
    if response.status_code == 200:
        data = response.json()
        if data:
            row_id = data[0]["id"]
            update_data = {
                "SMM": user_data["SMM"],
                "Mobilografiya": user_data["Mobilografiya"],
                "Buxgalteriya": user_data["Buxgalteriya"]
            }
            # Data yangilandi
            update_response = requests.put(f"https://sheetdb.io/api/v1/wa33txehgmlyx/{row_id}", json=update_data)
            if update_response.status_code == 200:
                await message.answer("Sizning tanlovlaringiz muvaffaqiyatli yangilandi!")
        else:
            # Agar foydalanuvchi yangi bo'lsa, yangi ma'lumot qo'shish
            post_data = {
                "telegram id": user_data["telegram id"],
                "username": user_data["username"],
                "Ism Familya": "Unknown",  # Ism va familya kiritilishi kerak
                "Telefon nomer": "Unknown"  # Telefon raqami kiritilishi kerak
            }
            post_response = requests.post("https://sheetdb.io/api/v1/wa33txehgmlyx", json=post_data)
            if post_response.status_code == 200:
                await message.answer("Yangi ma'lumotlar Sheets'ga muvaffaqiyatli qo'shildi!")
    else:
        await message.answer("Ma'lumotlarni yangilashda xato yuz berdi.")

async def main():
    await bot.send_message(chat_id=admin[1], text="bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
