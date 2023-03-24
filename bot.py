import logging

from aiogram import Bot, Dispatcher, executor, types

from random import randint

from decouple import config

API_TOKEN = config('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def get_reply(file_name):
    with open(file_name, 'r', encoding='utf-8') as fl:
        replies = fl.readlines()
        return replies[randint(0, len(replies) - 1)]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm BrainBot!\nPowered by aiogram. Send 'Hi!' to continue")

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Hi!':
        await message.answer("Hi again!\nYou can ask next questions:\nHow are you?\nWhat is the weather like today?\nWhat is your name?\nHow old are you?\nWhat time is it?")
    elif message.text == 'How are you?':
        await message.answer(get_reply('replies\howAreYou.txt')) 
    elif message.text == 'What is the weather like today?':
        await message.answer(get_reply('replies\weather.txt'))
    elif message.text == 'What is your name?':
        await message.answer(get_reply('replies/names.txt'))
    elif message.text == 'How old are you?':
        await message.answer(get_reply('replies\days.txt'))
    elif message.text == 'What time is it?':
        await message.answer(get_reply('replies/time.txt'))
    else:
        await message.answer('Please, repeat one of the questions exactly')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)