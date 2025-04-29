import asyncio
from aiohttp import web
from telegram import Bot

TOKEN = 'ใส่ Token ของคุณ'
CHANNEL_ID = '@ชื่อช่องของคุณ'

async def send_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text="Hello from the bot!")

async def handle(request):
    return web.Response(text="Bot is running.")

async def main():
    await send_message()

    # Start Web Server
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=10000)
    await site.start()

    # Keep the server running
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
