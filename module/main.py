import re
import uuid
import socket
import platform
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
import os
import random
import logging
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from asyncio import *
import requests
from filmedb.database import Database
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import *
from pyrogram.types import Message

from config import *
from filmedb import Media, unpack_new_file_id

logger = logging.getLogger(__name__)

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        

@Client.on_message(filters.command("start"))
async def start(client, message):
    #return
    chat_id = message.from_user.id
    if not await database.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await database.add_user(chat_id)
        if -1001741009206:
            await client.send_message(
                -1001741009206,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.reply_video("https://telegra.ph/file/64865d56582fa87eba003.mp4", caption=START, reply_markup=ST_BTN)
       
DATABASE_URI=DATABASE_URI
database = Database(DATABASE_URI, "epic_bot") 
    
#•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#State chek

@Client.on_message(filters.command("state") & filters.user(ADMINS))   
async def startprivate(bot, message):
    countb = await database.total_users_count()
    countb = await database.total_users_count()
    count = await bot.get_chat_members_count(-1001620454933)
    counta = await bot.get_chat_members_count(-1001620454933)
    text=f"""**🏅Bot Total Users**
**Members Count In Bot & Chane**
╔═════════════════════════════════════════════╗
   **🌱Chanel Members**  🏅`{count}`
   **⚡Epic App Store Bot Users**  🏅`{countb}`
╚═════════════════════════════════════════════╝
"""
    await bot.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await bot.send_message(message.chat.id, text=text)


ST_BTN = InlineKeyboardMarkup([[
                InlineKeyboardButton('➕ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ➕', url="https://t.me/EpicFilmeBot?startgroup=true")
            ],
            [
                InlineKeyboardButton('࿉ᴍʏ ꜰɪʟᴍ ᴅᴀᴛᴀʙᴀꜱᴇ࿉', url='https://t.me/SinhalaEnglishFilme')
            ],
            [
                InlineKeyboardButton('☑ꜱᴜᴘᴘᴏʀᴛ', url='https://t.me/EpicChats'),
                InlineKeyboardButton('ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ 🇱🇰', url='https://t.me/EpicBotsSl')
            ],
            [
                InlineKeyboardButton('🔄ꜱᴇᴀʀᴄʜ ɪɴʟɪɴᴇ', switch_inline_query_current_chat=''),
                InlineKeyboardButton('ꜱᴡɪᴛʜᴄ ɪɴʟɪɴᴇ ɪɴ ɢʀᴏᴜᴘ◀', switch_inline_query='')
            ]
        ])

STAT_STICKER = ["CAACAgQAAxkBAAEFHRditZFgRBAPm-9bkFJUQKOjSEgxoQACfwsAAmgpeVF2roP_0GLhzykE",
                "CAACAgQAAxkBAAEFHRVitZFYQ_EPOF7Y1GenAAHZOfu6xNIAAj4MAAKd3llQRh5-qJlCwa0pBA",
                "CAACAgQAAxkBAAEFHRNitZFVEBwdq0uFJDOvDRx2IzdoCwAC5wwAAubdSFEk6BkQ4EbQ1ikE",
                "CAACAgQAAxkBAAEFHRFitZFRwzQPYrVUQkxVP4yxF2Uw3gAC4AkAAu9GYFGTgHavjO_HLikE",
                "CAACAgQAAxkBAAEFHQ9itZFNixLf7fEZICaK8DF-Li967wACUAwAAmEq4VF8xFsUvkvQXSkE"              
         ]  

START = f"""
𝒉𝒆𝒍𝒍𝒐 𝒑𝒆𝒐𝒑𝒍𝒆𝒔😌

ᚖ𝑰 𝒂𝒎 𝒇𝒂𝒔𝒕 & 𝑺𝒊𝒎𝒑𝒍𝒆 𝑺𝒊𝒏𝒉𝒂𝒍𝒂 & 𝑬𝒏𝒈𝒍𝒊𝒔𝒉 𝑭𝒊𝒍𝒎𝒆 𝒅𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒆𝒓 𝒃𝒐𝒕ᚖ

ᨖ𝑻𝒉𝒊𝒔 𝑩𝒐𝒕 𝒂𝒍𝒔𝒐 𝑰𝒏𝒍𝒊𝒏𝒆 & 𝒈𝒓𝒐𝒖𝒑 𝒔𝒖𝒑𝒑𝒐𝒓𝒕𝒆𝒅

ᨖ𝒀𝒐𝒖 𝑪𝒂𝒏 𝒈𝒆𝒕 𝒂𝒏𝒚 𝑭𝒊𝒍𝒎𝒆 𝒇𝒓𝒐𝒎 𝒖𝒔𝒊𝒏𝒈 𝑻𝒉𝒊𝒔 𝒃𝒐𝒕

ᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔ
ᚗDeveloperᚋ [ɴᴀᴠᴀɴᴊᴀɴᴀ](https://t.me/NA_VA_N_J_NA1)
ᚗPowerd byᚋ [Epic Developers Community🇱🇰](https://t.me/EpicBotsSl)
ᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔ
•`𝓌ℯ𝓁𝒸ℴ𝓂ℯ 𝓉ℴ 𝓉𝒽ℯ 𝓃ℯ𝓌 𝒶ℊℯ`
"""

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
print("Commands.py Started🔥🌹")


@Client.on_message(filters.text & filters.private)
async def sendsret(bot, message):
     await bot.send_message(message.chat.id, f'🔥Search Results For **{message.text}**', reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton("Click Here",switch_inline_query_current_chat=message.text)
                 ]]
                  ))
