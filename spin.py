from pyrogram import Client, Filters, Emoji
import random
from datetime import datetime
import time
app = Client("session",bot_token="691205521:AAEHy793MZQi7tvxTNAJ62XvPt4VvQiie-E",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

@app.on_message(Filters. command('getlink'))
def ran(client, Message):
 if Message.from_user.id == 491634139:
  if len(Message.text.split( )) > 1:
   Message.reply(client.export_chat_invite_link(int(Message.text.split(' ')[1])))

@app.on_message(Filters.command('spin'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
  x = random.choice(["1","2","3","4","5","6","7","8","9","10","5","6","4","10","3","2","1","10","5","7","8"])
  if x == "1":
   client.send_animation(message.chat.id, "CgADBQADhQADwMtgVU8anppTsg2LAg" )
  if x == "2":
   client.send_animation(message.chat.id, "CgADBQADhwADwMtgVbe__SA8_sZuAg" )
  if x == "3":
   client.send_animation(message.chat.id, "CgADBQADiQADwMtgVQOdkZJfBQiPAg" )
  if x == "4":
   client.send_animation(message.chat.id, "CgADBQADiwADwMtgVYw4-G7BJ8jQAg" )
  if x == "5":
   client.send_animation(message.chat.id, "CgADBQADjQADwMtgVVAkLqg-aFvAAg" )
  if x == "6":
   client.send_animation(message.chat.id, "CgADBQADjgADwMtgVWRs70v3XQHHAg" )
  if x == "7":
   client.send_animation(message.chat.id, "CgADBQADkwADwMtgVflXO-FbOZrIAg" )
  if x == "8":
   client.send_animation(message.chat.id, "CgADBQADlgADwMtgVQORjNELCu7IAg" )
  if x == "9":
   client.send_animation(message.chat.id, "CgADBQADmgADwMtgVWVbSXzHW3dGAg" )
  if x == "10":
   client.send_animation(message.chat.id, "CgADBQADmQADwMtgVaKH0P14GehhAg" )
@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 491634139:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
@app.on_message(Filters. private & Filters.command("start"))
def ran( client, message) :
  message.reply( """♻️ This is Gamebot created by a wonderful [person](https://t.me/Google_console) ✍️.
My commands :
👉 flip a coin 
1. /toss
👉 for bowling
2. /bowl {bowl no.}
👉 For show user cards
3. /show {username}
👉 for spin numbers
4. /spin
👉 for sps
5. /sps
👉 for even odd
6. /dice or /roll {range}
👉 for double roll
7. /droll {range} or /dice2
👉 for decision
8. /decide
👉 for roulette
9. /rolls
All command exist only Admins in Super groups ✍️.
For buy [click here](https://t.me/google_console)
 """,disable_web_page_preview = True )
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
@app.on_message(Filters.command('ani'))
def ran(client, message):
  print(message.reply_to_message.animation.file_id)
  client.send_message(message.chat.id,message.reply_to_message.animation.file_id)

@app.on_message(Filters.new_chat_members)
def joined(client, Message):
    for i in Message.new_chat_members:
     if i.id == 691205521:
      client.send_message(-1001250871922,"I am added to " + str(Message.chat.id))
         

app.run()
