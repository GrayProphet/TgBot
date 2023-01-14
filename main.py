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
<b>/buy</b> - <em>купить рыбов</em>
"""


@dp.message_handler(commands=['help'])
async def send_help_command(message: types.Message):
    await bot.send_message(message.chat.id, HELP_MESSAGE, "HTML")


@dp.message_handler(commands=['buy'])
async def send_bay_command(message: types.Message):
    args = message.get_args()
    if len(ribov_list) == 0:
        return await bot.send_message(message.chat.id,
                                      "Мы сожалеем, но рыбов не осталось, приходите по позже")
    if not args:
        await bot.send_message(message.chat.id,
                               f"Сейчас есть {len(ribov_list)} рыбов в наличии. Сколько рыбов вы хотитете?")
    else:
        if args.isdigit():
            args = int(args)
            if args > len(ribov_list):
                return await bot.send_message(message.chat.id,
                                              "Мы сожалеем, но рыбов не хватит поробуйте ввести число поменьше")
            else:
                for i in range(args):
                    print(i)
                    ribov_list.pop()
                await bot.send_message(message.chat.id, f"Осталось {len(ribov_list)} рыбов в наличии.")
        else:
            return await bot.send_message(message.chat.id, "Ой кажется вы ввели не верное значение, введите пожалуйста цифру")


@dp.message_handler(commands=['start'])
async def send_welcome_command(message: types.Message):
    await bot.send_message(message.chat.id, "Данный бот продает рыбов")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)