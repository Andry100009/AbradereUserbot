# Copyright © 2020 di Abradere Github, <https://github.com/Andry100009>.
#
# Questo file fa parte del progetto <https://github.com/Andry100009/AbradereUserbot>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/Andry100009/AbradereUserbot/blob/master/LICENSE>
#
# Tutti i diritti riservati a @Abradere.

from telethon import functions
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern="invite ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n__Sei scemo porco dio? esegui il comando `.invite` in un gruppo non in chat privata coglione.__")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            for user_id in to_add_users.split(" "):
                try:
                    await bot(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n✔️ Utente aggiunto correttamente!")
        else:
            for user_id in to_add_users.split(" "):
                try:
                    await bot(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n✔️ Utente aggiunto correttamente!")

async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n__Sei scemo porco dio? esegui il comando `.invite` in un gruppo non in chat privata coglione.__")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            for user_id in to_add_users.split(" "):
                try:
                    await bot(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.reply("**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n✔️ Utente aggiunto correttamente!")
        else:
            for user_id in to_add_users.split(" "):
                try:
                    await bot(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.reply("**♨️ AʙʀᴀᴅᴇʀᴇUsᴇʀʙᴏᴛ 🔍**\n\n✔️ Utente aggiunto correttamente!")
