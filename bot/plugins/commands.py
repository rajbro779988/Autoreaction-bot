from pyrogram import filters, enums
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
    return await msg.reply_photo(
        photo=tg.SB_PIC,
        caption=WelcomeText % {'first_name': msg.from_user.first_name if msg.from_user else 'Anonymous'}
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆', url=f'https://telegram.me/{tg.BOT_USERNAME}?startgroup=botstart')
                ],
                [
                    InlineKeyboardButton(text='• ᴜᴩᴅᴀᴛᴇꜱ •', url='https://t.me/SB_Botz_Update'),
                    InlineKeyboardButton(text='• ꜱᴜᴩᴩᴏʀᴛ •', url='https://t.me/+Vegv963Nf2kzYzBl')
                ],
                [
                    InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆', url=f'https://telegram.me/{tg.BOT_USERNAME}?startchannel=botstart')
                ]
            ]
        ),
        parse_mode=enums.ParseMode.HTML
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
                    InlineKeyboardButton(text='👨‍💻 ᴜᴩᴅᴀᴛᴇꜱ', url='https://t.me/SB_Botz_Update'),
                    InlineKeyboardButton(text='💥 ꜱᴜᴩᴩᴏʀᴛ', url='https://t.me/+Vegv963Nf2kzYzBl')
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
 
