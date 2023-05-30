import telebot
import requests, json
from telebot import types 
import random,time,os,sys
##################################################
own = 5207032121 #id owner
sown = "5207032121" # id owner
ch = "@lk_poi" #channel
tokenn="6249173878:AAEWi5TxQB_5bZ7bZw6AQMhqMGJPX45pXOo" #token
file="data.json"
bot = telebot. TeleBot(tokenn)
#########################
Allow = types.InlineKeyboardButton(text = "اضف عضو👤", callback_data = "allow" )
Deny = types.InlineKeyboardButton(text = "حذف عضو 🙄", callback_data = "deny")
Open = types.InlineKeyboardButton(text = "فتح الوضع المجاني🆓", callback_data = "open")
Close = types.InlineKeyboardButton(text = "تعطيل الوضع المجاني🚫", callback_data = "close")
Block = types.InlineKeyboardButton(text = "حظر عضو ⛔", callback_data = "block")
Unblock = types.InlineKeyboardButton(text = "الغاء حظر عضو ✔️", callback_data = "unblock")
Broudcast = types.InlineKeyboardButton(text = "اذاعه للجميع 📻", callback_data = "broudcast")
Total = types.InlineKeyboardButton(text = "احصائيات البوت📶", callback_data = "total")
Addveiw = types.InlineKeyboardButton(text = "اضف مشاهدات 👁️.", callback_data = "addview")
Kdm = types.InlineKeyboardButton(text = "Kdm Team", url = "t.me/lk_poi")
Whitepro = types.InlineKeyboardButton(text = "hamo", url = "t.me/e_7_h")
#########################
mck = types.InlineKeyboardMarkup()
mck.row_width = 2
mck.add(Open,Close)
mck.add(Allow, Deny)
mck.add(Block, Unblock)
mck.add(Broudcast,Total)
mck.add(Kdm,Whitepro)
#########################
ver= types.InlineKeyboardMarkup()
ver.add(Addveiw)
ver.add(Kdm, Whitepro)
#########################
dev= types.InlineKeyboardMarkup()
dev.add(Whitepro)
#########################
Kdmm= types.InlineKeyboardMarkup()
Kdmm.add(Kdm)
#########################
@bot.message_handler(commands=['start'])
def start(message):
  if message.chat.type == 'private':
    if message.from_user.id != own: #whitepro
        Hb = json.load(open(file, 'r'))
        id = str(message.from_user.id)
        req = requests.get(f'https://api.telegram.org/bot{tokenn}/getChatMember?chat_id={ch}&user_id={id}')
        re=req.text
        try:
            if str(req.json()['result']['status']) == 'left' :
                bot.send_message(message.chat.id, text=f'↯ عليك الاشتراك في قناه البوت لتتمكن من استخدامه🔰\n{ch} .', reply_markup = Kdmm)
            elif "creator" in re or "member" in re or "administrator" in re:
                if id not in Hb["members"] :
                    Hb["total"] = Hb["total"] + 1
                    Hb["members"].append(id)
                    with open(file, "w") as f:
                        json.dump(Hb, f,indent=4)
                    idu = message.from_user.id
                    use = message.from_user.username
                    fr = message.from_user.first_name
                    bot.send_message("5207032121" ,f"""< [{fr}](tg://user?id={idu}) >
𖡋 ID : `{idu}` ✈️
𖡋 User : `@{use}` 🛩️
𖡋 Count : {Hb["total"]}👤""",parse_mode="Markdown")#whitepro
                    bot.reply_to(message,"↯ تم التحقق بنجاح اضغط\n/start . ")
                else:
                    if id in Hb["block"]:
                        bot.reply_to(message,"↯ تم حظرك من البوت 🚫\n↯ تواصل مع المطور لرفع الحظر✔️", parse_mode ="Markdown", reply_markup =dev)
                    else:
                        if id in Hb["allow"]:
                            bot.send_message(message.chat.id,f"""
↯ Hello Sir,[{message.from_user.first_name}](tg://user?id={message.from_user.id}).
↯ You can throw views on Telegram posts 👁️
↯ Powered by : [WHITEPRO](t.me/PPRRO0)""", reply_markup =ver, parse_mode ="Markdown",disable_web_page_preview=True)
                        else:
                            if Hb["statue"] == True:
                                bot.send_message(message.chat.id,f"""
↯ Hello Sir,[{message.from_user.first_name}](tg://user?id={message.from_user.id}).
↯ You can throw views on Telegram posts 👁️
↯ Powered by : [hamo](t.me/e_7_h)""", reply_markup =ver, parse_mode ="Markdown",disable_web_page_preview=True)
                            else:
                                bot.reply_to(message,"↯ عذرا الوضع المجاني معطل ❌\n↯ تواصل مع المطور لشراء التفعيل👨‍💻", parse_mode ="Markdown", reply_markup =dev)
        except Exception as exp:
            bot.send_message(message.chat.id, text=f'↯ عليك الاشتراك في قناه البوت لتتمكن من استخدامه🔰\n{ch} .', reply_markup = Kdmm)
    if message.from_user.id == own: #whitepro
        bot.send_photo(message.chat.id,"https://a.top4top.io/p_2692bwjik1.jpg",f"""↯ Wellcome Sir, [{message.from_user.first_name}](tg://user?id={message.from_user.id}).
↯ Choose an order from the buttons 🦅🐾.
↯ Have anice time \"WHITEPRO\".
""", parse_mode ="Markdown", reply_to_message_id =message.message_id,reply_markup =mck)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "allow" :
    	alloww(call.message)
    if call.data == "deny" : #whitepro
        denyy(call.message)
    if call.data == "open" :
    	openn(call.message)
    if call.data == "close" :
    	closee(call.message)
    if call.data == "block" :
    	blockk(call.message)
    if call.data == "unblock" :
    	unblockk(call.message)
    if call.data == "broudcast" :
    	broudcastt(call.message)
    if call.data == "total" :
    	totall(call.message)
    if call.data == "addview" :
    	addvieww(call.message)
