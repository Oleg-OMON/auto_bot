import json
import emoji
from aiogram import types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '5674767733:AAGYZcOU431E0FkVHJ-l0A3n3bJApBS4LNs'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

button_p = KeyboardButton('Рулевая рейка')
button_s = KeyboardButton('Рулевая тяга')
button_v = KeyboardButton('Рулевая колонка')

audi = KeyboardButton('Lexus')
Ford = KeyboardButton('Lada')
Volkswagen = KeyboardButton('Volkswagen')

lada_1 = KeyboardButton('2120')
lada_2 = KeyboardButton('2114')
lada_3 = KeyboardButton('2112')

lexus_1 = KeyboardButton('LS')
lexus_2 = KeyboardButton('RX')

kb_cat = ReplyKeyboardMarkup(resize_keyboard=True)
kb_model = ReplyKeyboardMarkup(resize_keyboard=True)
kb_pok = ReplyKeyboardMarkup(resize_keyboard=True)


kb_model.add(audi).add(Ford).add(Volkswagen)
kb_cat.add(button_p).add(button_s).add(button_v)


class FSMSearch(StatesGroup):
    category = State()
    model = State()
    product = State()
    price_two = State()


@dp.message_handler(commands='start', state=None)
async def bot_start(message: types.Message):
    await FSMSearch.category.set()
    await message.reply('Введите категорию', reply_markup=kb_cat)


@dp.message_handler(state=FSMSearch.category)
async def load_category(message: types.Message, state=FSMContext):
    await state.update_data(category=message.text)
    await FSMSearch.next()
    await message.reply('Введите модель', reply_markup=kb_model)


@dp.message_handler(state=FSMSearch.model)
async def load_model(message: types.Message, state=FSMContext):
    await state.update_data(model=message.text)
    await FSMSearch.next()
    data = await state.get_data()
    if data['model'] == 'Lexus':
        kb_pok.add(lexus_1, lexus_2)
        await message.reply('Выберите поколение', reply_markup=kb_pok)
    if data['model'] == 'Lada':
        kb_pok.add(lada_1).add(lada_2).add(lada_3)
        await message.reply('Выберите поколение', reply_markup=kb_pok)


@dp.message_handler(state=FSMSearch.model)
async def load_product(message: types.Message, state=FSMContext):
    await state.update_data(product=message.text)
    await FSMSearch.next()
    data = await state.get_data()

    with open('detail.json') as f:
        d = json.load(f)
        for i in d:
            if (data['category'] in i['mark']) and (data['model'] in i['model']):
                await message.answer('ищу..')
                await message.answer(f"{i['name']}\n"
                                     f"{i['url']}\n"
                                     # f"Цена: {i['price']}{emoji.emojize(' :money_bag:')}"
                                     )

    await state.finish()





# @dp.message_handler(state=FSMSearch.price_two)
# async def load_price_two(message: types.Message, state=FSMContext):
#     await state.update_data(price_two=int(message.text))


if __name__ == '__main__':
    executor.start_polling(dp)
