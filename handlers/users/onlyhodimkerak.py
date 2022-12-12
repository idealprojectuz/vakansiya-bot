from aiogram import types
from states.hodimData import Xodimdata
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default.mainKeyboard import mainKeyboard
from keyboards.default.checkkeyoard import checkkeyboard
from creatorimg.image import createimg
from data.config import ADMINS
from keyboards.inline.adminpostingKeyboard import adminMenu
from keyboards.default.additiondatas import additiondatas
# idora nomini so'rash
@dp.message_handler(text="Vakansiya qo'shish")
async def for_hodim(message: types.Message):
    await message.answer('vakansiya joylash uchun ariza berish \n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.')
    await message.answer('🎓 Idora nomi?', reply_markup=ReplyKeyboardRemove())
    await Xodimdata.companyName.set()

#kompaniya nomini so'rash
@dp.message_handler(state=Xodimdata.companyName)
async def answer_idoraname(message: types.Message, state: FSMContext):
    idoranomi = message.text

    await state.update_data(
        {"idora": idoranomi}
    )

    await message.answer("📚<b> Texnologiya: </b>\n\n Talab qilinadigan texnologiyalarni kiriting? \nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#")

    await Xodimdata.next()

#texnologiya nomini so'rash
@dp.message_handler(state=Xodimdata.technologyName)
async def answer_technology(message: types.Message, state: FSMContext):
    technologyName = message.text

    await state.update_data(
        {"tech": technologyName}
    )

    await message.answer("<b> 📞 Aloqa: </b>\n\nBog`lanish uchun raqamingizni kiriting? \nMasalan, +998 90 123 45 67")

    # await PersonalData.email.set()
    await Xodimdata.next()

#masul shaxs telefon raqamini so'rash
@dp.message_handler(state=Xodimdata.phoneNum)
async def answer_phonenum(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )

    await message.answer("📚<b>🌐 Hudud: </b>\n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")

    await Xodimdata.next()

#manzilini so'rash
@dp.message_handler(state=Xodimdata.location)
async def answer_location(message: types.Message, state: FSMContext):
    locations = message.text

    await state.update_data(
        {"location": locations}
    )

    await message.answer("✍️Mas'ul ism sharifi?")

    await Xodimdata.next()
#masul ism sharifi
@dp.message_handler(state=Xodimdata.fullname)
async def answer_name(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {
            "fullname": fullname,
            'username': message.from_user.username
         }
    )
    await message.answer("🕰 <b> Murojaat qilish vaqti:</b>\n\n Qaysi vaqtda murojaat qilish mumkin? \nMasalan, 9:00 - 18:00")
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.murojatvaqti)
async def answer_murojatvaqti(message: types.Message, state: FSMContext):
    murojatvaqti = message.text
    await state.update_data(
        {
            "murojatvaqti": murojatvaqti,
         }
    )
    await message.answer("🕰 Ish vaqtini kiriting?")
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.ishvaqti)
async def answer_ishvaqti(message: types.Message, state: FSMContext):
    ishvaqti = message.text
    await state.update_data(
        {
            "ishvaqti": ishvaqti,
         }
    )
    await message.answer("Kasb nomini kiriting?")
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.kasb)
async def answer_maosh(message: types.Message, state: FSMContext):
    kasb = message.text
    await state.update_data(
        {
            "kasbi": kasb,
         }
    )
    await message.answer("💰 Maoshni kiriting?")
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.maosh)
async def answer_maosh(message: types.Message, state: FSMContext):
    maosh = message.text
    await state.update_data(
        {
            "maosh": maosh,
         }
    )
    await message.answer("‼️ Qo`shimcha ma`lumotlar?", reply_markup=additiondatas)
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.additioninfo)
async def answer_addition(message: types.Message, state: FSMContext):
    additiondata=message.text
    await state.update_data(
        {
            "aditioninfo":additiondata,
        }
    )
    data = await state.get_data()
    idora=data.get('idora')
    tech=data.get('tech')
    phone=data.get('phone')
    location=data.get('location')
    fullname=data.get('fullname')
    username=data.get('username')
    murojatvaqti=data.get('murojatvaqti')
    ishvaqti=data.get('ishvaqti')
    maosh=data.get('maosh')
    kasb=data.get('kasbi')
    qoshimchamalumot=data.get('aditioninfo')

    text=f"<b>Xodim kerak: </b> \n\n🏢 Idora: {idora} \n"
    text+=f"Kasb {kasb} \n"
    text+=f"📚 Texnologiya: <b>{tech} </b>\n"
    text+=f"🇺🇿 Telegram: @{username}\n"
    text+=f"📞 Aloqa: {phone} \n"
    text+= f"🌐 Hudud: {location} \n"
    text+= f"✍️ Mas'ul: {fullname} \n"
    text+=f"🕰 Murojaat vaqti: {murojatvaqti} \n"
    text+= f"🕰 Ish vaqti: {ishvaqti} \n"
    text+=f"💰 Maosh: {maosh} \n"
    if qoshimchamalumot=='Shart emas':
        pass
    else:
        text+=f"‼️ Qo`shimcha: {qoshimchamalumot} \n\n"
    text+=f"<a href='https://t.me/ayti_jobs'>✅ Kanalga obuna bo’lish </a>"

    imageres=createimg(kasb,maosh,idora)
    if imageres:
        with open('creatorimg/result.png', 'rb') as file:
            await message.answer_photo(photo=file.read(), caption=text)
            await message.answer("Ma'lumotlar to'g'rimi", reply_markup=checkkeyboard)
            await Xodimdata.next()
    await state.update_data(
        {
            "allinfo": text,
        }
    )



@dp.message_handler(state=Xodimdata.posting)
async def answer_addition(message: types.Message, state: FSMContext):
    if message.text=='Ha':
        await message.answer("Malumotlaringiz Yuborildi Biz uni ko'rib chiqib Kanalga joylaymiz")
        await message.answer('Yana vakansiya yubormoqchimisiz unda quyidagi tugmani bosing', reply_markup=mainKeyboard)
        for admin in ADMINS:
            try:
                data = await state.get_data()
                text=data['allinfo']
                with open('creatorimg/result.png', 'rb') as file:
                    await dp.bot.send_photo(admin, photo=file.read(), caption=text, reply_markup=adminMenu)
                    await state.finish()
            except Exception as err:
                logging.exception(err)
        pass
    elif message.text=="Yo'q":
        await message.answer('Yana vakansiya yubormoqchimisiz unda quyidagi tugmani bosing', reply_markup=mainKeyboard)
        await state.finish()
    else:
        await message.answer('Bunday buyruq yoq')

