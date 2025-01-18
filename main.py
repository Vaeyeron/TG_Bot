import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

dp = Dispatcher()

async def start_command(message: types.Message) -> None:
    await message.answer(
        "Этот бот предоставляет интерактивные карты запасов и добычи природных ресурсов\n"
        "Выберите ресурс (Введите номер):\n"
        "1 - Нефть\n"
        "2 - Природный газ\n"
        "3 - Уголь\n"
        "4 - Железная руда\n"
        "5 - Уран\n"
        "6 - Марганцевые руды\n"
        "7 - Хромовые руды\n"
        "8 - Бокситы\n"
        "9 - Нефелиновые руды\n"
        "10 - Медь\n"
        "11 - Никель\n"
        "12 - Кобальт\n"
        "13 - Свинец\n"
        "14 - Цинк\n"
        "15 - Олово\n"
        "16 - Вольфрам\n"
        "17 - Молибден\n"
        "18 - Титан\n"
        "19 - Цирконий\n"
        "20 - Литий\n"
        "21 - Редкоземельные металлы\n"
        "22 - Скандий\n"
        "23 - Золото\n"
        "24 - Серебро\n"
        "25 - Платиноиды\n"
        "26 - Алмазы\n"
        "27 - Графит\n"
        "28 - Апатитовые руды\n"
        "29 - Фосфоритовые руды\n"
        "30 - Калийные соли\n"
        "31 - Плавиковый шпат\n"
        "32 - Цементное сырьё",
        reply_markup=types.ReplyKeyboardRemove()
    )

#"1 - Нефть"
@dp.message(F.text == "1")
async def oil(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы нефти"), types.KeyboardButton(text="Добыча нефти")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы нефти")
    async def oil_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/sTFXf/1/")

    @dp.message(F.text == "Добыча нефти")
    async def oil_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/7MpOL/3/")





#"2 - Природный газ"
@dp.message(F.text == "2")
async def gas(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы газа"), types.KeyboardButton(text="Добыча газа")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы газа")
    async def gas_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/GtVXT/2/")

    @dp.message(F.text == "Добыча газа")
    async def gas_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/Ruakl/1/")




#3 - Уголь
@dp.message(F.text == "3")
async def coil(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы угля"), types.KeyboardButton(text="Добыча угля")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы угля")
    async def coil_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/Qvp52/2/")

    @dp.message(F.text == "Добыча угля")
    async def coil_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/0ejBn/1/")





#4 - Железная руда
@dp.message(F.text == "4")
async def iron(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы железных руд"), types.KeyboardButton(text="Добыча железных руд")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы железных руд")
    async def iron_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/Lh5Y8/1/")

    @dp.message(F.text == "Добыча железных руд")
    async def iron_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/qwsUF/1/")





#5 - Уран
@dp.message(F.text == "5")
async def uranium(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы урана"), types.KeyboardButton(text="Добыча урана")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы урана")
    async def uranium_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/6kw4r/1/")

    @dp.message(F.text == "Добыча урана")
    async def uranium_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/yAsaP/1/")





#6 - Марганцевые руды
@dp.message(F.text == "6")
async def manganese(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы марганцевых руд"), types.KeyboardButton(text="Добыча марганцевых руд")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы марганцевых руд")
    async def manganese_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/FUv2Z/1/")

    @dp.message(F.text == "Добыча марганцевых руд")
    async def manganese_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/SwKQK/1/")





#7 - Хромовые руды
@dp.message(F.text == "7")
async def chrome(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы хромовых руд"), types.KeyboardButton(text="Добыча хромовых руд")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы хромовых руд")
    async def chrome_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/8CgZ9/1/")

    @dp.message(F.text == "Добыча хромовых руд")
    async def chrome_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/dVReA/1/")





#8 - Бокситы
@dp.message(F.text == "8")
async def bauxite(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы бокситов"), types.KeyboardButton(text="Добыча бокситов")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы бокситов")
    async def bauxite_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/LcqL5/1/")

    @dp.message(F.text == "Добыча бокситов")
    async def bauxite_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/wxHvl/1/")






