import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

logging.basicConfig(level=logging.INFO)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
GIGACHAT_CREDENTIALS = os.getenv("GIGACHAT_CREDENTIALS")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

SYSTEM_PROMPT = """
Ты — суровый, токсичный, но гениальный продюсер видеоигр. 
Пользователь будет предлагать тебе идеи для игр. 
Твоя задача: жестко раскритиковать идею, указать на логические дыры в геймплее или сюжете, 
но в конце обязательно предложить 1-2 циничных способа, как на этом можно заработать кучу денег (монетизация, донат, лутбоксы).
Отвечай кратко, емко, используй сарказм.
"""

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Ну привет. Я главный продюсер этой студии. У тебя есть 30 секунд, чтобы "
        "продать мне свою идею для игры. Пиши, что там у тебя, и я скажу, почему это провалится."
    )

@dp.message()
async def handle_game_idea(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    try:
        async with GigaChat(
            credentials=GIGACHAT_CREDENTIALS,
            verify_ssl_certs=False,
            scope="GIGACHAT_API_PERS"
        ) as giga:
            models_response = await giga.aget_models()
            model_item = models_response.data[0]
            active_model = getattr(model_item, 'name', getattr(model_item, 'id_', 'GigaChat-Pro'))
            logging.info(f"Выбрана модель: {active_model}")

            payload = Chat(
                model=active_model,
                messages=[
                    Messages(role=MessagesRole.SYSTEM, content=SYSTEM_PROMPT),
                    Messages(role=MessagesRole.USER, content=message.text)
                ],
                temperature=0.7,
            )
            response = await giga.achat(payload)
            bot_reply = response.choices[0].message.content
            await message.reply(bot_reply)
            
    except Exception as e:
        logging.error(f"Ошибка API: {e}")
        await message.reply("Мой ассистент сейчас занят, я не могу оценить твою идею. Попробуй позже.")

async def main():
    print("Бот-продюсер запущен и готов разносить идеи!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())