import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://te.legra.ph/file/3aac366991b4add1942de.jpg https://te.legra.ph/file/81d0ba18954cc4bbe5c2e.jpg https://te.legra.ph/file/da0e9dd08e53511513fe4.jpg https://te.legra.ph/file/f2f7e13c9a892ac71fdbd.jpg https://te.legra.ph/file/8b9650b9ff6d9a7fb9b31.jpg https://te.legra.ph/file/b6605a5e58fe8cbfeb5fc.jpg https://te.legra.ph/file/fd767d900b239dbb546f1.jpg https://te.legra.ph/file/4dce9acec512d1bcdca71.jpg')).split()
PICS_RT = (environ.get('PICS_RT', 'https://te.legra.ph/file/3aac366991b4add1942de.jpg https://te.legra.ph/file/81d0ba18954cc4bbe5c2e.jpg https://te.legra.ph/file/da0e9dd08e53511513fe4.jpg https://te.legra.ph/file/f2f7e13c9a892ac71fdbd.jpg https://te.legra.ph/file/8b9650b9ff6d9a7fb9b31.jpg https://te.legra.ph/file/b6605a5e58fe8cbfeb5fc.jpg https://te.legra.ph/file/fd767d900b239dbb546f1.jpg https://te.legra.ph/file/4dce9acec512d1bcdca71.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUPS')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "hybrid")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'HYBRID_Bots')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>↬ File Name:</b><code> {file_name}</code>\n<b>↬ Size:</b> {file_size}\n\n<code>𝐃𝐨𝐧𝐭 𝐅𝐨𝐫𝐠𝐞𝐭 𝐭𝐨 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐭𝐡𝐞 𝐅𝐢𝐥𝐞 𝐭𝐨 𝐒𝐚𝐯𝐞𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐛𝐞𝐟𝐨𝐫𝐞 𝐃𝐞𝐥𝐞𝐭𝐞.!</code>\n\n\n╭=== • ❰ᴊᴏɪɴ ᴡɪᴛʜ ᴜs❱ • ===➣\n▫️ <b>ᴄʜᴀɴɴᴇʟ :</b><i> @HYBRID_Movies</i>\n▫️ <b>ɢʀᴏᴜᴘ :</b><i> @HYBRID_Movie_Group</i>\n╰======= • ✠ • =======➣")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b><i>➤ Title:</i></b><code> {title}</code>\n<b><i>➤ Release:</i></b> {release_date}\n<b><i>➤ Languages:</i></b> {languages}\n\n<b>☞ Note:</b> ミ★ 𝙏𝙝𝙞𝙨 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙬𝙞𝙡𝙡 𝙗𝙚 𝘼𝙪𝙩𝙤-𝙙𝙚𝙡𝙚𝙩𝙚𝙙 𝙖𝙛𝙩𝙚𝙧 5 𝙈𝙞𝙣𝙪𝙩𝙚𝙨 𝙩𝙤 𝘼𝙫𝙤𝙞𝙙 𝘾𝙤𝙥𝙮𝙧𝙞𝙜𝙝𝙩 𝙄𝙨𝙨𝙪𝙚𝙨 ★彡\n\n<b><i>♤ Requested by</i></b> : {message.from_user.mention}\n\n\n<code>❗️ 1st Join below Channel to Get your Files ❗️</code>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

DELETE_TIME = int(environ.get('DELETE_TIME', 300))
CH_LINK = environ.get('CH_LINK', "")
CH_FILTER = int(environ.get('CH_FILTER', 0))


LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
