import logging
import config
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.channel_post_handler(content_types=types.ContentType.ANY)
async def forward_post(channel_post: types.message_id):
        msg = await channel_post.forward(config.group, disable_notification=True)
        await msg.pin(disable_notification=True)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, "Я родился!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)