
import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", 26162072))
	API_HASH = os.environ.get("API_HASH", "ba25181c01b50d945748801b6c8b6ecc")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "7909023072:AAHcQ2k1ZubhzQFTFo-twxHy754oKCOh0XE")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Filmone_FileStore_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", -1002430476193))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', 'linkshortx.in')
	SHORTLINK_API = os.environ.get('SHORTLINK_API', '5094176751ade91b32057828a07d3dd49650c196')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", 7538143921))
	DATABASE_URL = os.environ.get("DATABASE_URL", 'mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority')
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "Filmone_Backup")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", -1002452358035)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "6805001741, 7538143921, 6717382350").split(",") if id.strip()]
	MOVIE_CHANNEL = os.environ.get('MOVIE_CHANNEL', 'Filmone_Theaters')
	MOVIE_GROUP = os.environ.get('MOVIE_GROUP', 'Filmone_Request')
	SHORTLINK = os.environ.get("SHORTLINK", False)
	OWNER_USERNAME = os.environ.get('OWNER_USERNAME', 'Stylish_Star2')
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Koyeb](https://koyeb.com)
│
├🔸 **Developer:** [Mr.Smile](https://t.me/talk2smile_bot) 
│
├🔸 **Movie Channel:** [Movie Channel]({MOVIE_CHANNEL})
│
╰──────[ 😎 ]───────────⍟
"""
	
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
