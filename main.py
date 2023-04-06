from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.dispatcher.filters import Text
import my_command
import os

api_key = '5448201870:AAEIeJ46pycDp_Wqd5DYghExQa6gka6gNIc'
bot = Bot(api_key)
dp = Dispatcher(bot)
#my_command.creation_my_database()


"""@dp.message_handler(commands=['старт'])
async def command_start(message: types.Message):
    # Функция реагирующая на команду старт
    time_day = my_command.command_start_time()
    answer_bot = my_command.read_database(time_day)
    button_1 = KeyboardButton('/Прогноз_погоды' + ' ' + '🌞' + '/' + '☔️', request_location=True)
    button_2 = KeyboardButton('/Курс_валют' + ' ' + '💵')
    button_3 = KeyboardButton('/Калькулятор' + ' ' + '🧮')
    button_4 = KeyboardButton('/График_работы' + ' ' + '📆')
    my_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    my_keyboard.add(button_1).add(button_2).add(button_3).add(button_4)
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEGRBhjYA4xka-yXYefwFxA97eyqsBblwACGg0AArUgEEvhdD6mKGXvgyoE")
    await bot.send_message(message.from_user.id, f'<em>{answer_bot}</em>', parse_mode="HTML", reply_markup=my_keyboard)"""

button_1 = KeyboardButton(text='Прогноз погоды')
button_2 = KeyboardButton(text='Курс валют')
button_3 = KeyboardButton(text='Минск Транспорт', web_app=WebAppInfo(url='https://yandex.ru/maps/157/minsk/transport'))
button_3_1 = KeyboardButton(text='ANEKDOT.RU', web_app=WebAppInfo(url='https://www.anekdot.ru/last/mem'))
my_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
my_keyboard.add(button_1).add(button_2).add(button_3).add(button_3_1)
button_4 = KeyboardButton(text='Обновить местоположение', request_location=True)
button_5 = KeyboardButton(text='YANDEX')
button_6 = KeyboardButton(text='OpenWeather')
button_7 = KeyboardButton(text='Главное меню')
my_keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
my_keyboard_2.add(button_4).row(button_5, button_6).add(button_7)


@dp.message_handler(commands=['старт'])
async def command_start(message: types.Message):
    """Функция реагирующая на команду старт"""
    await bot.send_message(message.from_user.id, 'Привет !!!', reply_markup=my_keyboard)


@dp.message_handler(text='Прогноз погоды')
async def weather_forecast(message: types.Message):
    """Функция реагирующая на кнопку Прогноз погоды"""
    await bot.send_message(message.from_user.id, 'Обнови местоположение', reply_markup=my_keyboard_2)


@dp.message_handler(content_types=['location'])
async def location(message):
    global latitude, longitude
    if message.location is not None:
        my_location = message.location
        await message.delete()
        latitude = my_location['latitude']
        longitude = my_location['longitude']


@dp.message_handler(text=['YANDEX'])
async def exchange_rates(message: types.Message):
    global latitude, longitude
    print(latitude, longitude)
    query_result = my_command.parser_yandex_weather(latitude, longitude)
    my_command.creating_picture(query_result)
    await bot.send_photo(message.from_user.id, types.InputFile('1.jpg'))
    os.remove('1.jpg')


@dp.message_handler(text=['OpenWeather'])
async def exchange_rates(message: types.Message):
    global latitude, longitude
    print(latitude, longitude)
    query_result = my_command.parser_yandex_weather(latitude, longitude)
    my_command.creating_picture(query_result)
    await bot.send_photo(message.from_user.id, types.InputFile('1.jpg'))
    os.remove('1.jpg')


@dp.message_handler(text=['Курс валют'])
async def exchange_rates(message: types.Message):
    my_command.creating_picture_currency()
    await bot.send_photo(message.from_user.id, types.InputFile('1.jpg'))
    os.remove('1.jpg')


@dp.message_handler(text='Главное меню')
async def command_start(message: types.Message):
    """Функция реагирующая на кнопку Главное меню"""
    await bot.send_message(message.from_user.id, 'Выход в главное меню', reply_markup=my_keyboard)


@dp.message_handler()
async def error_response(message: types.Message):
    """Функция реагирующая на неизвестную команду"""
    error_response = 'Господи, дай мне силы, чтобы справиться с тем, \n что я могу сделать, \n' \
                     'дай мне мужество, чтобы смириться с тем, \n чего я не могу сделать, \n ' \
                     'и дай мне мудрость, чтобы отличить одно от другого !!!'
    await message.reply('Такую команду , я не знаю' + ' ' + '🤔')
    await message.answer(f'<b>{error_response}</b>' + ' ' + '🤔', parse_mode="HTML")


if __name__ == '__main__':
    latitude = '53.915581'
    longitude = '27.662505'
    executor.start_polling(dp, skip_updates=True)
