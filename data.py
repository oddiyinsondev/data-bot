import sqlite3


def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username text,
        full_name TEXT,
        phone_number TEXT
    )
    ''')
    conn.commit()
    conn.close()


def KantakQosh(user_id, username, fullname, contact):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT OR REPLACE INTO users (user_id, username, full_name, phone_number) 
    VALUES (?, ?, ?, ?)
    ''', (user_id, username, fullname, contact))
    conn.commit()
    conn.close()

def KantakOqish1(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    malumot = cursor.fetchone()
    conn.close()
    return malumot

def KantakOqish():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("select * from users")
    malumot = cursor.fetchall()
    conn.close()
    return malumot



def TestQosh(user_id, username, fullname, contact, smm='null', mob='null', bugalter='null', video='null'):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT into kurslar(user_id, username, full_name, phone_number, smm, mobile, bugalter, video) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, username, fullname, contact, smm, mob, bugalter, video))
    conn.commit()
    conn.close()



def SMMQosh(user_id, name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO smm (user_id, name) 
    VALUES (?, ?)
    ''', (user_id, name))
    conn.commit()
    conn.close()

def BugalterQosh(user_id, name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO Bugalter (user_id, name) 
    VALUES (?, ?)
    ''', (user_id, name))
    conn.commit()
    conn.close()

def VideoQosh(user_id, name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO video (user_id, name) 
    VALUES (?, ?)
    ''', (user_id, name))
    conn.commit()
    conn.close()

def MobQosh(user_id, name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO MOB (user_id, name) 
    VALUES (?, ?)
    ''', (user_id, name))
    conn.commit()
    conn.close()


