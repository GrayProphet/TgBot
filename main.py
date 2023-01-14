import logging
import config
from aiogram import Bot, Dispatcher, executor, types
ribov_list = [1,2,3,4,5,6,7,8,9]
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=config.token)
dp = Dispatcher(bot)

HELP_MESSAGE =  """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/bay</b> - <em>купить рыбов</em>
"""
@dp.message_handler(commands=['help'])
async def send_help_command(message: types.Message):
    await bot.send_message(message.chat.id, HELP_MESSAGE,"HTML")


@dp.message_handler(commands=['bay'])
async def send_bay_command(message: types.Message):
    await bot.send_message(message.chat.id, f"Сейчас есть {len(ribov_list)} рыбов в наличии. Сколько рыбов вы хотитете?")

@dp.message_handler(commands=['start'])
async def send_welcome_command(message: types.Message):
    await bot.send_message(message.chat.id, "Данный бот продает рыбов")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)