import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

STAT_STICKER = ["CAACAgQAAxkBAAEFHRditZFgRBAPm-9bkFJUQKOjSEgxoQACfwsAAmgpeVF2roP_0GLhzykE",
                "CAACAgQAAxkBAAEFHRVitZFYQ_EPOF7Y1GenAAHZOfu6xNIAAj4MAAKd3llQRh5-qJlCwa0pBA",
                "CAACAgQAAxkBAAEFHRNitZFVEBwdq0uFJDOvDRx2IzdoCwAC5wwAAubdSFEk6BkQ4EbQ1ikE",
                "CAACAgQAAxkBAAEFHRFitZFRwzQPYrVUQkxVP4yxF2Uw3gAC4AkAAu9GYFGTgHavjO_HLikE",
                "CAACAgQAAxkBAAEFHQ9itZFNixLf7fEZICaK8DF-Li967wACUAwAAmEq4VF8xFsUvkvQXSkE"              
         ]  

START = f"""
πππππ ππππππππ

π°π°π ππππ & πΊπππππ π­πππ ππππππππππ πππ

α¨π»πππ π©ππ ππππ π°πππππ & πππππ πππππππππ
α¨πππ πͺππ πππ πππ π­πππ ππππ πππππ π»πππ πππ

ααααααααααααααααααα
αDeveloperα [Ι΄α΄α΄ α΄Ι΄α΄α΄Ι΄α΄](https://t.me/NA_VA_N_J_NA1)
αPowerd byα [Epic Developersπ±π°](https://t.me/EpicBotsSl)
ααααααααααααααααααα
β’`πβ―ππΈβ΄πβ― πβ΄ ππ½β― πβ―π πΆββ―`
"""

CLOSE_BUTTON = InlineKeyboardMarkup([[
                InlineKeyboardButton('cloce', callback_data="cloce")
            ]])
