import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, add_config_data
from handlers import other_handlers, user_handlers

logger = logging.getLogger(__name__)
# Функция конфигурирования и запуска бота
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s'
               '[%(asctime)s] - %(name)s - %(message)s')
    
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    config: Config = add_config_data()

    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

# Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
