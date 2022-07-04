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
from script import *
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
        if -1001618730343:
            await client.send_message(
                -1001618730343,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.reply_video("https://telegra.ph/file/64865d56582fa87eba003.mp4", caption=START, reply_markup=ST_BTN)
       
DATABASE_URI=DATABASE_URI
database = Database(DATABASE_URI, "filme_epic") 
    
#•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#State chek

@Client.on_message(filters.command("state") & filters.user(ADMINS))   
async def startprivate(bot, message):
    countb = await database.total_users_count()
    countb = await database.total_users_count()
    count = await bot.get_chat_members_count(-1001620454933)
    counta = await bot.get_chat_members_count(-1001620454933)
    text=f"""**𝔱𝔬𝔱𝔞𝔩 𝔲𝔰𝔢𝔯𝔰**
**𝔱𝔢𝔞𝔪 & 𝔟𝔬𝔱 𝔪𝔢𝔪𝔟𝔢𝔯 𝔠𝔬𝔲𝔫𝔱**
ᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔ
   **𝔠𝔥𝔞𝔫𝔢𝔩 𝔰𝔱𝔞𝔱𝔢**  🏅`{count}`
   **𝔣𝔦𝔩𝔪𝔢 𝔟𝔬𝔱 𝔰𝔱𝔞𝔱𝔢**  🏅`{countb}`
ᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔ
"""
    await bot.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await bot.send_message(message.chat.id, text=text)


ST_BTN = InlineKeyboardMarkup([[
                InlineKeyboardButton('➕ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ➕', url="https://t.me/EpicFilmeBot?startgroup=true")
            ],
            [
                InlineKeyboardButton('࿉ᴍʏ ꜰɪʟᴍ ᴅᴀᴛᴀʙᴀꜱᴇ࿉', url='https://t.me/+tZqaN4Us6YM2ZjRl')
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


#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
print("Commands.py Started🔥🌹")


@Client.on_message(filters.text & filters.private)
async def sendsret(bot, message):
     await bot.send_message(message.chat.id, f'🔥Search Results For **{message.text}**', reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton("Click Here",switch_inline_query_current_chat=message.text)
                 ]]
                  ))


print("main.py Started Successfully 🍎🍓")
