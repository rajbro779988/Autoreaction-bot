from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import TelegramBot
from bot.config import Telegram as tg
from bot.static import *
from bot.plugins.fsub import get_fsub

@TelegramBot.on_message(
    filters.command('start')
    & (
        filters.private |
        filters.group
    )
)
async def start_command(_, msg: Message):
    if tg.FSUB:
        client = _
        message = msg
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    return await msg.reply(
        text=WelcomeText % {'first_name': msg.from_user.first_name if msg.from_user else 'Anonymous'},
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆', url=f'https://telegram.me/{Telegram.BOT_USERNAME}?startgroup=botstart')
                ],
                [
                    InlineKeyboardButton(text='• ᴜᴩᴅᴀᴛᴇꜱ •', url='https://telegram.me/RahulReviewsYT'),
                    InlineKeyboardButton(text='• ꜱᴜᴩᴩᴏʀᴛ •', url='https://telegram.me/CodeXSupport')
                ],
                [
                    InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆', url=f'https://telegram.me/{Telegram.BOT_USERNAME}?startchannel=botstart')
                ]
            ]
        )
    )

@TelegramBot.on_message(
    filters.command('help')
    & (
        filters.private |
        filters.group
    )
)
async def send_emojis(_, msg: Message):
    if tg.FSUB:
        client = _
        message = msg
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    return await msg.reply(
        text=Help,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='👨‍💻 ᴏᴡɴᴇʀ', url='https://telegram.me/CodeXBro'),
                    InlineKeyboardButton(text='💥 ʀᴇᴘᴏ', url='https://github.com/CodeXBots/Auto-Reaction-Bot')
                ]
            ]
        )
    )
