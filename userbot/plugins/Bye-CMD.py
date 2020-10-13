# Copyright © 2020 di Abradere Github, <https://github.com/Andry100009>.
#
# Questo file fa parte del progetto <https://github.com/Andry100009/AbradereUserbot>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/Andry100009/AbradereUserbot/blob/master/LICENSE>
#
# Tutti i diritti riservati a @Abradere.

import time

from telethon.tl.functions.channels import LeaveChannelRequest
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("bye", outgoing=True))
async def bye(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit('**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n**⚠️ Abbandono questo gruppo di merda!**')
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n**❌ Puoi abbandonare un gruppo,**\n**❌ Non una chat privata coglione.**')