#9 - Нефелиновые руды
@dp.message(F.text == "9")
async def nepheline(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы нефелиновых руд"), types.KeyboardButton(text="Добыча нефелиновых руд")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы нефелиновых руд")
    async def nepheline_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/oHytr/1/")

    @dp.message(F.text == "Добыча нефелиновых руд")
    async def nepheline_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/ye2Tu/1/")





#10 - Медь
@dp.message(F.text == "10")
async def copper(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы меди"), types.KeyboardButton(text="Добыча меди")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы меди")
    async def copper_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/Gc465/1/")

    @dp.message(F.text == "Добыча меди")
    async def copper_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/V7W7l/1/")





#11 - Никель
@dp.message(F.text == "11")
async def nickel(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы никеля"), types.KeyboardButton(text="Добыча никеля")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы никеля")
    async def nickel_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/MTuyn/1/")

    @dp.message(F.text == "Добыча никеля")
    async def nickel_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/9txGM/2/")





#12 - Кобальт
@dp.message(F.text == "12")
async def cobalt(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы кобальта"), types.KeyboardButton(text="Добыча кобальта")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы кобальта")
    async def cobalt_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/UhhkY/1/")

    @dp.message(F.text == "Добыча кобальта")
    async def cobalt_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/O7X8g/1/")





#13 - Свинец
@dp.message(F.text == "13")
async def lead(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы свинца"), types.KeyboardButton(text="Добыча свинца")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы свинца")
    async def lead_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/dqwwk/1/")

    @dp.message(F.text == "Добыча свинца")
    async def lead_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/Rl0In/1/")





#14 - Цинк
@dp.message(F.text == "14")
async def zinc(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы цинка"), types.KeyboardButton(text="Добыча цинка")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы цинка")
    async def zinc_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/gnace/1/")

    @dp.message(F.text == "Добыча цинка")
    async def zinc_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/1ZEg4/1/")





#15 - Олово
@dp.message(F.text == "15")
async def tin(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы олова"), types.KeyboardButton(text="Добыча олова")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы олова")
    async def tin_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/EkRJk/1/")

    @dp.message(F.text == "Добыча олова")
    async def tin_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/V30UE/1/")





#16 - Вольфрам
@dp.message(F.text == "16")
async def tungsten(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы вольфрама"), types.KeyboardButton(text="Добыча вольфрама")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы вольфрама")
    async def tungsten_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/g618s/1/")

    @dp.message(F.text == "Добыча вольфрама")
    async def tungsten_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/VMBOP/1/")





#17 - Молибден
@dp.message(F.text == "17")
async def molybdenum(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы молибдена"), types.KeyboardButton(text="Добыча молибдена")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы молибдена")
    async def molybdenum_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/UxCyB/1/")

    @dp.message(F.text == "Добыча молибдена")
    async def molybdenum_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/dYcPB/1/")





#18 - Титан
@dp.message(F.text == "18")
async def tytanium(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы титана"), types.KeyboardButton(text="Добыча титана")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы титана")
    async def tytanium_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/zTbQb/1/")

    @dp.message(F.text == "Добыча титана")
    async def tytanium_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/kL7Ge/1/")





#19 - Цирконий
@dp.message(F.text == "19")
async def zirconium(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы циркония"), types.KeyboardButton(text="Добыча циркония")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы циркония")
    async def zirconium_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/ia1mb/1/")

    @dp.message(F.text == "Добыча циркония")
    async def zirconium_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/gcC3P/1/")





#20 - Литий
@dp.message(F.text == "20")
async def lithium(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы лития"), types.KeyboardButton(text="Добыча лития")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы лития")
    async def lithium_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/Pph19/1/")

    @dp.message(F.text == "Добыча лития")
    async def lithium_mining(message: types.Message):
        await message.answer("В России не ведется промышленная добыча лития")





#21 - редкоземельные металлы
@dp.message(F.text == "21")
async def raremetal(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы редкоземельных металлов"), types.KeyboardButton(text="Добыча редкоземельных металлов")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы редкоземельных металлов")
    async def raremetal_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/UYnKi/1/")

    @dp.message(F.text == "Добыча редкоземельных металлов")
    async def raremetal_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/ChGW2/1/")





