from pyrogram import Client, Filters
app = Client("baaz",869912,"a7b049e08df35464047d57e5134327e5")
d = -1001378725482
@app.on_message( Filters.text & ~Filters.edited)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
    text = message.text
    f = False
    words = ['dekho','fix','๐ฑ','๐ข','๐ณ','fixer','๐','๐','match','pass','sab','chase','defend','hai','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐ฅบ','members','๐','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','๐ค','๐ค','โ๏ธ','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','โ','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','๐ค','LUND',"?","LU"]
    for word in words:
        if word.casefold() in text.casefold():
            f = True
    if not f:
     mes = client.send_message(d, "<b>" + message.text + "</b>", parse_mode="html" )
     files = open("sure.txt" , "a")
     files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
     files.close()  
@app.on_message( Filters.text & Filters.edited)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   file = open("sure.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
     try:
      client.edit_message_text(d,int(x[x.index(id)+1]),"<b>" + message.text.replace("๐ฉ๐ช","๐ณ๐ฎ").replace("๐พ","๐ฅ").replace("๐ฒ","๐งค").replace("๐","๐").replace("WD","๐ท WIDE BALL ๐ท").replace("/","~").replace("CHALU RAKHO","GAME STARTED, PLAYERS ON THE STEDIUM ").replace("NB","๐ท NO BALL ๐ท") + "</b>", parse_mode="html" )
     except FloodWait as e:
      time.sleep(e.x)
@app.on_message(Filters.command("clear"))
def forward(client, message):
 with open("sure.txt" , "w") as file:
  file.write("001 002")
  file.close()
@app.on_message(Filters.command("set"))
def forward(client, message):
  with open("source.txt" , "w") as file:
   file.write(message.text.split(' ')[1])
   file.close()
app.run()
