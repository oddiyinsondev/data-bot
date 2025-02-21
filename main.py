import asyncio
import logging
from config import token, admin
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from data import KantakQosh, KantakOqish, SMMoqish, SMMQosh, BugalterQosh, Bugolteroqish, Videooqish, VideoQosh, Moboqish, MobQosh, KantakOqish1, smm_text, videograf_text, bugalter_text, mob_text
from buttons import keyboard, guruhlar, buttons_inlane, Menyu, AboutButton
import time
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

smm1 = -1002264165151
mblografiya = -1002405625404
bugalter = -1002375726826
vidoegraf = -1002369778312

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
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
    user_id = message.from_user.id
    if KantakOqish1(user_id):
        await message.answer("Siz allaqachon ro'yxatdan o'tgansiz!", reply_markup=Menyu)
    else:
        await message.answer(
            f"Assalomu alaykum !\nIsm familyangizni to'liq yozing: ",
        )
        await state.set_state(UserState.ism1)

@router.message(Command("reklama"), F.from_user.id.in_(admin))
async def ReklamaBot(message: Message, state: FSMContext):
    await state.set_state(Reklama.yubor)
    await message.answer("Postingizni yuboring")

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
    KantakQosh(user_id=user_id, username=username, fullname=ism, contact=phone)
    time.sleep(2)
    await message.answer("Qaysi yopiq kanalimizga qo'shilmoqchisiz ?\n\nPastdagi tugma orqali belgilang !", reply_markup=guruhlar)
    await state.clear()




@router.message(Reklama.yubor)
async def YuborishBot(message: Message, state: FSMContext):
    malumotlar = KantakOqish()
    for id in malumotlar:
        await message.send_copy(chat_id=id[0])
    await message.answer("Malumotlar yuborildi")




@router.message(F.text)
async def process_contact(message: Message):
    user_id = message.from_user.id
    if message.text == "SMM":
        if not SMMoqish(user_id=user_id):
            SMMQosh(user_id=user_id, name=message.text)
        chat = await bot.get_chat(smm1)
        invite_link = await bot.create_chat_invite_link(chat_id=chat.id, member_limit=1)
        text = smm_text
        await message.answer(text, disable_web_page_preview=True, reply_markup=buttons_inlane(li=invite_link.invite_link))
        await message.answer("Asosiy menyudasiz", reply_markup=Menyu)
    elif message.text == "Mobilografiya":
        if not Moboqish(user_id=user_id):
            MobQosh(user_id=user_id, name=message.text)
        chat = await bot.get_chat(mblografiya)
        invite_link = await bot.create_chat_invite_link(chat_id=chat.id, member_limit=1)
        await message.answer(mob_text, disable_web_page_preview=True, reply_markup=buttons_inlane(li=invite_link.invite_link))
        await message.answer("Asosiy menyudasiz", reply_markup=Menyu)
    elif message.text == "Buxgalteriya":
        if not Bugolteroqish(user_id):
            BugalterQosh(user_id=user_id, name=message.text)
        chat = await bot.get_chat(bugalter)
        invite_link = await bot.create_chat_invite_link(chat_id=chat.id, member_limit=1)
        await message.answer(bugalter_text, disable_web_page_preview=True, reply_markup=buttons_inlane(li=invite_link.invite_link))
        await message.answer("Asosiy menyudasiz", reply_markup=Menyu)
    elif message.text == "Videografiya":
        if not Videooqish(user_id):
            VideoQosh(user_id=user_id, name=message.text)
        chat = await bot.get_chat(vidoegraf)
        invite_link = await bot.create_chat_invite_link(chat_id=chat.id, member_limit=1)
        await message.answer(videograf_text, disable_web_page_preview=True, reply_markup=buttons_inlane(li=invite_link.invite_link))
        await message.answer("Asosiy menyudasiz", reply_markup=Menyu) 
    elif message.text == "FAQ":
        await message.answer("Botga tez beriladigan savollar <a href='https://docs.google.com/document/d/1j1mk4hieEd7lANTie1ZMV5ium5SCEchgiilT4IinJxE'>savollar</a>", parse_mode="HTML")
    elif message.text == "Menejer bilan aloqa":
        await message.answer("Menejer bilan aloqa\n☎️ 62-227-72-22\nAdmin: @DATA_menejer",reply_markup=Menyu)
    elif message.text == "Biz haqimizda":
        await message.answer(f"Data Talim stansiyasiga xush kelibsiz", reply_markup=AboutButton)
    elif message.text == "Yopiq Kanallar":
        await message.answer("Yopiq kanalni tanlang!", reply_markup=guruhlar)
    else:
        await message.answer("Xato text")



async def main():
    await bot.send_message(chat_id=admin[1], text="bot ishga tushdi")
    await dp.start_polling(bot) 

if __name__ == "__main__":
    asyncio.run(main())