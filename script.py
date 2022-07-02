import os
from pyrogram import Client, filters
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup

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