def alloww(message):
    mj = bot.send_message(message.chat.id,text="""
↯ حسنا عزيزي ارسل ايدي العضو الان.""",parse_mode ="Markdown")
    bot.register_next_step_handler(mj,user)
def user(message):
    global msg
    msg = message.text
    #print(msg)
    Hb = json.load(open(file, 'r'))
    #print(Hb)
    if msg in Hb["allow"]:
        bot.reply_to(message,"↯ العضو في قائمه السماح بالفعل ✔️.")
    else:
        #print("white")
        Hb["allow"].append(msg)
        with open(file, "w") as f:
            json.dump(Hb, f,indent=4)
        #print(Hb)
        bot.reply_to(message,"↯ تم اضافه العضو في قائمه السماح بنجاح ✔️.")
def denyy(message):
    mj = bot.send_message(message.chat.id,text="""
↯ حسنا عزيزي ارسل ايدي العضو الان.""",parse_mode ="Markdown")
    bot.register_next_step_handler(mj,bvbvb)
def bvbvb(message):
    global msg
    msg = message.text
    #print(msg)
    Hb = json.load(open(file, 'r'))
    #print(Hb)
    if msg not in Hb["allow"]:
        bot.reply_to(message,"↯ العضو محذوف من القائمه من قبل 🚫.")
    else:
        #print("white")
        Hb["allow"].remove(msg)
        with open(file, "w") as f:
            json.dump(Hb, f,indent=4)
        #print(Hb)
        bot.reply_to(message,"↯ تم حذف العضو من القائمه بنجاح.✔️")
def openn(message):
    Hb = json.load(open(file, 'r'))
    if Hb["statue"] == True:
        bot.send_message(message.chat.id,"""↯ الوضع المجاني مفتوح بالفعل✔️.""")
    else:
        Hb["statue"] = True
        with open(file, "w") as f:
            json.dump(Hb, f,indent=4)
        bot.send_message(message.chat.id,"""↯ تم فتح الوضع المجاني في البوت✔️.""")
