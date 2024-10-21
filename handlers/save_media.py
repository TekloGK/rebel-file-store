import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client, enums
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

def generate_random_alphanumeric():
    """Generate a random 8-letter alphanumeric string."""
    characters = string.ascii_letters + string.digits
    random_chars = ''.join(random.choice(characters) for _ in range(8))
    return random_chars

def get_short(url):
    rget = requests.get(f"https://{Config.SHORTLINK_URL}/api?api={Config.SHORTLINK_API}&url={url}&alias={generate_random_alphanumeric()}")
    rjson = rget.json()
    if rjson["status"] == "success" or rget.status_code == 200:
        return rjson["shortenedUrl"]
    else:
        return url

    
async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.value > 45:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await forward_to_channel(bot, message, editable)

async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list):
    try:
        if editable.reply_to_message.from_user.id not in Config.OTHER_USERS_CAN_SAVE_FILE:
            await editable.reply_text("You are not authorized to save files.")
            return

        message_ids_str = ""
        for message_id in message_ids:
            message = await bot.get_messages(chat_id=editable.chat.id, message_ids=message_id)
            sent_message = await forward_to_channel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.id)} "
            await asyncio.sleep(2)
        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Delete Batch", callback_data="closeMessage")
            ]])
        )
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=PredatorHackerzZ_{str_to_b64(str(SaveMessage.id))}"
        txt = f"""**Batch Files Stored ✅, Here Is The Link Of Batch Files:**\n\n `{share_link}` \n\n**Or Click Below Buttons To Get Files 😎**"""
        buttons = [
            [InlineKeyboardButton("Link", url=share_link)],
            [InlineKeyboardButton("Movie Channel", url=f"https://t.me/{Config.MOVIE_CHANNEL}"),
            InlineKeyboardButton("Movie Group", url=f"https://t.me/{Config.MOVIE_GROUP}")]
        ]
        if Config.SHORTLINK:
           short_link = get_short(share_link)
           buttons.insert(1, [InlineKeyboardButton("Short Link", url=short_link)])
        await editable.edit(text=txt, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True, parse_mode=enums.ParseMode.MARKDOWN)
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) Got Batch Link!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )


async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    try:
        if message.from_user.id not in Config.OTHER_USERS_CAN_SAVE_FILE:
            await editable.reply_text("You are not authorized to save files.")
            return
        forwarded_msg = await message.forward(Config.DB_CHANNEL)
        file_er_id = str(forwarded_msg.id)
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
            disable_web_page_preview=True)
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=PredatorHackerzZ_{str_to_b64(file_er_id)}"
        txt = f"""**Single Files Stored ✅, Here Is The Link Of Single File:** \n\n`{share_link}` \n\n**Or Click Below Buttons To Get Files 😎**"""
        buttons = [
            [InlineKeyboardButton("Link", url=share_link)],
            [InlineKeyboardButton("Movie Channel", url=f"https://t.me/{Config.MOVIE_CHANNEL}"),
            InlineKeyboardButton("Movie Group", url=f"https://t.me/{Config.MOVIE_GROUP}")]
        ]
        if Config.SHORTLINK:
           short_link = get_short(share_link)
           buttons.insert(1, [InlineKeyboardButton("Short Link", url=short_link)])
        await editable.edit(txt, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True, parse_mode=enums.ParseMode.MARKDOWN)
    except FloodWait as sl:
        if sl.value > 45:
            print(f"Sleep of {sl.value}s caused by FloodWait ...")
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text="#FloodWait:\n"
                     f"Got FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await save_media_in_channel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text="#ERROR_TRACEBACK:\n"
                 f"Got Error from `{str(editable.chat.id)}` !!\n\n"
                 f"**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
