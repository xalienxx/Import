from pyrogram import Client, Filters, Emoji
import random
import time
app = Client("session",bot_token="622131522:AAHordhdDvQ08qLmEsVl3U4Nkb2S-aEAJr8",api_id=715451,api_hash="d2cba6f7bf5d1a45682da5bb9071a307")
@app.on_message(Filters. private & Filters.command("start"))
def ran( client, message) :
  message.reply( """♻️ This is antiusername created by a wonderful [person](https://t.me/Google_console) ✍️.
Add me to your group i will delete username from non admins automatically.""")
@app.on_message(Filters.group)
def main(client, message):
 if not message.from_user:
  message.delete(message.message_id)
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if not b == 'administrator' or not b == "creator": 
  if "@" in message.text: 
   client.delete_messages(message.chat.id, message.message_id)
app.run()
