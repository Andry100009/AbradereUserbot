# Copyright © 2020 di Abradere Github, <https://github.com/Andry100009>.
#
# Questo file fa parte del progetto <https://github.com/Andry100009/AbradereUserbot>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/Andry100009/AbradereUserbot/blob/master/LICENSE>
#
# Tutti i diritti riservati a @Abradere.

"""Gestione dell'userbot
Comandi:
.riavvia
.spegniuserbot"""
import asyncio
import os
import sys

from telethon import events
from userbot import bot, ALIVE_NAME
from userbot.system import dev_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Errore-No-Username"


@bot.on(dev_cmd("riavvia"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n✔️ **Riavvio in corso...**\n⚠️ **Sarò online tra 2min prova con `.alive`**")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@bot.on(dev_cmd("spegniuserbot"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n💢 **Userbot spento**\n📛 **Avviami manualmente da heroku**")
    await bot.disconnect()
