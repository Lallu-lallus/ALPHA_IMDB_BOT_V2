# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Messages
START_MSG = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press follwing buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = 'Please join @.... to use this bot'import re

import os

from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information

SESSION = environ.get('SESSION', 'LuciferMoringstar_Robot')

API_ID = int(environ['API_ID'])

API_HASH = environ['API_HASH']

BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings

CACHE_TIME = int(environ.get('CACHE_TIME', 300))

USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", ""))

ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "").split())

DB_URL = os.environ.get("DATABASE_1", "")

BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]

CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]

auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]

AUTH_USERS = (auth_users + ADMINS) if auth_users else []

auth_channel = environ.get('FORCES_SUB')

AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

TUTORIAL = "https://youtu.be/5hnYOKBzyi8"

# MongoDB information

DATABASE_URI = environ['DATABASE_2']

DATABASE_NAME = environ['BOT_NAME']

COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages

default_start_msg = """

**Hi, I'm Auto Filter V3**

Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.

"""

START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")

OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")

if FILE_CAPTION.strip() == "":

    CUSTOM_FILE_CAPTION=None

else:

    CUSTOM_FILE_CAPTION=FILE_CAPTION

if OMDB_API_KEY.strip() == "":

    API_KEY=None

else:

    API_KEY=OMDB_API_KEY
