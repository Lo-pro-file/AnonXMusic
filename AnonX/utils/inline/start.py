from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    return [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
    ]


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    return [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(text="❣ sᴜᴩᴩᴏʀᴛ ❣", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="🥀 ᴍᴀɪɴᴛᴀɪɴᴇʀ 🥀", user_id=OWNER),
        ],
        [InlineKeyboardButton(text="✨ sᴏᴜʀᴄᴇ ✨", url=config.UPSTREAM_REPO)],
    ]
