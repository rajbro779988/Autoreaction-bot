from os import environ as env

class Telegram:
    API_ID = int(env.get("API_ID", "14680661")) #TG API ID
    API_HASH = env.get("API_HASH", "166f6e394021081c5cdb41c92344deb7") #TG API HASH
    BOT_TOKEN = env.get("BOT_TOKEN", "7155858303:AAFgpH-qpBainkm41okcN5UQQ4qlcEX9P-U") #Add Bot Token, get from botfather
    FSUB_ID = int(env.get("FSUB_ID", "-1001710807965"))  #Add Your FSub Channel Id
    FSUB = bool(env.get("FSUB", True)) #Keep True If U Want Force Subscribe 
    SB_PIC = env.get("SB_PIC", "https://i.ibb.co/c6vkVBP/photo-2024-11-15-12-13-41-7437478159336865812.jpg") #Add Link For Start Cmd Pic
    BOT_USERNAME = env.get("BOT_USERNAME", "Sb_reactionbot") #Add Bot Username Without @
    EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🥶", "🤩", "🤮", "💩",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "😡",
        "👅", "🆒", "🖕", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
