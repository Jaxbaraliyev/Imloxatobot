import logging
from aiogram import Bot, Dispatcher, executor, types
from checword import checkWords



logging.basicConfig(level=logging.INFO)

bot = Bot(token="#")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    ism = message.from_user.full_name
    await message.answer(f"Assalomu alaykum {ism}.\n So`z kiritng!")

@dp.message_handler(commands=['admin'])
async def admin(message:types.Message):
    admin = "@RAmziddin_17_17"
    await message.answer(f"Admin: {admin}")

@dp.message_handler(commands=['help'])
async def admin(message:types.Message):
    await message.answer("Botimiz faqatgina imloviy xatolarni tekshiradi!")

@dp.message_handler()
async def imlo(message:types.Message):
    word = message.text
    result = checkWords(word)
    if result['available']:
        response = f"✔{word.capitalize()}"
    else:
        response = f"✖{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✔ {text.capitalize()}\n"
    await message.answer(response)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)












