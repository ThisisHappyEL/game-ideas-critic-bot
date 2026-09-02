# 🎮 Game Idea Critic Bot (AI Telegram Bot)

Telegram-бот на базе искусственного интеллекта (LLM), выступающий в роли токсичного и циничного игрового продюсера. Пользователь предлагает идею для видеоигры, а бот критикует её слабые стороны и предлагает способы монетизации.

## 🛠 Стек технологий
* **Python 3.11+**
* **aiogram 3.x** — современный асинхронный фреймворк для Telegram Bot API
* **GigaChat API (Сбер)** — интеграция с LLM
* **python-dotenv** — безопасное управление переменными окружения
* **asyncio / aiohttp** — асинхронная обработка запросов

## 🚀 Основные возможности
* Асинхронный опрос серверов (Long Polling) с обработкой chat actions (индикация «печатает...»).
* Интеграция с нейросетью через системный промпт (Prompt Engineering).
* Динамический резолвинг доступных моделей LLM.
* Обработка исключений и кастомных сетевых сценариев (SSL / Proxy).

## ⚙️ Установка и локальный запуск

1. **Клонируйте репозиторий:**
   git clone https://github.com/ThisisHappyEL/game_ideas_critic_bot.git
   cd game_ideas_critic_bot
  
2. **Создайте и активируйте виртуальное окружение:**
    code
    python -m venv venv

    *Windows:*
    .\venv\Scripts\activate

    *Linux/macOS:*
    source venv/bin/activate

4. **Установите зависимости:**
    pip install -r requirements.txt

5. **Создайте файл .env в корне проекта:**
    BOT_TOKEN=ваш_токен_от_botfather
    GIGACHAT_CREDENTIALS=ваши_авторизационные_данные_gigachat

6. **Запустите бота:**
    python bot.py
