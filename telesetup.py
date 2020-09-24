from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Vai su my.telegram.org
Fai il login nel tuo account Telegram
Click API Development Tools
Crea una nuova applicazione e inserisci i requisiti necessari""")
APP_ID = int(input("Inserisci APP ID qui: "))
API_HASH = input("Inserisci API HASH qui: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
