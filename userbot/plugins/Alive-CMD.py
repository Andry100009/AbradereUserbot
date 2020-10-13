# Copyright © 2020 di Abradere Github, <https://github.com/Andry100009>.
#
# Questo file fa parte del progetto <https://github.com/Andry100009/AbradereUserbot>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/Andry100009/AbradereUserbot/blob/master/LICENSE>
#
# Tutti i diritti riservati a @Abradere.

import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, bot, versions
from userbot.system import dev_cmd

currentversion = "1.0-Beta"

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Errore-No-Username"
# ============================================

@bot.on(dev_cmd(pattern=f"alive", outgoing=True))
async def amireallyalive(alive):
    """ Comando .alive per vedere lo stato del bot """
    await alive.edit("**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n"
                     f"↬ **Ⲋⲧⲇⲧⲟ Ⳙ⳽ⲉⲅⲃⲟⲧ**: `ᴏηƖɪηє`\n"
                     f"↬ **ʋᥱɾ⳽ɩoᥒᥱ**: `{currentversion}`\n"
                     f"↬ **Ⳙ⳽ⲉⲅⲃⲟⲧ 𝖽ⲓ**: `{DEFAULTUSER}`\n\n"
                     f"↬ **𝙘𝙤𝙥𝙞𝙧𝙞𝙜𝙝𝙩 𝙗𝙮**  [Founder](http://t.me/TurboCompressore)\n"
                     "↬ **ɢʀʊքքօ** [𝗟𝗘 🅱️𝗔𝗠🅱️𝗜𝗡𝗘 𝗗𝗜 𝗔𝗟𝗣𝗔𝗧𝗢𝗞🤡](http://t.me/lebambineditiktokredirect)\n")
