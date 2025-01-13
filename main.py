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
        "14 - Цинк\n",
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
@dp.message(F.text == "11")
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
@dp.message(F.text == "11")
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