def Videooqish(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("select * from video where user_id=?", (user_id, ))
    malumot = cursor.fetchone()
    conn.close()
    return malumot

def SMMoqish(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("select * from SMM where user_id=?", (user_id, ))
    malumot = cursor.fetchone()
    conn.close()
    return malumot

def Moboqish(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("select * from MOB where user_id=?", (user_id, ))
    malumot = cursor.fetchone()
    conn.close()
    return malumot

def Bugolteroqish(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("select * from Bugalter where user_id=?", (user_id, ))
    malumot = cursor.fetchone()
    conn.close()
    return malumot


smm_text = """🚀 SMM Yopiq Kanaliga Xush Kelibsiz!

Bu yerda siz SMM sohasida kuchli mutaxassis bo‘lish va shaxsiy brendingizni rivojlantirish uchun eng muhim bilimlarga ega bo‘lasiz!

🎯 Yopiq kanalning asosiy maqsadi:
SMM sohasida rivojlanishni xohlagan har bir kishi uchun maxsus tajriba almashish maydonini yaratish. Bu yerda siz ilg‘or bilimlarni o‘rganib, ularni amaliyotda qo‘llash imkoniyatiga ega bo‘lasiz.

🔥 SMM mutaxassisi bo‘lish uchun 3 asosiy omil mavjud:
1️⃣ Kuchli shaxsiyat – O‘z uslubingiz va strategiyangizni yaratish.
2️⃣ Kuchli mutaxassislik – Algoritmlar, trendlar va ilg‘or texnikalarni mukammal o‘zlashtirish.
3️⃣ Sifatli kontent – Raqobatchilardan ajralib turish uchun professional yondashuv.

📌 Kanalda sizni nima kutmoqda?
✅ Har kuni foydali bilim va SMM bo‘yicha eng so‘nggi yangiliklar
✅ Eksklyuziv video darslar va sifatli kontent yaratish bo‘yicha maslahatlar
✅ Eng kuchli SMM mutaxassislari bilan yopiq podkastlar va onlayn suhbatlar
✅ Amaliy strategiyalar va real misollar

💡 Raqobatda oldinga chiqishni xohlaysizmi? Unda sizga kerakli bo‘lgan barcha bilimlar shu yerda jamlangan! 🚀

🔗 Kanalga qo'shilish uchun bir martalik havola:"""

mob_text = """📱📸 Mobilagrafiya Yopiq Kanaliga Xush Kelibsiz!  

Bu yerda sizni quyidagi foydali materiallar kutmoqda:  

✅ Top Sound Effektlar – Eng yaxshi resurslar va saytlar  
🎞 Futajlar – Yangi va sifatli mobil videolar uchun materiallar  
🎓 Bepul Tutoriallar – Mobilagrafiya va videografiya bo‘yicha darsliklar  
🎨 Ikonkalar – Dizayningizni yanada jozibador qiladigan elementlar  
🌐 Foydali Websaytlar – Mobilagrafiya va videografiya uchun kerakli manbalar  
🎥 Syomka bo‘yicha maslahatlar – Professional video olish sirlarini o‘rganing  
🚀 Yangiliklar va Trendlar – Sohadagi eng so‘nggi o‘zgarishlar  
🤖 AI vositalari – Sun’iy intellekt bilan videolar yaratish  

🎯 Bizning maqsadimiz – Sizga mobilagrafiya va videografiya sohasida kerakli barcha bilim va tajribalarni yetkazish, shuningdek, bu sohadan daromad olishga yordam berish!  

📩 Kanalga qo‘shiling va orzularingiz sari birinchi qadamni tashlang! 🚀"""

bugalter_text = """📊📚 Buxgalteriya Yopiq Kanaliga Xush Kelibsiz!  

Bu yerda sizni quyidagi foydali materiallar kutmoqda:  

📌 Qonunchilik yangiliklari – Soliq va buxgalteriya sohasidagi o‘zgarishlardan xabardor bo‘ling  
📊 Moliyaviy hisobotlar – To‘g‘ri va samarali hisobot tayyorlash bo‘yicha qo‘llanmalar  
💡 Buxgalteriya sir-asrorlari – Ishingizni osonlashtiradigan tavsiyalar va lifehacklar  
📆 Muddatlar va majburiyatlar – Soliq va moliyaviy hisobot topshirish sanalari  
📑 Hujjatlar shablonlari – Buxgalterlar uchun kerakli tayyor namuna hujjatlar  
🖥 Dasturlar va servislar – 1C, Excel va boshqa muhim dasturlar bo‘yicha foydali materiallar  
📈 Tahlil va prognozlar – Moliyaviy tahlil qilish va biznesni rejalashtirish bo‘yicha maslahatlar  

🎯 Bizning maqsadimiz – Sizga buxgalteriya sohasida mustahkam bilim berish va ish jarayoningizni yengillashtirish!  

📩 Kanalga qo‘shiling va professional buxgalter sifatida o‘sishda bir qadam oldinda bo‘ling! 🚀"""


videograf_text = """🚀 Videografiya Yopiq Kanaliga Xush Kelibsiz!

Bu yerda siz videografiya sohasida kuchli mutaxassis bo‘lish va sifatli videolar yaratish uchun eng muhim bilimlarga ega bo‘lasiz!

🎯 Yopiq kanalning asosiy maqsadi:
Videografiya sohasida rivojlanishni istagan har bir kishi uchun maxsus tajriba almashish maydonini yaratish. Bu yerda siz ilg‘or bilimlarni o‘rganib, ularni amaliyotda qo‘llash imkoniyatiga ega bo‘lasiz.

🔥 Professional videograf bo‘lish uchun 3 asosiy omil:
1️⃣ Texnik mahorat – Kamera sozlamalari, montaj va yorug‘lik ishlatish bo‘yicha mukammal bilim.
2️⃣ Ijodiy yondashuv – Kadr kompozitsiyasi, hikoya qilish va vizual estetika asoslari.
3️⃣ Amaliy tajriba – Real loyihalar ustida ishlash va mustahkam portfolio yaratish.

📌 Kanalda sizni nima kutmoqda?
✅ Har kuni foydali bilim va videografiya bo‘yicha eng so‘nggi yangiliklar
✅ Eksklyuziv video darslar va montaj texnikalari bo‘yicha maslahatlar
✅ Eng kuchli videograf va rejissyorlar bilan yopiq podkastlar va onlayn suhbatlar
✅ Amaliy strategiyalar, real misollar va kreativ yondashuv

💡 Siz ham professional videograf bo‘lishni xohlaysizmi? Unda sizga kerak bo‘lgan barcha bilimlar shu yerda jamlangan! 🎥🚀"""



# def create_smm():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#     CREATE TABLE SMM(
#         user_id INTEGER PRIMARY KEY,
#         name text not null
#     )
#     ''')
#     conn.commit()
#     conn.close()


# def create_mob():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#     CREATE TABLE MOB(
#         user_id INTEGER PRIMARY KEY,
#         name text not null
#     )
#     ''')
#     conn.commit()
#     conn.close()


# def create_Video():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#     CREATE TABLE video(
#         user_id INTEGER PRIMARY KEY,
#         name text not null
#     )
#     ''')
#     conn.commit()
#     conn.close()

# def create_bugalter():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#     CREATE TABLE Bugalter(
#         user_id INTEGER PRIMARY KEY,
#         name text not null
#     )
#     ''')
#     conn.commit()
#     conn.close()

# create_bugalter()
# create_mob()
# create_Video()
# create_smm()

# def CreateTest():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Kurslar (
#         ID INTEGER PRIMARY KEY NOT NULL,
#         user_id INTEGER UNIQUE,
#         username TEXT,
#         full_name TEXT,
#         phone_number TEXT,
#         smm TEXT,
#         mobile TEXT,
#         bugalter TEXT,
#         video TEXT
#     )
#     ''')
#     conn.commit()
#     conn.close()
#     return "test"

# print(CreateTest())
