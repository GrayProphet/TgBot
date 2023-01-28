import logging
import os
import config
from aiogram import Bot, Dispatcher, executor, types

ribov_list = [1,2,3,4,5,6,7,8,9]
ribov_dict = {"Сайра" : 4, "Семга" : 1, "Язь" : 10}
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot)

HELP_MESSAGE = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/buy</b> - <em>купить рыбов</em>
<b>/add</b> - <em>добавить рыбов</em>
"""


def print_dict (ribov):
    tmp = ""
    for i in ribov:
        tmp += f'{i} : {ribov[i]} \n'
    return tmp



@dp.message_handler(commands=['help'])
async def send_help_command(message: types.Message):
    await bot.send_message(message.chat.id,
                           HELP_MESSAGE,"HTML")

@dp.message_handler(commands=['add'])
async def send_add_command(message: types.Message):
    print(message.chat.id)
    args = message.get_args()
    if message.chat.id != 363739310:
        return await bot.send_message(message.chat.id,
                                      f"Вы не можете добавлять рыбов")

    if not args:
        return await bot.send_message(message.chat.id,
                                      f"Сейчас есть {len(ribov_list)} "
                                      f"рыбов в наличии. Сколько рыбов "
                                      f"вы хотитете добавить?")
    else:
        if args.isdigit():
            args = int(args)
            for i in range(args):
                ribov_list.append(i)
            return await bot.send_message(message.chat.id,
                                          f"Сейчас есть {len(ribov_list)} рыбов в наличии.")

        else:
            return await bot.send_message(message.chat.id,
                                          "Ой кажется вы ввели не "
                                          "верное значение, введите "
                                          "пожалуйста цифру")


@dp.message_handler(commands=['buy'])
async def send_bay_command(message: types.Message):
    args = message.get_args()
    # /buy Язь 3
    args = args.split()

    if not args:
        return await bot.send_message(message.chat.id, f'Вот наш асортимент рыбов\n{print_dict(ribov_dict)}'
                                                       f'Сколько рыбов вы хотите купить?')
    else:
        if args[0] in ribov_dict:
            if ribov_dict[args[0]] == 0:
                return await bot.send_message(message.chat.id,
                                              "Мы сожалеем, но рыбов "
                                              "не осталось, "
                                              "приходите по позже")
            if args[1].isdigit():
                args[1] = int(args[1])
                if args[1] > ribov_dict[args[0]]:
                    return await bot.send_message(message.chat.id,
                                                  "Мы сожалеем, но "
                                                  "рыбов "
                                                  "не хватит поробуйте "
                                                  "ввести "
                                                  "число поменьше")
                else:
                    ribov_dict[args[0]] = ribov_dict[args[0]] - args[1]

                    return await bot.send_message(message.chat.id,
                                                  f"Осталось \n{print_dict(ribov_dict)} рыбов в наличии.")
            else:
                return await bot.send_message(message.chat.id, "Ой кажется вы ввели "
                                                               "не верное значение, "
                                                               "введите пожалуйста цифру")
        else:
            return await bot.send_message(message.chat.id, "Мы сожалем но такой рыбы нет!")


@dp.message_handler(commands=['start'])
async def send_welcome_command(message: types.Message):
    print(message.chat.id)
    return await bot.send_message(message.chat.id, "Данный бот продает рыбов")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)