#22 - скандий
@dp.message(F.text == "22")
async def scandium(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы скандия"), types.KeyboardButton(text="Добыча скандия")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы скандия")
    async def scandium_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/eVvPU/1/")

    @dp.message(F.text == "Добыча скандия")
    async def scandium_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/wVS1Q/1/")





#23 - золото
@dp.message(F.text == "23")
async def gold(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы золота"), types.KeyboardButton(text="Добыча золота")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы золота")
    async def gold_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/HgIvs/1/")

    @dp.message(F.text == "Добыча золота")
    async def gold_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/ACIJ0/1/")





#24 - Серебро
@dp.message(F.text == "24")
async def silver(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы серебра"), types.KeyboardButton(text="Добыча серебра")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы серебра")
    async def silver_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/PNVH6/1/")

    @dp.message(F.text == "Добыча серебра")
    async def silver_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/w6iKR/1/")





#25 - платиноиды
@dp.message(F.text == "25")
async def platinum(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы платиноидов"), types.KeyboardButton(text="Добыча платиноидов")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы платиноидов")
    async def platinum_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/saY8t/1/")

    @dp.message(F.text == "Добыча платиноидов")
    async def platinum_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/5KRHv/1/")





#26 - алмазы
@dp.message(F.text == "26")
async def diamond(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы алмазов"), types.KeyboardButton(text="Добыча алмазов")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы алмазов")
    async def diamond_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/lJr3M/1/")

    @dp.message(F.text == "Добыча алмазов")
    async def diamond_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/l9Hkx/1/")





#27 - графит
@dp.message(F.text == "27")
async def graphite(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы графита"), types.KeyboardButton(text="Добыча графита")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы графита")
    async def graphite_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/ZZThZ/1/")

    @dp.message(F.text == "Добыча графита")
    async def graphite_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/2hTzR/1/")





#28 - апатитовые руды
@dp.message(F.text == "28")
async def apatites(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы апатитовых руд"), types.KeyboardButton(text="Добыча апатитовых руд")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы апатитовых руд")
    async def apatites_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/Pjm4R/1/")

    @dp.message(F.text == "Добыча апатитовых руд")
    async def apatites_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/5vkFD/1/")





#29 - Фосфоритовые руды
@dp.message(F.text == "29")
async def phosphorites(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы фосфоритовых руд"), types.KeyboardButton(text="Добыча фосфоритовых руд")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы фосфоритовых руд")
    async def phosphorites_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/dwjms/1/")

    @dp.message(F.text == "Добыча фосфоритовых руд")
    async def phosphorites_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/QHXv0/1/")





#30 - калийные соли
@dp.message(F.text == "30")
async def potassiumsalts(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы калийных солей"), types.KeyboardButton(text="Добыча калийных солей")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы калийных солей")
    async def potassiumsalts_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/jae2A/1/")

    @dp.message(F.text == "Добыча калийных солей")
    async def potassiumsalts_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/0MU9j/1/")





#31 - Плавиковый шпат
@dp.message(F.text == "31")
async def fluorspar(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запасы плавикового шпата"), types.KeyboardButton(text="Добыча плавикового шпата")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вы хотите получить статистику запасов или добычи?", reply_markup=keyboard)

    @dp.message(F.text == "Запасы плавикового шпата")
    async def fluorspar_reserves(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/lSkmx/1/")

    @dp.message(F.text == "Добыча плавикового шпата")
    async def fluorspar_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/2WVlT/1/")





#32 - Цементное сырьё
@dp.message(F.text == "32")
async def cement(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Добыча цементного сырья")],
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Статистика добычи", reply_markup=keyboard)

    @dp.message(F.text == "Добыча цементного сырья")
    async def cement_mining(message: types.Message):
        await message.answer("https://datawrapper.dwcdn.net/PN0dq/1/")



@dp.message(F.text == "Назад")
async def back_to_start(message: types.Message):
    await start_command(message)

async def main() -> None:
    token = "7892302309:AAHD8ulB9P126MuH1pxfKXs9iY0UEcCDvbM"
    bot = Bot(token=token)

    dp.message.register(start_command, Command(commands=["start"]))

    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