def closee(message):
    Hb = json.load(open(file, 'r'))
    if Hb["statue"] == False:
        bot.send_message(message.chat.id,"""↯ الوضع المجاني مغلق بالفعل🚫.""")
    else:
        Hb["statue"] = False
        with open(file, "w") as f:
            json.dump(Hb, f,indent=4)
        bot.send_message(message.chat.id,"""↯ تم غلق الوضع المجاني في البوت🚫.""")
def blockk(message):
    mj = bot.send_message(message.chat.id,text="""
↯ حسنا عزيزي ارسل ايدي العضو الان.""",parse_mode ="Markdown")
    bot.register_next_step_handler(mj,usersr)
def usersr(message):
    global msg
    msg = message.text
    #print(msg)
    Hb = json.load(open(file, 'r'))
    #print(Hb)
    if msg in Hb["block"]:
        bot.reply_to(message,"↯ العضو محظور من البوت بالفعل 🚫.")
    else:
        #print("white")
        Hb["block"].append(msg)
        with open(file, "w") as f:
            json.dump(Hb, f,indent=4)
        #print(Hb)
        bot.reply_to(message,"↯ تم حظر العضو من البوت بنجاح 🚫.")
def unblockk(message):
    mj = bot.send_message(message.chat.id,text="""
↯ حسنا عزيزي ارسل ايدي العضو الان.""",parse_mode ="Markdown")
    bot.register_next_step_handler(mj,usersrr)
def usersrr(message):
    global msg
    msg = message.text
    #print(msg)
    Hb = json.load(open(file, 'r'))
    #print(Hb)
    if msg not in Hb["block"]:
        bot.reply_to(message,"↯ العضو غير محظور من البوت بالفعل ✔️.")
    else:
        #print("white")
        Hb["block"].remove(msg)
        with open(file, "w") as f:
            json.dump(Hb, f,indent=4)
        #print(Hb)
        bot.reply_to(message,f"↯ تم إلغاء حظر العضو `{msg}`\nمن البوت بالفعل✔️.", parse_mode ="Markdown")
def broudcastt(message):
    mj = bot.send_message(message.chat.id,text="""
↯ حسنا عزيزي ارسل ما تريد اذاعته الان.""",parse_mode ="Markdown")
    bot.register_next_step_handler(mj,usersrrb)
def usersrrb(message):
    global msg
    msg = message.text
    Hb = json.load(open(file, 'r'))
    on=-1
    of=0
    xv=bot.send_message(message.chat.id,f"↯ تم الاذاعه الي : {on}\n↯ عدد من قاموا بحظر البوت : {of}", reply_to_message_id =message.message_id )
    for i in range(len(Hb["members"])):
        on=on+1
        id = Hb["members"][on]
        try:
            bot.send_message(f"{id}",msg)
            bot.edit_message_text(chat_id=message.chat.id,message_id=xv.message_id, text=f"↯ تم الاذاعه الي : {on}\n↯ عدد من قاموا بحظر البوت : {of}")
        except:
            bot.edit_message_text(chat_id=message.chat.id,message_id=xv.message_id,text=f"↯ تم الاذاعه الي : {on}\n↯ عدد من قاموا بحظر البوت : {of}")
            of=of+1
            pass
    bot.edit_message_text(chat_id=message.chat.id,message_id=xv.message_id, text=f"↯ تم الانتهاء من الاذاعه بنجاح ✔️\n↯ تم الاذاعه الي : {on}\n↯ عدد من قاموا بحظر البوت : {of}")
