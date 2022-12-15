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
    await message.answer('<b>Vakansiya joylash uchun ariza berish</b> \n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.')
    await message.answer('<b>🎓 Idora nomi: </b>', reply_markup=ReplyKeyboardRemove())
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

    await message.answer(f"<b> 📞 Aloqa: </b>\n\n Bog`lanish uchun raqamingizni yoki <b>telegram usernamini: Masalan @{message.from_user.username}</b> kiritishingiz mumkin ")

    # await PersonalData.email.set()
    await Xodimdata.next()

#masul shaxs telefon raqamini so'rash
@dp.message_handler(state=Xodimdata.phoneNum)
async def answer_phonenum(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )

    await message.answer("<b> 🌐 Hudud: </b>\n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")

    await Xodimdata.next()

#manzilini so'rash
@dp.message_handler(state=Xodimdata.location)
async def answer_location(message: types.Message, state: FSMContext):
    locations = message.text

    await state.update_data(
        {"location": locations}
    )

    await message.answer("<b> ✍️ Mas'ul ism sharifi? </b>")

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
    await message.answer("🕰 <b> Murojaat qilish vaqti:</b>\n\n Qaysi vaqtda murojaat qilish mumkin? \nMasalan, 9:00 - 18:00", reply_markup=additiondatas)
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.murojatvaqti)
async def answer_murojatvaqti(message: types.Message, state: FSMContext):
    murojatvaqti = message.text
    await state.update_data(
        {
            "murojatvaqti": murojatvaqti,
         }
    )
    await message.answer("🕰 Ish vaqtini kiriting?", reply_markup=additiondatas)
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.ishvaqti)
async def answer_ishvaqti(message: types.Message, state: FSMContext):
    ishvaqti = message.text
    await state.update_data(
        {
            "ishvaqti": ishvaqti,
         }
    )
    await message.answer("<b>📝 Kasb nomini kiriting?</b>", reply_markup=ReplyKeyboardRemove())
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.kasb)
async def answer_maosh(message: types.Message, state: FSMContext):
    kasb = message.text
    await state.update_data(
        {
            "kasbi": kasb,
         }
    )
    await message.answer("<b>💰 Maoshni kiriting?</b>")
    await Xodimdata.next()

@dp.message_handler(state=Xodimdata.maosh)
async def answer_maosh(message: types.Message, state: FSMContext):
    maosh = message.text
    await state.update_data(
        {
            "maosh": maosh,
         }
    )
    await message.answer("<b>‼️ Qo`shimcha ma`lumotlar?</b>", reply_markup=additiondatas)
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

    locationlist=location.split()
    texnologiya=tech.split()
    kasbi=kasb.split()
    locationlist[0]=f" #{locationlist[0]} "
    texnologiya[0]=f" #{texnologiya[0]} "
    kasbi[0]=f" #{kasbi[0]} "

    hashtaglar=locationlist[0]
    hashtaglar+=" #".join(texnologiya)
    hashtaglar+=kasbi[0]


    text=f"{hashtaglar} \n\n"
    text+=f"<b>Kasb: {kasb.title()} </b> \n\n🏢 Idora: {idora} \n"
    text+=f"📚 Texnologiya: <b>{tech} </b>\n"
    adminlist=[1167233264,1174153911,913047674]
    
    text+=f"Aloqa: {phone} \n"
    text+= f"🌐 Hudud: {location} \n"
    text+= f"✍️ Mas'ul: {fullname} \n"
    if murojatvaqti=='Shart emas':
        pass
    else:
        text+=f"🕰 Murojaat vaqti: {murojatvaqti} \n"
    if ishvaqti=='Shart emas':
        pass
    else:
        text+= f"🕰 Ish vaqti: {ishvaqti} \n"
    text+=f"💰 Maosh: {maosh} \n\n"
    if qoshimchamalumot=='Shart emas':
        pass
    else:
        text+=f"‼️ Qo`shimcha: {qoshimchamalumot} \n\n"
    text+=f"<a href='https://t.me/ayti_jobs'>✅ Kanalga obuna bo’lish </a> \n"

    imageres=createimg(kasb.title(),maosh,idora)
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
    elif message.text=="Yo'q":
        await message.answer('Yana vakansiya yubormoqchimisiz unda quyidagi tugmani bosing', reply_markup=mainKeyboard)
        await state.finish()
    else:
        await message.answer('Bunday buyruq yoq')

