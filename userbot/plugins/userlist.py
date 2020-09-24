"""Get Administrators of any Chat*
Syntax: .userlist"""
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from userbot.system import dev_cmd
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
                                          
@bot.on(events.NewMessage(pattern=r"\.userlist ?(.*)", outgoing=True))
async def get_users(show):
    """ Il comando .userslist per visualizzare gli utenti presenti nel gruppo """
    if not show.text[0].isalpha() and show.text[0] not in ("/", "#", "@", "!"):
        if not show.is_group:
            await show.edit("Dio bastardo te ne sei reso conto che non sei in un gruppo? Impiccati e riprova!")
            return
        info = await show.client.get_entity(show.chat_id)
        title = info.title if info.title else "In questa chat"
        mentions = 'Utenti {}: \n'.format(title)
        try:
            if not show.pattern_match.group(1):
                async for user in show.client.iter_participants(show.chat_id):
                    if not user.deleted:
                        mentions += f" @{user.username}"
                    else:
                        mentions += f"\nAccount Eliminato `{user.id}`"
            else:
                searchq = show.pattern_match.group(1)
                async for user in show.client.iter_participants(show.chat_id, search=f'{searchq}'):
                    if not user.deleted:
                        mentions += f" @{user.username}"
                    else:
                        mentions += f"\nAccount Eliminato `{user.id}`"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        try:
            await show.edit(mentions)
        except MessageTooLongError:
            await show.edit("Dio Laido, questo gruppo è enorme, gli utenti sono stati salvati in un file")
            file = open("Utenti.txt", "w+")
            file.write(mentions)
            file.close()
            await show.client.send_file(
                show.chat_id,
                "Utenti.txt",
                caption='Utenti {}'.format(title),
                reply_to=show.id,
            )
            remove("Utenti.txt")