def totall(message):
    Hb = json.load(open(file, 'r'))
    count=Hb["total"]
    bot.reply_to(message,f"""↯ اليك احصائيات البوت عزيزي ❤️👨‍👩‍👧‍👦
↯ عدد الأعضاء : `{count}` 👥
↯ لغه البوت : `Python` 🐍
↯ اصدار البايثون : `3.10` ⚡
↯ المطور : [hamo](t.me/e_7_h) 👨‍💻
""", parse_mode ="Markdown")
def addvieww(message):
    Hb = json.load(open(file, 'r'))
    id = str(message.chat.id)
    if id in Hb["block"]:
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="↯ تم حظرك من البوت 🚫\n↯ تواصل مع المطور لرفع الحظر✔️", parse_mode ="Markdown", reply_markup =dev)
    else:
        if id in Hb["allow"]:
            Rb=bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="↯ حسنا عزيزي ارسل رابط البوست الان 👁️.\n↯ مثال : \n*https://t.me/L_e_a_r_n/3019*", parse_mode ="Markdown", reply_markup =dev, disable_web_page_preview=True)
            bot.register_next_step_handler(Rb,veiwsss)
        else:
             if Hb["statue"] == True:
                 Rb=bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="↯ حسنا عزيزي ارسل رابط البوست الان 👁️.\n↯ مثال : \n*https://t.me/L_e_a_r_n/3019*", parse_mode ="Markdown", reply_markup =dev, disable_web_page_preview=True)
                 bot.register_next_step_handler(Rb,veiwsssone)
             else:
                 bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="↯ عذرا الوضع المجاني معطل ❌\n↯ تواصل مع المطور لشراء التفعيل👨‍💻", parse_mode ="Markdown", reply_markup =dev)
def veiwsss(message):
    global msg
    msg = message.text
    if "https://t.me/" in msg:
        rr=requests.get("https://dev-mnsdert.pantheonsite.io/CODR/Add.php?d="+msg)
        localtime=time.asctime(time.localtime(time.time()))
        bot.reply_to(message,f"""↯ تم إرسال طلبك بنجاح✔️
↯ العدد 👁️ : `1000` مشاهده
↯ الوقت 📆 : `{localtime}`
↯ البوست 🖇️ : `{msg}`
""", parse_mode ="Markdown", reply_markup =dev)
    else:
        bot.reply_to(message,"↯ عذرا هذا الرابط غير صحيح❌")
def veiwsssone(message):
    global msg
    msg = message.text
    id = str(message.from_user.id)
    Hb = json.load(open(file, 'r'))
    if id in Hb["coins"]:
        if Hb["coins"][id] == 0:
            bot.reply_to(message,"↯ عذرا لقد نفذت نقاطك 🪙\n↯ تواصل مع المطور لشراء نقاط او للتفعيل✔️", reply_markup =dev, parse_mode ="Markdown")
        else:
            Hb["coins"][id] = Hb["coins"][id]-1
            with open(file, "w") as f:
                json.dump(Hb, f,indent=4)
            rr=requests.get("https://dev-mnsdert.pantheonsite.io/CODR/Add.php?d="+msg)
            localtime=time.asctime(time.localtime(time.time()))
            bot.reply_to(message,f"""↯ تم إرسال طلبك بنجاح✔️
↯ العدد 👁️ : `1000` مشاهده
↯ الوقت 📆 : `{localtime}`
↯ الكوينزات المتبقيه 🪙 : `{Hb["coins"][id]}`
↯ البوست 🖇️ : `{msg}`
""", parse_mode ="Markdown", reply_markup =dev)
    else:
        Hb["coins"][id] = 2
        with open(file, "w") as f:
            json.dump(Hb, f,indent=4)
        rr=requests.get("https://dev-mnsdert.pantheonsite.io/CODR/Add.php?d="+msg)
        localtime=time.asctime(time.localtime(time.time()))
        bot.reply_to(message,f"""↯ تم إرسال طلبك بنجاح✔️
↯ العدد 👁️ : `1000` مشاهده
↯ الوقت 📆 : `{localtime}`
↯ الكوينزات المتبقيه 🪙 : `{Hb["coins"][id]}`
↯ البوست 🖇️ : `{msg}`
""", parse_mode ="Markdown", reply_markup =dev)
bot.infinity_polling()
