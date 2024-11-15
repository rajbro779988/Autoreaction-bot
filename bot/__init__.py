from pyrogram import Client
from logging import getLogger
from logging.config import dictConfig
from .config import Telegram, LOGGER_CONFIG_JSON
from aiohttp import web
from route import web_server

dictConfig(LOGGER_CONFIG_JSON)

version = 0.3
logger = getLogger('bot')

TelegramBot = Client(
    name="bot",
    api_id=Telegram.API_ID,
    api_hash=Telegram.API_HASH,
    bot_token=Telegram.BOT_TOKEN,
    plugins={'root': 'bot/plugins'}
) 

app = web.AppRunner(await web_server())
await app.setup()
bind_address = "0.0.0.0"
await web.TCPSite(app, bind_address, 8080).start()      
print(f'Bot Started...🍃')

app = TelegramBot()
app.run()
